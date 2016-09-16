#!/usr/bin/env python 

import socket,traceback

host = ''
port =51424

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while 1:
	try:
		clientsock,clientaddr = s.accept()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	try:
		print "Got connection from :",clientsock.getpeername()
		while 1:
			data = clientsock.recv(4096)
		if not len(data):
			break
		clientsock.sendall(data)
	except(KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()
	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()	