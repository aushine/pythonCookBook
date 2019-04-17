from sys import stdout
from collections import Counter

def out(Any):
    return stdout.write(Any)
def main():
    words = [
        'hell', 'into', 'my', 'eyes', 'look', 'fucking', 'crazy', 'what',
        'love', 'eyes', 'hell', 'design', 'see', 'look', 'crazy', 'hell',
        'to', 'die', 'eyes', 'look', 'hell', 'see'
    ]
    words_counts = Counter(words)
    top_3 = words_counts.most_common(3)
    print(words.count("eyes"))
    print("出现次数最多的三个单词是", top_3)  # 输出了字符列表中出现次数最多的三个单词
    more_words = ["why", "are", "u", "not", "see", "my", "eyes"]
    '''
    for word in more_words:
        words_counts[word] += 1
    print(words_counts["are"])
    '''
    words_counts.update(more_words)
    print("更新后eyes出现的次数:", words_counts["eyes"])

    a = Counter(words)
    b = Counter(more_words)
    print("a 的counter:", a)
    print("b 的counter:", b)
    c = a + b
    print("a对b取并c:", c)
    d = a - b
    print("a对b取差d:", d)

    record = ('.'*20)+"100"+("."*7)+"513.25"
    print(record)

    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 8, 2)
    print(a.indices(4))
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))
    b = [{'x': 1, 'y': 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]

    print(list(dedupe(b, lambda d: (d['x'], d['y']))))
    print(list(itertest()))
'''
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
 '''

def dedupe(items, key=None):
    '''
    如果接收到的items
    :param items:
    :param key:
    :return:
    '''
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
def itertest():
    n = 0
    while True:
        if n == 20:
            break
        if n % 2 == 0:
            yield n
        n += 1

if __name__ == "__main__":

    main()