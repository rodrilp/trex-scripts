# get TRex APIs
from trex_stl_lib.api import *

def simple():

    # create client
    c = STLClient(server = '127.0.0.1')
    passed = True

    try:
        # connect to server
        c.connect()

        my_ports=[0,1]

        # prepare our ports
        c.reset(ports = my_ports)

        profile_file =   "/trex/v2.88/stl/udp_1pkt_simple.py"   # a traffic profile file

        try:                                                    # load a profile
            profile = STLProfile.load(profile_file)
        except STLError as e:
            print (format_text("\nError while loading profile '{0}'\n".format(profile_file), 'bold'))
            print (e.brief() + "\n")
            return

        print (profile.to_json())

        c.remove_all_streams(my_ports)                          # remove all streams

        c.add_streams(profile.get_streams(), ports = my_ports)  # add them

        c.start(ports = [0, 1], mult = "5mpps", duration = 10)  # start for 10 sec

        # block until done
        c.wait_on_traffic(ports = [0, 1])                       # wait


    finally:
        c.disconnect()

simple()