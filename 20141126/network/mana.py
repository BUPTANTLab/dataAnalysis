#!/usr/bin/env python

import os
import os.path

def s(filename, m):
	with open(filename) as f:
		print filename
		all = f.readlines()
		for str in all:
			ss = str.split('\t')
			if m.has_key(ss[2] + '\t' + ss[3]):
				m[ss[2] + '\t' + ss[3]] += 1
			else:
				m[ss[2] + '\t' + ss[3]] = 1

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
			if m[key] > 0:
				w.write(key + '\t' + str(m[key]) + '\r\n')
