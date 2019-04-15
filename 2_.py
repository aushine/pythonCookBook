from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        yield line, previous_lines
    previous_lines.append(line)
if __name__ == "__main__":
    with open(r"some.txt", encoding="utf-8") as f:
        for line, prevlines in search(f, "python", 3):
            for pline in prevlines:
                print(pline, end="")
        print(line, end="")
        print('-' * 20)
