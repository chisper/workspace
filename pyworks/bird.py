#!/usr/bin/env python

import sys

class bird (object):
	def __init__(self,more_words):
		print "we aren't early birds.",more_words
	HasFeather = True
	WayOfReproduction = 'egg'
	def move(self,dx,dy):
		position = [0,0]
		position[0] = position[0] + dx
		position[1] = position[1] + dy
		return position
	def show(self):
		print self.HasFeather
		print self.WayOfReproduction
dog = bird('what?')
print dog.move(17,1)
dog.show()
print dir(bird)
print help(bird)