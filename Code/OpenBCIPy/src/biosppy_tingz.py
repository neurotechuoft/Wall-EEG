import csv
from biosppy.signals import tools as st
import matplotlib.pyplot as plt
import numpy as np



if __name__ == '__main__':

    data = []
    # INTERPRET EACH LINE
    #with open('2016-8-23_17-52-48.csv', 'rb') as ecg_file:
    with open('OpenBCI-RAW-aaron_ecg_1.csv', 'rb') as ecg_file:
        ecg_reader = csv.reader(ecg_file, delimiter=',')

        counter = 0

        for row in ecg_reader:
            #print(row)
            #print("\n")

            data.append(float(str(row[1])))
            counter+= 1

    data_arr = np.array(data)

    sampling_rate = 256.0  # sampling rate
    Ts = 1.0 / sampling_rate  # sampling interval
    t = []

    for i in range(0, len(data)):
        t.append(i*Ts)

    order = int(0.3 * sampling_rate)

    # filtered_data = ecg.ecg(data_arr, 256, False)['filtered']
    filtered_data, _, _ = st.filter_signal(signal=data_arr,
                                           ftype='FIR',
                                           band='bandpass',
                                           order=order,
                                           frequency=[3, 45],
                                           sampling_rate=sampling_rate)

    print(filtered_data)

    plt.plot(t, filtered_data, 'r')
    #plt.plot(t, data, 'b')
    plt.xlabel("Time")
    plt.ylabel("Amplitude (V)")

    plt.show()