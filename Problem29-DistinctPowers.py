n = 100
distpow = []
for x in xrange(2,n+1):
	for y in xrange(2,n+1):
		dist = x**y
		if (dist != z for z in distpow):
			distpow.append(dist)

distpow.sort()
s = [x for i, x in enumerate(distpow) if i == distpow.index(x)]
print(s)
print(len(s))