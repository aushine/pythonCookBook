from pymysql import *
from sys import stdout


def out(Any):
    return stdout.write(Any)


def get_all(cursor):
    cursor.execute("select * from goods;")
    """获取了所有的数据库内容"""
    for i in cursor.fetchall():
        print(i)


def get_classify(cursor):
    cursor.execute("select * from goods;")
    for i in cursor.fetchall():
        yield i[2]


def get_brand(cursor):
    cursor.execute("select * from goods;")
    for i in cursor.fetchall():
        yield i[3]


def get_info_byname(cursor):
    findname = input("输入想要查询的商品")
    sql = "select * from goods where name = %s;"
    cursor.execute(sql, [findname])
    print(cursor.fetchall())


def main():
    conn = connect(host="localhost", port=3306, database="jing_dong", user="root", password="SXBCMZT.", charset="utf8")
    cursor = conn.cursor()
    while True:
        op = input("请输入想要获取的数据:\na:全部\nc:所有的分类\nb:所有品牌\nall:我全都要\n请输入:")

        if op == "a":
            get_all(cursor)

        elif op == "c":
            print("所有商品种类:", set(get_classify(cursor)))

        elif op == "b":
            print("所有品牌种类:", set(get_brand(cursor)))

        elif op == "all":
            print("所有商品种类:", set(get_classify(cursor)))
            print("所有品牌种类:", set(get_brand(cursor)))
            get_all(cursor)

        elif op == "1":
            get_info_byname(cursor)

        elif op == "q":
            break

        else:
            print("输入有误,重新输入!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()