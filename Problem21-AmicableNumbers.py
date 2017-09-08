def d(num):
	tot = 0
	for x in xrange(1,num/2+1):
		if (num%x == 0):
			tot = tot + x
	return tot

amicable = []
total = 0

for x in xrange(4,10000):
	if d(x) > 4:
		if (d(d(x)) == x) and (d(x) != x):
			total = total + x
			print x, "and", d(x)

print(total)			