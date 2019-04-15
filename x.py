from functools import reduce
print(reduce(lambda x, y: x*y, range(1, 6)))

def ride(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
print(ride(5))