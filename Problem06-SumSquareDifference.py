n = 101
sums = 0
square = 0
for x in xrange(1,n):
	sums_i = x**2
	sums = sums + sums_i
	square = square + x

tot = (square**2)-sums
print(tot)