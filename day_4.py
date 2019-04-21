import heapq
import time
from collections import OrderedDict
from operator import itemgetter


def main():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_fname = sorted(rows, key=itemgetter("fname"))
    rows_by_uid = sorted(rows, key=itemgetter("uid"))
    print(rows_by_fname)
    print(rows_by_uid)
    dict1 = {"a": 1, "b": 2, "c": 3}
    zip1 = zip(dict1.values(), dict1.keys())
    print(sorted(zip1))
    '''
    因为字典是按照hash值进行存储,所以一般的字典是无序的
    :return:
    '''
    tes = dict()
    tes['a'] = "A"
    tes['b'] = "B"
    tes['c'] = "C"
    tes['d'] = "D"
    for key in tes:
        print(key, tes[key])
    # 字典的排序
    # OrderedDict()会生成一个字典,进行迭代和
    d = OrderedDict()
    d["foo"] = 2
    d["bar"] = 1
    d["spam"] = 3
    d["grok"] = 4
    # print([[x, d[x]] for x in d])
    for key in d:
        print(key, d[key])
    porfolio = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "APPLE", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 34, "price": 21.0},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    # 生成了一个堆集合,取出可迭代对象排序前3个元素
    cheap = heapq.nsmallest(3, porfolio, key=lambda x: x["price"])
    print(cheap)

    cheap_ = heapq.nlargest(3, porfolio, key=lambda x: x["price"])
    print(cheap_)

    # 将一个可迭代元素堆化,堆化后再往其中添加元素就是排序好的
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    heap.append(66)
    print(heap)

    # 使用列表生成式取出了列表中最小的三个元素
    smallest_3 = [heapq.heappop(heap) for i in range(3)]
    print(smallest_3)

    # pop 取出的元素是执行的pop操作
    print(heap)


if __name__ == "__main__":
    main()