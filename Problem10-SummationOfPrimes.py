prime = []
prime.append(2)
n = 3
sumprime = 2

while (n < 2000000): 
	if (all((n%x != 0 for x in prime))):
		prime.append(n)
		print(n)
		sumprime = sumprime + n
	n = n + 1
print(sumprime)