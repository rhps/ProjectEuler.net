def factorial(num):
	sumasi = 1
	for x in xrange(1, num+1):
		sumasi = sumasi * x

	return sumasi

fact = factorial(100)
fact = list(str(fact))

sumasi = 0
for x in fact:
	sumasi = sumasi + int(x)

print(sumasi)