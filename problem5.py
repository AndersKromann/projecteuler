def isDivisible(num):
    for i in range(20, 1, -1):
        if num % i != 0:
            return False
    return True

for i in range(1,50000000):
    if isDivisible(i * 20):
        print i * 20
