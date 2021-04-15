# get TRex APIs
from trex_stl_lib.api import *

base_pkt =  Ether()/IP(src="16.0.0.1",dst="48.0.0.1")/UDP(dport=12,sport=1025)
base_pkt1 =  Ether()/IP(src="16.0.0.2",dst="48.0.0.1")/UDP(dport=12,sport=1025)
base_pkt2 =  Ether()/IP(src="16.0.0.3",dst="48.0.0.1")/UDP(dport=12,sport=1025)
pad = max(0, size - len(base_pkt)) * 'x'

s1 = STLProfile( [ STLStream( isg = 1.0, # star in delay in usec
                                packet = STLPktBuilder(pkt = base_pkt/pad),
                                mode = STLTXCont( pps = 10),
                                ),

                        STLStream( isg = 2.0,
                                packet  = STLPktBuilder(pkt = base_pkt1/pad),
                                mode    = STLTXCont( pps = 20),
                                ),

                        STLStream(  isg = 3.0,
                                    packet = STLPktBuilder(pkt = base_pkt2/pad),
                                    mode    = STLTXCont( pps = 30)

                                )
                    ]).get_streams()

c = STLClient(server = '127.0.0.1')

try:
    # connect to server
    c.connect()

    # prepare our ports (my machine has 0 <--> 1 with static route)
    c.reset(ports = [0, 1])

    # add both streams to ports
    c.add_streams(s1, ports = [0])

    # clear the stats before injecting
    c.clear_stats()

    c.start(ports = [0, 1], mult = "5kpps", duration = 10)

    # block until done
    c.wait_on_traffic(ports = [0, 1])

    # check for any warnings
    if c.get_warnings():
      # handle warnings here
      pass

except STLError as e:
    print(e)

finally:
    c.disconnect()