import argparse
import math
import os
import sys
import win32com.shell.shell as shell

from pythonosc import dispatcher
from pythonosc import osc_server


def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)

def connect_to_tcp():
    print("starting")
    # Connect to TCP Port
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()

    new_dispatcher = dispatcher.Dispatcher()
    new_dispatcher.map("/debug", print)
    new_dispatcher.map("/muse/eeg", eeg_handler, "EEG")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), new_dispatcher)
    print("Serving on {}".format(server.server_address))

    # Collect from port
    server.serve_forever()



def connect_to_tcp_admin():
    ASADMIN = 'asadmin'

    # Get admin permissions on Windows
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

    connect_to_tcp()
    input('Press ENTER to exit')

if __name__ == "__main__":
    connect_to_tcp_admin()
    os.system("pause")



