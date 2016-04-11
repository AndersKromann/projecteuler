def findMaxFactor(n):
    factors = {}
    d = n -1
    while d > 1:
        if n % d == 0:
            factors.append(d)
        d /= 2
    return factors

print max(findMaxFactor(204))
