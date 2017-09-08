sum = 0
for x in xrange(1,1000):
	if (x%3  == 0) :
		sum = sum + x
	elif (x%5 == 0) :
		sum = sum + x

print(sum)