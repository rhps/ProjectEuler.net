sums = 0
for x in xrange(1,1001):
	sums = sums + x**x

words = str(sums)
print(words[-10:])