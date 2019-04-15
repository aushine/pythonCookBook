from collections import deque
if __name__ == "__main__":

    p = (4, 5)
    x, y = p
    print(x, y)
    data = ['ACME', 50, 91.9, (2123, 12, 32)]
    data = ["acme", 50, 91.1, (2012, 12, 22)]
    #解构一个可迭代的对象
    name, shares, price, (year, mon, day) = data
    print(name, shares, price, year)
    #使用下划线对一个值进行占位
    name, shares, price, _ = data
    print(name, shares, price, year)
    #所有可迭代的对象都可以被解构
    s = "Sakura"
    a, b, c, d, e, f = s
    print(a, b, c, d, e, f)
    '''
    当一个可迭代对象的元素个数超过变量的个数,
    将会抛出一个ValueError
    '''
    record = ("Sakura", "www.honkai@3rd.com", "9123-15551", "145611234")
    #使用*来收集解构出来的多个元素
    name, email, *phonenum = record
    print(phonenum)
    #此处,首位和末位被指定接收,中间被收集接收
    score = [100, 88, 54, 65, 57]
    hign, *middle, lower = score
    print(middle)
    *trailling, current = [10, 8, 7, 1, 9, 10, 3]
    print(trailling)

    records = [
        ('foo', 1, 2),
        ("bar", "hello"),
        ("foo", 3, 4)
    ]
    def do_foo(x, y):
        print("foo", x, y)
    def do_bar(s):
        print("bar", s)
    for tag, *args in records:
        if tag == "foo":
            do_foo(*args)#解构成收集参数传给do_foo
        elif tag == "bar":
            do_bar(*args)

    line = 'nobody:*:-2-2:Unprivileged User:/var/empty:/usr/in/false'
    uname, *fields, homedir, sh = line.split(":")
    print(uname, fields, homedir, sh)

    record = ("Acme", 98, 112, (12, 12, 9102))
    name, *_, (*_, year) = record
    print(name, year)

    items = [1, 23, 5, 1, 55, 11]
    head, *tail = items
    print(head, "->", tail)
    if head:
        print("Because I am batman")
    def sum(items):
        head, *tail = items
        return head + sum(tail) if tail else head
    print(sum(items))

    def search(lines, patteern, history=8):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if patteern in line:
                yield line, previous_lines
            previous_lines.append(line)



    def countdown(n):
        print("starting to count from", n)
        while n > 0:
            yield n
            n -= 1
        print("boom")
    w = countdown(4)
    print(next(w))
    print(next(w))
    print(next(w))
    print(next(w))
    print(next(w))
