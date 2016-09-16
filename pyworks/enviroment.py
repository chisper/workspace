#!/usr/bin/env python 

import sys,socket

def getipaddr(hostname):
	result = socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
	return [x[4][0] for x in result]
	hostname = socket.gethostname()
	print "hostname :",hostname

	print "Fully-qualified name:",socket.getfqdn(hostname)
	try:
		print "IP address :",",".join(getipaddr(hostname))
	except socket.gaierror, e:
		print "Couldn't get IP addresses:",e
	