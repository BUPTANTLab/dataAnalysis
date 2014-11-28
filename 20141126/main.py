#!/usr/bin/env python

import random
import os
import os.path
import time
import math

def s(filename, m):
	with open(filename) as f:
		all = f.readlines()
		last = ''
		for sstr in all:
			ss = sstr.split('\t')
			if last != ss[2]:
				m.append(sstr)
				last = ss[2]

def bigAna():
	applist = []
	t1 = {}
	with open('lastAppResult') as f:
		all = f.readlines()
		for ss in all:
			m = ss.split('\t')
			applist.append(m[1])
			t1[m[0] + "\t" + m[1]] = int(m[2])
	applist = {}.fromkeys(applist).keys()
	print "App Num:", len(applist)
	print "lastApp:", len(t1.keys())

	t2 = {}
	with open('cellIDResult') as f:
                all = f.readlines()
                for ss in all:
                        m = ss.split('\t')
			t2[m[0] + "\t" + m[1]] = int(m[2])
	print "cellID:", len(t2.keys())

	t3 = {}
	with open('timeWeekdays') as f:
                all = f.readlines()
                for ss in all:
                        m = ss.split('\t')
                        t3[m[0] + "\t" + m[1]] = int(m[2])
        print "Weekdays:", len(t3.keys())

	t4 = {}
	with open('timeWeekend') as f:
                all = f.readlines()
                for ss in all:
                        m = ss.split('\t')
                        t4[m[0] + "\t" + m[1]] = int(m[2])
        print "Weekend:", len(t4.keys())

	t5 = {}
	with open('networkResult') as f:
                all = f.readlines()
                for ss in all:
                        m = ss.split('\t')
                        t5[m[0] + "\t" + m[1]] = int(m[2])
        print "network:", len(t5.keys())

	t6 = {}
	with open('avgDownSpeedResult') as f:
                all = f.readlines()
                for ss in all:
                        m = ss.split('\t')
                        t6[m[0] + "\t" + m[1]] = int(m[2])
        print "avgDownSpeed:", len(t6.keys())	

	all = []
	with open('demo1') as f:
		for parent,dirnames,filenames in os.walk("tmp/"):
			for filename in filenames:
				if filename.find('sort') != -1:
					s(os.path.join(parent,filename), all)
	print "record:", len(all)

	rnum = {}
	while len(rnum.keys()) < 1000:
		rnum[random.randint(1, len(all))] = 1
	rnum = rnum.keys()
	print "randomNum:", len(rnum)

	hit = [0,0,0,0,0]
	id = 0
	for ri in rnum:
		id += 1
		last = all[ri - 1]
		current = all[ri]
		m = current.split("\t")
		capp = m[2]
		lapp = last.split("\t")[2]
		ctime = m[1]
		cnet = m[3]
		ccell = m[4]
		cspeed = m[5]
		s5 = int( ctime ) / 1000
		s1 = time.strftime("%H",time.localtime(s5))
		s5 = int(time.strftime("%w",time.localtime(s5)))
		weekend = False
		if s5 <= 5 and s5 > 0:
			weekend = True
		re = {}
		ss5 = int( cspeed ) / 1000
		logspeed = '0'
		if ss5 > 0:
			logspeed = str( int( math.log10( ss5 ) + 1 ) )
#		print capp,lapp,ctime,cnet,ccell,cspeed
		for it in applist:
			if weekend:
				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 1 * t2[it+"\t"+ccell] if t2.has_key(it+"\t"+ccell) else 1 * t4[it+"\t"+s1] if t4.has_key(it+"\t"+s1) else 1 * t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 1 * t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 1
			else:
				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 1 * t2[it+"\t"+ccell] if t2.has_key(it+"\t"+ccell) else 1 * t3[it+"\t"+s1] if t3.has_key(it+"\t"+s1) else 1 * t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 1 * t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 1
#			print re[it]
		re = sorted(re.items(), key=lambda d: d[1])
#		print "result:", len(re)
		hhit = False
		for i in range(0,5):
			if hhit:
				hit[i] += 1
				continue
			if capp == re[len(re) -  1 - i][0]:
				hit[i] += 1
				hhit = True
		print id, hit

def timeTop():
	with open('timeWeekdays') as f:
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
