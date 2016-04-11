fib_array = {}
def fib(n):
    if not n in fib_array:
        if n == 0: return 0
        elif n == 1: return 1
        else: fib_array[n] = fib(n-1)+fib(n-2)
    return fib_array[n]

result = 0
for i in range(1,1000):
    current = fib(i)
    print current
    if(current < 4000000 and current % 2 == 0):
        result += current

print result
