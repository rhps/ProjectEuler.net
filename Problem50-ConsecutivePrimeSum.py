prime = []
prime.append(2)
n = 3

while (n < 1000000): 
	if (all((n%x != 0 for x in prime))):
		prime.append(n)
		print(n)
	n = n + 1

sums = 0
for x in prime:
	sums = sums + x
	if (sums == y for y in prime):
		print(x)