tot = 1000

for a in xrange(tot/3):
	for b in xrange(a+1,tot):
		c = tot - a - b
		if ((a**2 + b ** 2) == c**2):
			print(a,b,c)
			print(a*b*c)