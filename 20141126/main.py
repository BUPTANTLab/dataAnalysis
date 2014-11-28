#!/usr/bin/env python

def bigAna():
	applist = []
	with open('lastAppResult') as f:
		all = f.readlines()
		for ss in all:
			m = ss.split('\t')
			applist.append(m[1])
	applist = {}.fromkeys(applist).keys()
	print "App Num:", len(applist)

	t1 = {}
	
	t2 = {}
	t3 = {}
	t4 = {}
	t5 = {}
	t6 = {}
	

def timeTop():
	with open('timeWeekend') as f:
                all = f.readlines()
		ha = {}
                for ss in all:
                        m = ss.split('\t')
                        if ha.has_key(m[0]):
                                ha[m[0]] += int(m[2])
                        else:
                                ha[m[0]] = int(m[2])
		print sorted(ha.items(), key=lambda d: d[1]) 

def timeH():
	with open('timeWeekend') as f:
		all = f.readlines()
		ha = {}
		for ss in all:
			m = ss.split('\t')
			if ha.has_key(m[1]):
				if ha[m[1] + 'time'] < int(m[2]):
					ha[m[1]] = m[0]
					ha[m[1] + 'time'] = int(m[2])
			else:
				ha[m[1]] = m[0]
				ha[m[1] + 'time'] = int(m[2])
		print ha

if __name__ == '__main__':
	cata = {'1':timeH, '2':timeTop, '3':bigAna}
	print cata
	x = raw_input()
	cata.get(x)()
