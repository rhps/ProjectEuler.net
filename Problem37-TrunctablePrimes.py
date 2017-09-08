def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def trunctleft(num):
	x = list(str(num))
	for n in xrange(1,len(x)):
		y = x [n:]
		s = int(''.join(y))
		if isprime(s):
			continue
		else:
			return False
	return True

def trunctright(num):
	x = list(str(num))
	for n in xrange(1,len(x)):
		y = x [:-n]
		s = int(''.join(y))
		if isprime(s):
			continue
		else:
			return False
	return True

trunctablePrime = []
for i in xrange(10,1000000):
	if isprime(i):
		if (trunctleft(i) == True) and (trunctright(i) == True):
			trunctablePrime.append(i)
			print(i)
		else:
			continue
	else:
		continue

print sum(trunctablePrime)