#!/usr/bin/env python

import os
import os.path

def s(filename):
	with open(filename) as f:
		all = f.readlines()
		l = []
		for str in all:
			l.append(str)
		l.sort()
		with open(filename + '.sort', 'w') as fs:
			for str in l:
				fs.write(str)
			

if __name__ == '__main__':
	rootdir = 'tmp/'
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
#			print os.path.join(parent,filename)
			s(os.path.join(parent,filename))
