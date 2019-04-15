from collections import deque
def count(n):
    b = 1
    res = []
    while n != 0:
        yield n, b
        n -= 1
        b += 1
        if True:
            pass

def test():
    n = 0
    while True:
        if n != 1:
            yield n
        n += 1
def search(list):
    a = deque(maxlen=3)
    for i in list:
        yield i, a
    a.append(i)
a = search([1, 2, 3, 4, 5, 6])
for i, j in a:
    for each in j:
        print(each)
for i in range(5):
    print(i)

print(count(2))
for i, j in count(5):
    print(i, "===>", j)

