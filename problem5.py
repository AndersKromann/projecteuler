def isDivisible(num):
    for i in range(1,20):
        if num % i != 0:
            return False
    return True

for i in range(1,100000000):
    if isDivisible(i):
        print i
