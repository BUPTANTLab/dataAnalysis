#!/usr/bin/env python

import os
import os.path

def s(filename, m):
	with open(filename) as f:
		print filename
		all = f.readlines()
		last = ''
		for str in all:
			ss = str.split('\t')
			if last != '' and last != ss[2]:
				if m.has_key(last + '\t' + ss[2]):
					m[last + '\t' + ss[2]] += 1
				else:
					m[last + '\t' + ss[2]] = 1
				if not m.has_key(ss[2] + '\t' + last):
					m[ss[2] + '\t' + last] = 0
			last = ss[2]

if __name__ == '__main__':
	rootdir = '../tmp/'
	m = {}
	applist = []
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			if filename.find('sort') != -1:
			#	print os.path.join(parent,filename)
				s(os.path.join(parent,filename), m)
	with open('result', 'w') as w:
		for key in m.keys(): 
#			applist.append(key.split('\t')[0])
#			applist.append(key.split('\t')[1])
#			k2 = key.split('\t')[1] + '\t' + key.split('\t')[0]
#			if m[key] > 0 and m[k2] > 0:
			if m[key] > 0:
				applist.append(key.split('\t')[0])
				applist.append(key.split('\t')[1])
				w.write(key + '\t' + str(m[key]) + '\r\n')
	print len({}.fromkeys(applist).keys())
