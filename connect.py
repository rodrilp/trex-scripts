# get TRex APIs
from trex_stl_lib.api import *

# connect to the server
c = STLClient(server = '127.0.0.1')

try:
    # connect to the server
    c.connect()

    # fetch the TRex server version
    ver = c.get_server_version()

    print(ver)

except STLError as e:
    print(e)

finally:
    c.disconnect()