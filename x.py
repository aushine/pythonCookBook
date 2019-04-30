import urllib.request
import sys
import re
from importlib import reload

reload(sys)


def out(any):
    return sys.stdout.write(any)


def main():
    url_text = urllib.request.urlopen("https://search.bilibili.com/photo?keyword=%E5%85%AB%E9%87%8D%E6%A8%B1")
    url_content = url_text.read()
    print(url_content)


if __name__ == "__main__":
    main()
