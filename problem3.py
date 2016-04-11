def findMaxFactor(n):
    print n
    if n <= 3: return n
    if n % 2 == 0:
        return findMaxFactor(n/2)
    if n % 3 == 0:
        return findMaxFactor(n/3)
    return n

print findMaxFactor(215127)
