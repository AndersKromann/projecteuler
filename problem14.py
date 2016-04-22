import time

start_time = time.time()

def collatz(n):
    if n == 1: return 1
    if n % 2 == 0: return n / 2
    else: return 3*n + 1

def collatzChain(n):
    count = 1
    while n != 1:
        n = collatz(n)
        count += 1
    return count

longestChain = 0
longestChainProducer = 0

for i in range(1, 1000000):
    chainLength = collatzChain(i)
    if chainLength > longestChain:
        longestChain = chainLength
        longestChainProducer = i

print longestChain
print longestChainProducer

end_time = time.time()
print "Elapsed time was %g seconds" % (end_time - start_time)
