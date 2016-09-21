#!/usr/bin/env python

import sys,math,random

global j=0
n = range(1,100000)
for i in n:
	x = random.uniform(-10,10)
	y = random.uniform(-10,10)
	dist = x*x+y*y
	if dist<100 :
		j = j + 1
print j/100000*4

