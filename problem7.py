primes = [2, 3, 5, 7, 11, 13]

count = 14

while len(primes) < 10001:
    #append next prime
    prime = 0
    for i in range(len(primes)):
        if count % primes[i] == 0:
            prime = 0
            break
        else:
            prime = count
    if prime != 0:
        primes.append(prime)

    count += 1

print primes[10000]
