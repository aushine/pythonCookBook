from collections import deque
def search(lines, pattern,history=3):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)
def frange(start, stop, increment):
    x = start
    while x<stop:
        yield x
        x += increment
    print(list(frange(0, 1, 0.125)))
if __name__ == "__main__":
    for n in frange(0, 4, 0.5):
        print(n)
    with open(r"some.txt") as f:
        for line,prevlines in search(f, "python", 1):
            for pline in prevlines:
                print(pline, end="")
            print(line, end='')
            print("-" * 20)
