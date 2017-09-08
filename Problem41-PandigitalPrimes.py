def ispandigital(n, s=9):
	n=str(n)
	return len(n)==s and not '1234567890'[:s].strip(n)


prime = []
prime.append(2)
n = 2
while (n < 987654321): 
	if (all((n%x != 0 for x in prime))):
		prime.append(n)
		if ispandigital(n, 7):
			print(n)
	n = n + 1
