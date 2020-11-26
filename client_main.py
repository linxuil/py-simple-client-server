# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#!/usr/bin/env python3

import socket	#for sockets
import sys	    #for exit


print('Config owr data...')
SEND_HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
SEND_PORT = 54285        # Port to listen on (non-privileged ports are > 1023)
print('\t Set owr ip    = ', SEND_HOST)
print('\t Set owr port  = ', SEND_PORT)

print('Config connection data...')
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432                # Port to listen on (non-privileged ports are > 1023)
print('\t Set host ip   = ', HOST)
print('\t Set host port = ', PORT)

print('Try create socket...')
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as err:
    print ('Failed to create socket. Error code:')
    print (str(err[0]) , err[1])
    sys.exit(1) # Exit with error
else:
    print('\t OK: Create socket success')
    print('\t OK: Socket info:', s)
    print('\t OK: Socket fd:', s.fileno())

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(1)   # 5 seconds

# This str better not uncomment -> be error when we cloce connection and want connected second time -> get error
# s.bind((SEND_HOST, SEND_PORT))

print('Try connect ...')
try:
    s.connect((HOST, PORT))
except OSError as e:
    print('\t ERROR: Socket not connected to server, cause:')
    if(e.args[0] == 'timed out'):
        print('\t \t We have time out connection')
    else:
        print('\t \t We have unknown error')
        print('\t \t Object print error.args:', e.args)

    print('\t \t s:', s)
    s.shutdown(socket.SHUT_RDWR)
    print('\t \t s:', s)
    s.close()
    print('\t \t s:', s)
    s.fileno()
    print('\t \t s:', s)
    sys.exit(1) # Exit with error
else:
    print('\t OK: Connection success')

# If connection OK -> try send data to server
print('Try send data to server ...')
try:
    s.sendall(b'Hello, world')
except OSError as e:
    print('\t ERROR: Socket not connected to server, cause:')
    if(e.args[0] == 'timed out'):
        print('\t \t We have time out connection')
    else:
        print('\t \t We have unknown error')
        print('\t \t Object print error.args:', e.args)
    print('\t \t s:', s)
    s.shutdown(socket.SHUT_RDWR)
    print('\t \t s:', s)
    s.close()
    print('\t \t s:', s)
    s.fileno()
    print('\t \t s:', s)
    sys.exit(1) # Exit with error
else:
    print('\t OK: Data send success')

print('Close socket ...')
print('\t \t s:', s)
s.shutdown(socket.SHUT_RDWR)
print('\t \t s:', s)
s.close()
print('End program ...')
print('\t \t s:', s)
s.fileno()
print('\t \t s:', s)
sys.exit(1)  # Exit with error

# data = s.recv(1024)
# print('Received', repr(data))