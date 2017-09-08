search = 200
cointsize = [1,2,5,10,20,50,100,200]
matrix = {}

for y in xrange(0,search+1):
	matrix[y,0] = 1

for y in xrange(0,search+1):
	print y, ":", 1,
	for x in xrange(1,len(cointsize)):
		matrix[y,x] = 0
		if y >= cointsize[x]:
			matrix[y, x] += matrix[y, x-1]
			matrix[y, x] += matrix[y-cointsize[x], x]
		else:
			matrix[y, x] = matrix[y, x-1]
		print matrix[y,x],
	print