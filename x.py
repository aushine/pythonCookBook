import itertools
"""
def a():
    x = 1
    while True:
        yield x
        print("aaaaa")
        x += 1
print(type(a()))
def b():
    for i in range(10):
        yield i
it = b()"""
'''
li = [1, 2, 3]


def yield_test():
    pass


def permutation(li):
    print(list(itertools.permutations(li)))
permutation(li)'''
from pymysql import connect

def main():
    # 创建Connection连接
    conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='SXBCMZT.',charset='utf8')
    # 获得Cursor对象
    cursor = conn.cursor()
    # 插入10万次数据
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
    # 提交数据
    conn.commit()

if __name__ == "__main__":
    main()