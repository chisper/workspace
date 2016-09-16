#!/usr/bin/env python 

import socket,sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send('GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnect:close\r\n\r\n')

buf = []
while 1:
	d = s.recv(1024)
	if d:
		buf.append(d)
	else:
		break
	data = ''.join(buf)

header,html = data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
	f.write(html)