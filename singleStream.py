# get TRex APIs
from trex_stl_lib.api import *

c = STLClient(server = '127.0.0.1')
c.connect()

try:
    # create a base pkt
    base_pkt = Ether()/IP(src="16.0.0.1",dst="48.0.0.1")/UDP(dport=12,sport=1025)

    # later on we will use the packet builder to provide more properties
    pkt = STLPktBuilder(base_pkt)

    # create a stream with a rate of 1000 PPS and continuous
    s1 = STLStream(packet = pkt, mode = STLTXCont(pps = 1000))

    # prepare the ports
    c.reset(ports = [0, 1])

    # add the streams
    c.add_streams(s1, ports = 0)

    # start traffic with limit of 3 seconds (otherwise it will continue forever)
    c.start(ports = 0, duration = 3)

    # hold until traffic ends
    c.wait_on_traffic()


except STLError as e:
    print(e)

finally:

    c.disconnect()