fib = []
fib.append(1)
fib.append(1)

n = 1
i = 2
while (n < 1000):
	bil = fib[i-1] + fib[i-2]
	fib.append(bil)
	n = len(str(bil))
	i = i + 1
	print(n)

print(len(fib))


