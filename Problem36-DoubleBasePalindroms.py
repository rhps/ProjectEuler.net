def binary(dec):
	base = ""
	while dec != 0:
		base = str(dec%2) + base
		dec //= 2
	return base

def ispalindrom(num):
	return str(num) == str(num)[::-1]

#print(ispalindrom(10))
#print(ispalindrom(binary(10)))

DoubleBasPal = []

for x in xrange(1,1000000):
	binum = binary(x)
	binPal = ispalindrom(binum)
	decPal = ispalindrom(x)
	if ((binPal == True) and (decPal == True)):
		DoubleBasPal.append(x)
		print(x)

print(sum(DoubleBasPal))