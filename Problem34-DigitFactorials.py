def fact(n):
	tot = 1
	for x in xrange(1,n+1):
		tot = tot * x
	return tot

digfact = []
for x in xrange(3,1000000):
	print(x)
	digit = list(str(x))

	tot = 0
	for y in digit:
		tot = tot + fact(int(y))

	if tot == x:
		digfact.append(x)

print(sum(digfact))