from pymysql import *
"""
模拟一个电商网站:

# 用户表,存储顾客的信息姓名 id 姓名, 地址, 手机号, 密码 
## 不在用户表中的用户不可以登陆, 引导用户前往注册
# 订单表 id 下单时间 用户表中的id
# 订单详情表 id  订单表的id 商品表(goods)的id 数量
"""


class GouDong:
    def __init__(self):
        # 创建了数据库的链接
        self.conn = connect(host="localhost", database="jing_dong", user="root", password="SXBCMZT.", charset="utf8")
        self.cursor = self.conn.cursor()
        # self.cursor.execute("select * from user")
        # print(self.cursor.fetchall())
        op = self.guidance()

        if op == "L":
            # 执行登录操作
            self.login()
        elif op == "R":
            # 执行注册操作
            self.regist()
        elif op == "B":
            # 执行购买操作,需要登录的同时完善个人信息(有地址以及手机电话)
            pass
        elif op == "Q":
            quit()

    def __del__(self):
        self.conn.close()
        self.cursor.close()

    @staticmethod
    def guidance():
        """开启操作引导"""
        print("-"*24)
        op = input("|请输入您想进行的操作: |\n|登陆(L)   注册(R)     |\n|请输入(圆括号中的字母):")
        return op.upper()

    def query(self, user_name):
        """查询方法"""
        # 先收到
        sql = "select name from user;"

        self.cursor.execute(sql)
        all_user = [y for x in self.cursor.fetchall() for y in x]
        # print("所有用户:", all_user)
        if user_name in all_user:
            # 输入的用户名存在于所有用户的列表中
            yield True
            # print("aaaaaaaa")
            # 验证输入正确的用户名的密码是否和user表中的password一致的sql语句
            sql = "SELECT password FROM USER WHERE NAME = %s;"
            self.cursor.execute(sql, user_name)
            user_password = self.cursor.fetchone()
            yield self.user_password == user_password[0]
        else:
            # 输入的用户名不存在与所有用户的列表中
            yield False


    def update(self):
        """更新方法"""
        pass

    def login(self):
        """登陆的方法"""
        # 获取输入的用户名和密码
        self.user_name = input("请输入用户名:")
        self.user_password = input("请输入密码:")
        # 创建一个判断用户的生成器,yield两个值,判断
        judge_user = self.query(self.user_name)
        if judge_user.__next__():
            # 用户名在用户表中,再判断用户的密码是否正确
            if next(judge_user):
                # 当秘密为正确时
                print("用户登录成功!")
            else:
                # 否则为密码错误
                print("密码输入错误")
        else:
            print("用户名不存在!\n是否需要前往注册\n")
    def regist(self):
        """注册的方法"""
        pass


def main():
    goudong = GouDong()


if __name__ == "__main__":
    main()