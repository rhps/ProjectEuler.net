prime = []
prime.append(2)
n = 3
while (len(prime) < 10001): 
	if (all((n%x != 0 for x in prime))):
		prime.append(n)
		print(n)
	n = n + 1

print(prime)