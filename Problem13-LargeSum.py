file = 'euler13.txt'

with open(file, "r") as ins:
	array = []
	for line in ins:
		array.append(int(line))

sumasi = sum(array)

print str(sumasi)[:10]