#!/usr/bin/env python

import random
import os
import os.path
import time
import math

filter = {'com.tencent.mobileqq':1, 'com.tencent.mm':2, 'com.tencent.qqlive':3, 'com.taobao.taobao':4}

def s(filename, m):
	with open(filename) as f:
		all = f.readlines()
		last = ''
		for sstr in all:
			ss = sstr.split('\t')
			if filter.has_key(ss[2]):
				continue
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
			if not filter.has_key(m[1]):
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
		ri = random.randint(1, len(all))
		rnum[ri] = 1
	rnum = rnum.keys()
	print "randomNum:", len(rnum)

	max1 = max(t1.values())
        max2 = max(t2.values())
        max3 = max(t3.values())
        max4 = max(t4.values())
        max5 = max(t5.values())
        max6 = max(t6.values())
	print max1,max2,max3,max4,max5,max6

	hit = [0,0,0,0,0]
	id = 0
	capplist = []
	for ri in rnum:
		id += 1
		last = all[ri - 1]
		current = all[ri]
		m = current.split("\t")
		capp = m[2]
		capplist.append(capp)
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
#				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 1 * t2[it+"\t"+ccell] if t2.has_key(it+"\t"+ccell) else 1 * t4[it+"\t"+s1] if t4.has_key(it+"\t"+s1) else 1 * t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 1 * t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 1
#				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 1 * t4[it+"\t"+s1] if t4.has_key(it+"\t"+s1) else 1 * t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 1 * t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 1
#				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 0 + t2[it+"\t"+ccell] if t2.has_key(it+"\t"+ccell) else 0 + t4[it+"\t"+s1] if t4.has_key(it+"\t"+s1) else 0 + t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 0 + t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 0
				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 0
#				re[it] = t4[it+"\t"+s1] if t4.has_key(it+"\t"+s1) else 0
#				re[it] = t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 0
			else:
#				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 1 * t2[it+"\t"+ccell] if t2.has_key(it+"\t"+ccell) else 1 * t3[it+"\t"+s1] if t3.has_key(it+"\t"+s1) else 1 * t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 1 * t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 1
#				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 1 * t3[it+"\t"+s1] if t3.has_key(it+"\t"+s1) else 1 * t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 1 * t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 1
#				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 0 + t2[it+"\t"+ccell] if t2.has_key(it+"\t"+ccell) else 0 + t3[it+"\t"+s1] if t3.has_key(it+"\t"+s1) else 0 + t5[it+"\t"+cnet] if t5.has_key(it+"\t"+cnet) else 0 + t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 0
				re[it] = t1[lapp+"\t"+it] if t1.has_key(lapp+"\t"+it) else 0
#				re[it] = t3[it+"\t"+s1] if t3.has_key(it+"\t"+s1) else 0
#				re[it] = t6[it+"\t"+logspeed] if t6.has_key(it+"\t"+logspeed) else 0
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
		print id, hit# , capp, re[-5:]
	print len({}.fromkeys(capplist).keys())

def speedTop():
        with open('avgDownSpeedResult') as f:
                all = f.readlines()
                ha = {}
                for ss in all:
                        m = ss.split('\t')
			if not ha.has_key(m[1]):
				ha[m[1]] = {}
                        if ha[m[1]].has_key(m[0]):
                                ha[m[1]][m[0]] += int(m[2])
                        else:
                                ha[m[1]][m[0]] = int(m[2])
		for h in ha.keys():
			print h, sorted(ha[h].items(), key=lambda d: d[1])[-10:]

def networkTop():
        with open('networkResult') as f:
                all = f.readlines()
                haw = {}
                ham = {}
                for ss in all:
                        m = ss.split('\t')
			ha = {}
			if m[1] == 'mobile':
				ha = ham
			else:
				ha = haw
                        if ha.has_key(m[0]):
                                ha[m[0]] += int(m[2])
                        else:
                                ha[m[0]] = int(m[2])
                print "mobile", sorted(ham.items(), key=lambda d: d[1])[-10:]
                print "wifi", sorted(haw.items(), key=lambda d: d[1])[-10:]

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
		print sorted(ha.items(), key=lambda d: d[1])[-10:]

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
	cata = {'1':timeH, '2':timeTop, '3':bigAna, '4':networkTop, '5':speedTop}
	print cata
	try:
		while True:
			x = raw_input()
			cata.get(x)()
	except KeyboardInterrupt:
		exit(0)
