sumOfTriple = 0

m = 1
n = 1

while sumOfTriple != 1000 and sumOfTriple < 10000:
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n *n
    sumOfTriple = a + b + c
    print "a = %s, b = %s, c = %s, sum = %s" % (a,b,c,sumOfTriple)
    m += 6
    n += 6
