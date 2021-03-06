import time

start_time = time.time()

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = range(np1)
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)

primes = set(sieve(2000000))

result = 0
for n in primes:
    result += n

print result

end_time = time.time()
print "Elapsed time was %g seconds" % (end_time - start_time)
