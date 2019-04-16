from sys import stdout
import heapq
from collections import defaultdict
def out(Any):

    return stdout.write(Any)

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        #往堆中推入一个元组,heap会先按照优先级进行排序,优先级相同时
        #就会按照索引值进行排序
        #使用heap模块可以保证推入的元素就是排序好的
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Item('{self.name}')"

if __name__ == "__main__":
    #寻找两个字典中的相同点(相同的键,相同的值等)
    a ={
        'x': 1,
        'y': 2,
        'z': 3
    }
    b ={
        'w': 10,
        'x': 11,
        'y': 2
    }


    #比对一个字典的值,对字典的值进行比对的同时将进行排序,
    prices = {
        "ACME": 45.23,
        "AAPL": 612.78,
        "IBM": 205.55,
        "TENCENT": 150,
        "FB": 10.75
    }
    min_value = prices[min(prices, key=lambda k:prices[k])]
    print(min(zip(prices.values(), prices.keys())))
    print(max(zip(prices.values(), prices.keys())))
    print(sorted(zip(prices.values(), prices.keys())))

    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    print(f"max price:{max_price}")
    print(f"min price:{min_price}")

    prices_and_names = zip(prices.values(), prices.keys())
    print("prices the maxValue:", max(prices_and_names))
    #zip函数创建的是只能访问一次的迭代器,进行过一次迭代就销毁
    #print("prices the maxValue:", min(prices_and_names))
    d = {
        'a': [1, 2, 3],
        'b': [4, 5]
    }
    e = {
        'a': {1, 2, 3},
        'b': {4, 5}
    }
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(3)
    print(d)
    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    print(dict(d))
    d = {}
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)
    print(dict(d))

    d = defaultdict(list)
    pairs = ['a', 'b', 'c']
    for key in pairs:
        d[key].append(pairs.index(key))
    print(dict(d))
    #Item(bar)Item(spam)Item(foo)Item(grok)
    #Item('bar')Item('spam')Item('foo')Item('grok')
    #Item('bar')Item('spam')Item('foo')Item('grok')
    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 5)
    q.push(Item("spam"), 4)
    q.push(Item("grok"), 1)
    out(str(q.pop()))
    out(str(q.pop()))
    out(str(q.pop()))
    out(str(q.pop()))
