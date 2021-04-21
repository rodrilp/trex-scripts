# get TRex APIs
from trex_stl_lib.api import *


# create client
c = STLClient(server = '127.0.0.1')

try:
    c.connect()

    scapy_pkt = Ether()/IP()/UDP()/('x' * 100)
    packet = STLPktBuilder(pkt = scapy_pkt)

    s1 = STLStream(name = 's1',
                    packet = packet,
                    mode = STLTXSingleBurst(total_pkts = 1000),
                    next = 's2')
    s2 = STLStream(name = 's2',
                    packet = packet,
                    mode = STLTXSingleBurst(total_pkts = 2000),
                    next = 's3')
    s3 = STLStream(name = 's3',
                    packet = packet,
                    mode = STLTXSingleBurst(total_pkts = 3000))

    c.reset()

    c.add_streams(ports = 0, streams = [s1, s2, s3])

    start_ts = time.time()
    c.start(ports = 0, mult = '1kpps')

    c.wait_on_traffic(ports = 0)
    stop_ts = time.time()

    print('TX time measured: {0}'.format(stop_ts - start_ts))

    stats = c.get_stats()
    print('total output packets: {}'.format(stats[0]['opackets']))
except STLError as e:
    print(e)

finally:
    c.disconnect()