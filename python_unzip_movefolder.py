import multiprocessing
import os
import shutil
import zipfile
from collections import defaultdict
'''解压一个目录中的所有压缩包,
    或解压一个压缩包中的所有目录,
    将解压获得的所有目录和文件
'''
'''
movie_f = open("E:/anime/《星蝶公主》中英双字 - 高清 [1024×576]/《星蝶公主》S01E04 - 迪幻字幕组.mkv", "rb")
content = movie_f.read()

new_folder = open("E:/TEST/测试.mkv", "wb")
new_folder.write(content)

movie_f.close()
'''
"""
先把指定目录的压缩包全部解压缩
然后把解压缩后的目录放入字典中
递归调用把所有文件的路径提取出来
"""


def un_zip(file_name):
    """解压缩"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name.split(".")[0]):
        pass
    else:
        os.mkdir(file_name.split(".")[0])
    for names in zip_file.namelist():
        name = file_name.split("/")[0:-1]
        zip_file.extract(names, "/".join(name))
        if file_name.split(".")[0] not in file_dict["dir_name"]:
            # 把解压后的文件夹路径放入字典中存起来
            file_dict["dir_name"].append(file_name.split(".")[0])
    zip_file.close()


def un_rar(file_name):
    rar_file = rarfile.ZipFile(file_name)
    if os.path.isdir(file_name.split(".")[0]):
        pass
    else:
        os.mkdir(file_name.split(".")[0])
    for names in rar_file.namelist():
        name = file_name.split("/")[0:-1]
        rar_file.extract(names, "/".join(name))
        if file_name.split(".")[0] not in file_dict["dir_name"]:
            # 把解压后的文件夹路径放入字典中存起来
            file_dict["dir_name"].append(file_name.split(".")[0])
    rar_file.close()

def judge_folder(file_name):
    """接收到的路径再分别判断,是否是目录
        递归调用,把所有文件的路径写进dict,
        直到打开的文件夹没有文件夹,
        提取所有文件
    """
    names = os.listdir(file_name)
    folders = list()
    files = list()
    for name in names:
        if os.path.isdir(file_name + "/" + name):
            folders.append(file_name + "/" + name)
        else:
            files.append(file_name + "/" + name)

    #print("此文件夹中的文件夹", folder)
    for folder in folders:
        judge_folder(folder)

    #print("此文件夹中文件", file)
    for file in files:
        if file.split(".")[-1] == "zip" or file.split(".")[-1] == "rar":
            # 如果文件是压缩文件,路径放入压缩文件键中
            file_dict["compress_file"].append(file)
        else:
            # 如果文件是其他文件,路径直接放入文件键中
            file_dict["file_name"].append(file)


def file_dispose(file_name):
    """文件处理"""
    if file_name.split("/")[-1].split(".")[-1] == "zip":
        # 路径给的是一个目录文件的话
        un_zip(file_name)
    elif file_name.split("/")[-1].split(".") == "rar":
        # 判断给定的目录位置是不是rar文件
        pass
    else:
        print("\r \033[033m Warning 给定的路径非压缩包也非目录", end="")


def judge_dir(file_name):
    """判断传入目录类型的函数"""
    if os.path.isdir(file_name):
        # 如果一开始给定的路径是个目录的话,去目录提取
        # file_dict["dir_name"].append(file_name)
        judge_folder(file_name)
    else:
        # 如果不是目录,是文件,去文件处理
        file_dispose(file_name)


def file_copy(file_folder, newfolder):
    # print(newfolder)
    # print(file_folder)
    # 打开并读取文件路径上的文件

    old_f = open(file_folder, "rb")

    # 读取文件内容并存放到一个变量中
    content = old_f.read()
    file_name = file_folder.split("/")[-1]
    newfolder = newfolder + "/" + file_name
    # print(newfolder)
    new_f = open(newfolder, "wb")
    new_f.write(content)
    # 开启新文件夹,并写入内容

    # new_f = open(file_folder, "wb")

    new_f.close()
    old_f.close()


def main():
    # 创建一个进程池
    po = multiprocessing.Pool(3)
    # 获取文件(目录)名
    file_name = "M:/新建文件夹 (3)/测试"
    global new_folder
    new_folder = file_name.split("/")
    new_folder[-1] = "[提取]"+new_folder[-1]
    new_folder = "/".join(new_folder)
    os.mkdir(new_folder)
    # print(new_folder)
    # 创建一个字典来保存所有路径(文件,压缩文件,文件夹)
    global file_dict
    file_dict = defaultdict(list)

    # 判断给定的路径是压缩包还是文件夹
    judge_dir(file_name)
    """下列是提取完的文件,压缩包,文件夹路径"""
    #for k, v in file_dict.items():
    #  print(k, "==>", v)

    # 将压缩包键中的所有条目送去文件处理(解压),解压完后的文件夹再写入目录名键中
    for un_compress in file_dict["compress_file"]:
        file_dispose(un_compress)

    # 将dict中的所有文件夹路径送去目录提取
    for dir in file_dict["dir_name"]:
        judge_folder(dir)
        # shutil.rmtree(dir)

    for file in file_dict["file_name"]:
        #往进程池里添加进程
        po.apply_async(file_copy, (file, new_folder))

    po.close()
    po.join()

    for dir in file_dict["dir_name"]:
        shutil.rmtree(dir)


if __name__ == "__main__":
    main()