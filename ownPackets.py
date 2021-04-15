# get TRex APIs
from trex_stl_lib.api import *

c = STLClient(server = '127.0.0.1')
c.connect()

try:
    # create a base packet with scapy
    base_pkt = Ether()/IP(src='5.6.7.8', dst='10.10.10.1')/UDP(sport=5050)

    # create a list of 100 packets
    pkts = [base_pkt['UDP'].dport = p for p in range(1024, 1124)]

    # inject the packets
    c.push_packets(pkts, ports = [port_0])

    # hold until traffic ends
    c.wait_on_traffic()


except STLError as e:
    print(e)

finally:

    c.disconnect()