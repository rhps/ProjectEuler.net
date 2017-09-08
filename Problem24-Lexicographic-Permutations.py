import itertools
permutations = []

a = list('0123456789')
k = len(a)
tot = 0
for c in itertools.combinations(a,k):
	for p in itertools.permutations(c):
		perm = "".join(p)
		print perm,
		permutations.append(perm)

permutations.sort()
print(permutations[1000000-1])