import time
import urllib.request
import os
import gevent
from gevent import monkey

monkey.patch_all()


def img_downloader(url, file_name):
    # print("url>>>", url, "file_name>>>", file_name)
    content = urllib.request.urlopen(url)
    img_content = content.read()
    with open("C:/Users/16152/Desktop/material/图片下载测试/" + file_name + ".jpg", "wb") as i:
        i.write(img_content)
        time.sleep(0.4)


def main():
    os.mkdir("C:/Users/16152/Desktop/material/图片下载测试")

    img_url = [
        "https://i0.hdslb.com/bfs/album/e6697b9adb08947a026e3ec5230e58675337d3ce.jpg",
        "https://i0.hdslb.com/bfs/album/f4c54a8e9b9af100b39df03848720d5acc70c55f.jpg",
        "https://i0.hdslb.com/bfs/album/a6316d8afa8fc1c52effdab3e73c4e2a6cfe3eb2.jpg",
        "https://i0.hdslb.com/bfs/album/5f889c29c1bd1c54dc4be0be81638065801fdaec.jpg",
        "https://i0.hdslb.com/bfs/album/15967d03bf5cdf03053581c8d3f985209629b04d.jpg",
        "https://i0.hdslb.com/bfs/album/fff3253531f71f4be8933478f735dc948ad93c31.jpg",
        "https://i0.hdslb.com/bfs/album/a3f973a0ba676d571b79559782d4a5d9a76ea854.jpg",
        "https://i0.hdslb.com/bfs/album/8593266b0c079c603f25cfee283f216c2dc9ed07.jpg",
        "https://i0.hdslb.com/bfs/album/a0151eb33b9a27a6c064261eb13f102bd6de8a38.jpg",
        "https://i0.hdslb.com/bfs/album/9102196dbe6e51de9aac177add6589a63bccf93b.jpg",
        "https://i0.hdslb.com/bfs/album/13e87cc68fd42898763d7a9d0f6976724acc402f.png",

    ]
    img_list = list()
    for url in img_url:
        img_list.append(gevent.spawn(img_downloader, url, str(img_url.index(url))))

    gevent.joinall(img_list)


if __name__ == "__main__":
    main()
