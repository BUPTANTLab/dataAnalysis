#!/usr/bin/env python

if __name__ == '__main__':
        f = open('demo1')
        all = f.readlines()
        f.close()
        try:
		fname = ''
		for re in all:
			lre = re.split('\t')
			if lre[0] != fname:
				if fname != '':
					print 'close' + fname
					f.close()
				fname = lre[0]
				print 'open' + fname
				f = open('tmp/' + fname, 'w+')
			f.write(re)
	except KeyboardInterrupt:
            print 'over!'
        exit(0)
