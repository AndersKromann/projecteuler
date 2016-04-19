palindromes = []

for i in range(100, 999):
    for j in range(100, 999):
        x = i * j
        z = str(x)
        if z == z[::-1]:
            palindromes.append(x)

print max(palindromes)
