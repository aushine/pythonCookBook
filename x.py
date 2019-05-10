import itertools
"""
def a():
    x = 1
    while True:
        yield x
        print("aaaaa")
        x += 1
print(type(a()))
def b():
    for i in range(10):
        yield i
it = b()"""
li = [1, 2, 3]


def yield_test():
    pass


def permutation(li):
    print(list(itertools.permutations(li)))
permutation(li)