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
 
def new_rotation(y, n):
    c = 0
    while n != c:
        j = y[1:]
        r = y[0]
        j.append(r)
        s = ''.join(j)
        c = int(s)
        if isprime(c):
            pass
        else:
            return "False"
        y = list(str(s))
    return "True"
 
def main():
    L = []
    for n in range(10, 1000000):
        if isprime(n):
            y = list(str(n))
            if new_rotation(y, n) == "True":
                L.append(n)
            else:
                continue
    print "len(L) = ", len(L) + 4
    print L
             
if __name__ == '__main__':
    main()