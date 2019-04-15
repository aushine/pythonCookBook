from collections import deque
from sys import stdout
def out(Any):
    return stdout.write(Any)
def search(lines, pattern,history=3):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if "python\n" == line:
            yield line,previous_lines
        previous_lines.append(line)
def frange(start, stop, increment):
    x = start
    while x<stop:
        yield x
        x += increment
def countdown(n):
    print("starting to count from", n)
    while n>0:
        yield n
        n -= 1
    print("done!")
if __name__ == "__main__":
    with open(r"some.txt") as f:
        for line,prevlines in search(f, "python", 4):
            for pline in list(prevlines):
                print(pline, end="")
            #print(line, end='X')
            print("-" * 20)
    out("countdown()方法生成的类型是:")
    out(str(type(countdown(5))))
    print("一个生成器:generator")
    print(list(frange(0, 1, 0.125)))

    for n in frange(0, 4, 0.5):
        print(n)

