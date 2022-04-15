import socket
import sys
from datetime import datetime

# Server input
RHOST = input("Enter host to scan: ")
# remoteserverip = socket.gethostbyname(RHOST)

# Banner
print("Scanning: %s" % RHOST)

# Scan start time
time1 = datetime.now()

# Ports to scan

list = [
    20,
    21,
    22,
    23,
    25,
    53,
    80,
    110,
    111,
    135,
    139,
    143,
    443,
    445,
    993,
    995,
    1723,
    3306,
    3389,
    5900,
    8080,
]

length = len(list)

# Scanning top 20 ports

try:
    for port in range(length):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((RHOST, port))
        if result == 0:
            print("Port {}:   Open".format(list[port]))
        else:
            print("Port {}:   Closed".format(list[port]))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Check time after scan
time2 = datetime.now()

total = time2 - time1

# Scan completed
print("Scan completed in:", total)
