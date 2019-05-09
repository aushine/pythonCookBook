from pymysql import *


def main():
    coon = connect(host="localhost", port=3306, database="jing_dong", user="root", password="SXBCMZT.",charset="utf8")
    cursor = coon.cursor()
    cursor.execute('select * from goods;')
    for i in cursor.fetchall():
        print(i)
    print(type(i[4]))
    cursor.close()
    coon.close()
if __name__ == "__main__":
    main()