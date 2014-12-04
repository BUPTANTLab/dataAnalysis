#!/usr/bin/env python

def fenlei():
	with open ('output') as f:
		all = f.readlines()
		re = {}
		for ss in all:
			m = ss.split(' ')
			re[m[0]] = set([])
			for app in m[1:]:
				re[m[0]].add(app)
		name = re.keys()
		print len(name)
		output = ''
		for i in range(0, len(name)):
			for j in range(i+1, len(name)):
				print i,j
				output += name[i] + '\t' + name[j] + '\t' + str((len(re[name[i]] & re[name[j]]) + 0.0) / (len(re[name[i]] | re[name[j]]))) + '\r\n'
		with open('lens', 'w') as w:
			w.write(output)
			
if __name__ == '__main__':
	cata = {'1':fenlei}
	try:
		while True:
			print cata
			x = raw_input()
			cata.get(x)()
	except KeyboardInterrupt:
		exit(0)
