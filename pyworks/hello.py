#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;
import calendar


print dir()
ticks = time.time()
print calendar.month(2016,9)
localtime = time.localtime(ticks)

astime = time.asctime(localtime)
print range(2,10,2)
print astime
print localtime
print "Now is :",localtime
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# str = 'Hello World!'
# data = [1,2,3,4,5,6,7,8,9,10]

# for i in data:
# 	print "number :", data[i-1]

# for i in str:
# 	print "output :",i


# print str

# print str[1:3]
# print str[0:]
# print str[0:6]

# list1 =  ['asdf','234','john',17]
# print list1
# var1 = 1 
# var2 = 2 
# var3 = 3

# if var3 == 0:
# 	print "var3 is 0"
# else:
# 	print "var3 is not 0"
# dict = {}
# print var1 is var2
# dict['111'] = "what's this?"
# print dict
# print dict['111']


# print var1,var2,var3
# print complex(var1,var2)
# del var1,var2
# # raw_input("\n\nPress the enter key to exit")

for i in range(3,100):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print i,"is a prime number"

print r"sdfsd\n\n\tfsdfasdfasd"