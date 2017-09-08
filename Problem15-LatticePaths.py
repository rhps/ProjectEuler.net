def lattice(down, right):
	if ((down == 0) or (right == 0)):
		return 1
	else:
		print '.',
		return lattice(down -1, right) + lattice(down, right-1)


print(lattice(20,20))