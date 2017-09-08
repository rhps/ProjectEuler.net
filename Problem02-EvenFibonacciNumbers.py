fib = 2
fib_i = 1
tot = 0

while fib < 4000000:
	if (fib%2 == 0):
		tot = tot + fib
	fib_tmp = fib_i + fib
	fib_i = fib
	fib = fib_tmp

print(tot)