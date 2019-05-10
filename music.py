import urllib.request
url_content = urllib.request.urlopen("https://music.163.com/#/my/m/music/playlist?id=126427897")
print(url_content.read().decode("utf-8"))
