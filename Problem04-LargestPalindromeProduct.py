def ispalindrom(num):
	return str(num) == str(num)[::-1]

greatest = 0
for x in xrange(100,999):
	for y in xrange(100,999):
		hasil = x * y
		if ispalindrom(hasil):
			if greatest < hasil:
				greatest = hasil

print(greatest)