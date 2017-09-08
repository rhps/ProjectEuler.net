def collatz(num):
	seq = []
	seq.append(num)
	while (num > 1):
		if (num%2 == 0):
			num = num/2
		else:
			num = (num*3)+1

		seq.append(num)

	return len(seq)

greatest = 0
starting = 0
for x in xrange(2,1000000):
	contains = collatz(x)
	if contains > greatest:
		greatest = contains
		starting = x

	if (x%1000 == 0):
		print(greatest)
print(starting)
