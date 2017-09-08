digpow = []

for x in xrange(2,1000000):
	print(x)
	digit = list(str(x))

	tot = 0
	for y in digit:
		tot = tot + int(y)**5

	if (tot == x):
		digpow.append(x)

print(sum(digpow))