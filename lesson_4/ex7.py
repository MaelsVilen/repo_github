def fact(n):
    j = 1
    for i in range(1, n + 1):
        j *= i
        yield j

for el in fact(9):
    print(el)
