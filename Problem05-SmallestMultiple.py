import sys

n = 20
div = [x for x in range(1,(n+1))]

for x in xrange(2520,sys.maxint,n):
	if(all(x%y == 0 for y in div)):
		print(x)

#http://pythoncentral.io/how-to-use-pythons-xrange-and-range/
#https://docs.python.org/2/library/functions.html