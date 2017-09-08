def cycle(num):
	start = 10
	i = 0

	while ((start != 10) or (i < 1)):
		start = (start%num) * 10
		i += 1
		print start,
	return i

print(cycle(7))
"""
longest = 0
for i in xrange(2,1000):
	if ((i%2 != 0) and (i%5 != 0)):
		length = cycle(i)
		if length > longest:
			longest = length
			result = i

print(result)
"""