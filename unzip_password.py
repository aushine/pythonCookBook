import zipfile
# zipfile.ZipFile.extract
"""extract(self, member, path=None, pwd=None)
    Extract a member from the archive to the current working directory,
    using its full name. Its file information is extracted as accurately
    as possible. `member' may be a filename or a ZipInfo object. You can
    specify a different directory using `path'."""

"""穷举破解zip压缩包的密码
===========================
1.把所有数字,字母,符号组合成一个列表
2.先一个一个遍历穷举
3.累加个数来遍历,两个两个
"""

