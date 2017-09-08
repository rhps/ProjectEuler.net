def pandigital(n, s=9):
	n = str(n)
	return len(n)==s and not '1234567890'[:s].strip(n)

for x in xrange(9487,9213,-1):
	p = str(x*1) + str(x*2)
	if pandigital(p):
		print p