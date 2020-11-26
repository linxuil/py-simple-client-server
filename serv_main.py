#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does."""

__author__      = "Barack Obama"
__copyright__   = "Copyright 2009, Planet Earth"

# @brief This is a simple Python script for start server on PC and echo RX data

import socket

# - - - - - - - - - - - - -
# - - - 1. Configure - - -
print('Start configure socket ...')

# 1.1. Set IP address
# Set IP this PC machine, four variants (A, B, C, D)
# (Select needed ip, if you needed say anything between)

#       A) Two programs on 1 PC
#               - Uncomment loopback addr
local_ip = '127.0.0.1'  # Standard loopback interface address (localhost)

#       B) Two programs on 2 another PC in local network
#               - Uncomment network addr, get this addr from linux command "ifconfig"
#                   if not virtualized, or general OS settings if we run script in
#                   virtualized OS.
# local_ip = '192.168.6.191'  # Local network

#       C) Two programs on 2 another PC in global WEB network
#               - Uncomment network addr
#               - Configure you router for send and route concrete port to you local IP
# local_ip = '192.168.6.191'  # Local network

#       D) If work without virtualisation -> can use automaticaly get IP
# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)
# print('\t Set hostname = ', hostname)

print('\t Set local_ip = ', local_ip)

# 1.2. Set port
port = 65432            # Port to listen on (non-privileged ports are > 1023)
print('\t Set port     = ', port)

# - - - - - - - - - - - - - - - - - -
# - - - 2. Start server socket - - -
print('Start socket program ...')

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP )
# bind the socket to a public host, and a well-known port
serversocket.bind((local_ip, port))

# - - - - - - - - - - - - - - - - - - -
# - - - 3. Become a server socket - - -
while True:
    print('Listen start ...')
    serversocket.listen(5)
    # listen() is blocking function, go to this line only if get new connection

    # - - - - - - - - - - - - - - - - - -
    # - - - 4. Processing new data - - -
    # When we listen new data from outside -> accept connections from outside
    (clientsocket, address) = serversocket.accept()
    print('Connected by (IP, port):', address)
    print('Client socket:', clientsocket)
    print('\t Try get data from current connected client ...')
    data = clientsocket.recv(1024)
    import sys
    print('\t Size data', sys.getsizeof(data))
    if (data == 0):
        # error -> socket not open
        print('\t Socket close or in close process')
    elif (sys.getsizeof(data) == 0 ):
        # ok -> get empty data
        print('\t Data empty')
    elif (sys.getsizeof(data) > 0 ):
        # ok -> get fill data
        print('\t We recv new data ...')
        print('\t \t Data size: ', data.__sizeof__())
        print('\t \t Data     : ', data)
    clientsocket.close()

        # clientsocket.sendall(data)