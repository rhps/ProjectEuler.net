def pandigital(n, s=9):
	n=str(n)
	return len(n)==s and not '1234567890'[:s].strip(n)

p = set()
for i in xrange(2,60):
	if i < 10:
		start = 1234
	else:
		start = 123

	for j in xrange(start,10000//i):
		if pandigital(str(i)+str(j)+str(i*j)):
			p.add(i*j)

print(sum(p))