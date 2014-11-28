#!/usr/bin/env python

import os
import os.path
import math
import time

def s(filename, m):
	with open(filename) as f:
		print filename
		all = f.readlines()
		last = ''
		for sstr in all:
			if last == sstr:
				continue
			last = sstr
			ss = sstr.split('\t')
			s5 = int( ss[1] ) / 1000
			s1 = time.strftime("%H",time.localtime(s5))
			s5 = int(time.strftime("%w",time.localtime(s5)))
			if s5 <= 5 and s5 > 0:
#			if s5 > 5 or s5 == 0:
				if m.has_key(ss[2] + '\t' + s1):
					m[ss[2] + '\t' + s1] += 1
				else:
					m[ss[2] + '\t' + s1] = 1

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
