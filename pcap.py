# get TRex APIs
from trex_stl_lib.api import *

c = STLClient(server = '127.0.0.1')
c.connect()

try:
    c.reset(ports = [0, 1])

    # push local PCAP file 'http.pcap' over port_0 with IPG of 1 ms
    c.push_pcap('../avl/https.pcap', ports = 0, ipg_usec = 1000)

    # hold until traffic ends
    c.wait_on_traffic()

    # check out the stats
    stats = c.get_stats()

    # examine stats for port_0
    print("port_0 stats:")
    print(stats[0])

    # examine stats for port_1
    print("port_1 stats:")
    print(stats[1])

except STLError as e:
    print(e)

finally:

    c.disconnect()