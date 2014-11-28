#!/usr/bin/env python

import os
import os.path
import math

def s(filename, m):
	with open(filename) as f:
		print filename
		all = f.readlines()
		for sstr in all:
			ss = sstr.split('\t')
			s5 = int( ss[5] ) / 1000
			logspeed = '0'
			if s5 > 0:
				logspeed = str( int( math.log10( s5 ) + 1 ) )
			if m.has_key(ss[2] + '\t' + logspeed):
				m[ss[2] + '\t' + logspeed] += 1
			else:
				m[ss[2] + '\t' + logspeed] = 1

if __name__ == '__main__':
	rootdir = '../tmp/'
	m = {}
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			if filename.find('sort') != -1:
			#	print os.path.join(parent,filename)
				s(os.path.join(parent,filename), m)
	with open('result', 'w') as w:
		for key in m.keys(): 
			w.write(key + '\t' + str(m[key]) + '\r\n')
