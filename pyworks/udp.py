#!/usr/bin/env python 
 
import sys,socket

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

port = 51423
# try:
# 	port = int(textport)
# except ValueError:
# 	port = socket.getservbyname(text,"udp")

s.connect((host,port))
print "Enter data to transmit:"
data = sys.stdin.readline().strip()
s.sendall(data)
print "Looking for replies;press Ctrl-C or Ctrl-Break to stop"
while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)