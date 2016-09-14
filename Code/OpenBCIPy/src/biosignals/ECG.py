import csv
from biosppy.signals import tools as st
from biosignals.BioSignal import BioSignal
from scipy.signal import butter, lfilter
import numpy as np
#from scipy.fftpack import rfft, irfft


class ECG(BioSignal):
    # CONSTRUCTORS--------------------------------------------------------------
    def __init__(self, sample_rate):
        # SUPERCLASS
        BioSignal.__init__(self)

        # ATTRIBUTES------------------------------------------------------------

        # Vitals stats
        self.ecgList = []
        self.ecgListFFT = []

        # Board Characteristics
        self.sample_rate = sample_rate

    # FACTORY METHODS-----------------------------------------------------------
    # GETTERS, SETTERS----------------------------------------------------------

    # METHODS-------------------------------------------------------------------
    def update(self, sample):
        # Extract data needed: time, Einthoven vector
        # sample[2] : data from SRB-N1P
        data_to_add = [float(sample[0]), (float(sample[2]))/1000000.0]

        # Append to ECG list
        self.ecgList.append(data_to_add)

        # Apply bandpass filter
        self.ecgListFFT = self.biosppy_bandpass(self.ecgList)
        # self.ecgListFFT = self.butter_bandpass_filter(self.ecgList, 2, 45)
        #self.ecgListFFT = self.bandpass(self.ecgList, 2, 45)
        #self.ecgListFFT = self.remove_sixty_hz(self.ecgList)

        print((self.ecgListFFT[len(self.ecgListFFT) - 1]))
        #print(self.ecgListFFT)
        #print(data_to_add)

    def update_ecg(self):
        '''
        :return: None
        '''
        # OPEN CSV AND READ LINES
        with open('./../packets.csv', 'rb') as ecg_file:
            ecg_reader = csv.reader(ecg_file, delimiter=self.COMMA_DELIMITER)

            # INTERPRET EACH LINE
            for row in ecg_reader:
                # Extract data needed
                data_to_add = []
                data_to_add.append(row[0])
                data_to_add.append(float(row[3]) - float(row[2]))  # Einthoven
                # Append to ECG list
                self.ecgList.append(data_to_add)


    # HELPER FUNCTIONS----------------------------------------------------------
    def biosppy_bandpass(self, data_time_pair):
        ret_list = []
        data = []

        # Give enough data points to filter properly
        if len(data_time_pair) > 300:
            # Extract vals
            for point in data_time_pair:
                data.append(point[1])

            # Calculate order of filter
            order = int(0.3 * self.sample_rate)

            # Apply filters
            filtered_data, _, _ = st.filter_signal(signal=data,
                                                   ftype='FIR',
                                                   band='bandpass',
                                                   order=order,
                                                   frequency=[1, 58],
                                                   sampling_rate=self.sample_rate)

            # MIGHT NEED TO CONVERT filtered_data INTO A LIST!!!

            # Recompile data with times
            for i in range(0, len(data_time_pair)):
                ret_list.append([data_time_pair[i][0], filtered_data[i]])
        else:
            ret_list = data_time_pair

        return ret_list

    # def biosppy_old_bandpass(self, data_time_pair):
    #     ret_list = []
    #     data = []
    #
    #     if len(data_time_pair) > 600:
    #         # Extract vals
    #         for point in data_time_pair:
    #             data.append(point[1])
    #
    #         # Apply filters
    #         filtered_data = ecg.ecg(np.array(data), 256, False)[
    #             'filtered'].tolist()
    #
    #         # Recompile data with times
    #         for i in range(0, len(data_time_pair)):
    #             ret_list.append([data_time_pair[i][0], filtered_data[i]])
    #     else:
    #         ret_list = data_time_pair
    #
    #     return ret_list

    def butter_bandpass(self, lowcut, highcut, order=5):
        nyq = 0.5 * self.sample_rate
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def butter_bandpass_filter(self, data_time_pair, lowcut, highcut, order=5):
        ret_list = []
        data = []

        # Extract vals
        for point in data_time_pair:
            data.append(point[1])

        # Apply Butterworth Filter
        b, a = self.butter_bandpass(lowcut, highcut, order=order)
        filtered_data = lfilter(b, a, data)

        # Recompile data with times
        for i in range(0, len(data_time_pair)):
            ret_list.append([data_time_pair[i][0], filtered_data[i]])

        return ret_list

    # def bandpass(self, data_list, min_hz, max_hz):
    #     fft_list = []
    #     values_to_fft = []
    #     result_vals = []
    #     ret_list = []
    #
    #     # Extract vals
    #     for point in data_list:
    #         values_to_fft.append(point[1])
    #
    #     fft_list = rfft(values_to_fft)
    #
    #     # Filter
    #     for i in range(len(fft_list)):
    #         if not (min_hz < i/2+1 < max_hz): fft_list[i] = 0
    #
    #     result_vals = irfft(fft_list)
    #
    #     # Package new vals
    #     for i in range(0, len(data_list)):
    #         ret_list.append([data_list[i][0], result_vals[i]])
    #
    #     return ret_list
    #
    # def remove_freq_range(self,data_list, min_hz, max_hz):
    #     fft_list = []
    #     values_to_fft = []
    #     result_vals = []
    #     ret_list = []
    #
    #     # Extract vals
    #     for point in data_list:
    #         values_to_fft.append(point[1])
    #
    #     fft_list = rfft(values_to_fft)
    #
    #     # Filter
    #     for i in range(len(fft_list)):
    #         if (min_hz < i/2+1 < max_hz): fft_list[i] = 0
    #
    #     result_vals = irfft(fft_list)
    #
    #     # Package new vals
    #     for i in range(0, len(data_list)):
    #         ret_list.append([data_list[i][0], result_vals[i]])
    #
    #     return ret_list
    #
    # def remove_sixty_hz(self, data_list):
    #     return self.remove_freq_range(data_list, 58, 62)


if __name__ == '__main__':
    with open('./../packets_ffted.csv', 'rb') as ecg_file:
        # INTERPRET EACH LINE
        ecg_reader = csv.reader(ecg_file, delimiter=',')

        for row in ecg_reader:
            print(row)
            print("\n")

    # ecg = ECG('./../packets.csv', '', '')
    # ecg.update_ecg()
