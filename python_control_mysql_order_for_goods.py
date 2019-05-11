from pymysql import *
from sys import stdout
"""
模拟一个电商网站:

# 用户表,存储顾客的信息姓名 id 姓名, 地址, 手机号, 密码 
## 不在用户表中的用户不可以登陆, 引导用户前往注册
# 订单表 id 下单时间 用户表中的id
# 订单详情表 id  订单表的id 商品表(goods)的id 数量
"""


def out(Any):
    return stdout.write(Any)


class GouDong:
    def __init__(self):
        # 创建了数据库的链接
        self.conn = connect(host="localhost", database="jing_dong", user="root", password="SXBCMZT.", charset="utf8")
        self.cursor = self.conn.cursor()
        # self.cursor.execute("select * from user")
        # print(self.cursor.fetchall())
        # 初始情况下登录显示为false
        self.is_loging = False
        while True:
            op = self.guidance("start")

            if op == "L":
                # 执行登录操作
                self.login()
            elif op == "R":
                # 执行注册操作
                self.regist()
            elif op == "B":
                # 执行购买操作,需要登录的同时完善个人信息(有地址以及手机电话)
                self.place_order()
            elif op == "V":
                pass
            elif op == "Q":
                quit()
            elif op == "LOGOUT":
                if self.is_loging:
                    self.is_loging = False
                    self.user_name = NULL
                    self.user_password = NULL
                else:
                    out("---->当前未登录任何账户<----\n")

    def __del__(self):
        self.conn.close()
        self.cursor.close()

    @staticmethod
    def guidance(inital):
        """开启操作引导"""
        if inital == "start":
            print("-" * 26)
            op = input("|请输入您想进行的操作:   |\n|登陆(L)   注册(R)       |\n|退出(Q)   下单(需登录(B)|\n|浏览(V)   注销(LOGOUT)  |\n|请输入:")
            return op.upper()
        elif inital == "personal":
            print("-"*26)
            op = input("|修改密码(C)    修改/完善个人信息(P)|")

    def query(self, user_name):
        """查询方法
        # 如何通过仅此一个查询方法实现下列查询功能
        1. 可以查询用户名是否存在于user表的密码和user表中name和password能否对应
        2. 当前登录的用户可以查询到自己的订单和个人资料
        """

        # 查询所有用户名的sql语句
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

        # 本用户的id在订单表中能匹配到至少有一个的订单就表示存在有订单

    def update(self, op, *info):
        """更新方法
        1. 此方法将注册,下单的信息写入数据库中
        3. 此方法可以更新个人信息(手机号码和地址)
        """
        # print(info)
        if op == "regist":
            # 将接收到的用户信息写入用户表中
            sql = "insert into user(name,password) values(%s, %s)"
            self.cursor.execute(sql, info)
            # out("用户注册成功")
            self.conn.commit()
        elif op == "place_order":
            # 执行下订单操作
            pass
        elif op == "perfect_personal_info":
            # 执行完善个人信息
            sql = "update user set tel = %s, addr = %s where name = %s"
            self.cursor.execute(sql, info)
            self.conn.commit()

    def login(self):
        """登陆的方法"""
        if not self.is_loging:
            # 获取输入的用户名和密码
            self.user_name = input("请输入用户名:")
            self.user_password = input("请输入密码:")
            # 创建一个判断用户的生成器,yield两个值,判断
            judge_user = self.query(self.user_name)
            if judge_user.__next__():
                # 用户名在用户表中,再判断用户的密码是否正确
                if next(judge_user):
                    # 当密码为正确时
                    # print("用户登录成功!")
                    # 把已登录的标识修改为true
                    self.is_loging = True
                else:
                    # 否则为密码错误
                    print("密码输入错误")
            else:
                op = input("用户名不存在!\n是否需要前往注册\nY/N:")
                if op.upper == "Y":
                    self.regist()
                elif op.upper == "N":
                    op = input("是否再次尝试输入用户名和密码:Y/N")
                    if op.upper == "Y":
                        self.login()
        else:
            out("已登录一个账号,请注销后再尝试登录\n")


    def regist(self):
        """注册的方法
        1. 输入用户名和密码进行注册,密码输入完后需要再确认密码(再输入一次)一致再操作数据库
        2. 用户账号注册成功时可以自行选择是否此时完善个人信息(手机号和地址)
        """
        out("=" * 25)
        user_name = input("\n输入用户名:")
        user_pwd = input("输入密码:")
        user_password = input("确认密码:")
        if user_pwd == user_password:
            # 确认密码成功
            self.update("regist", user_name, user_pwd)
        else:
            # 确认密码失败
            pass
        op = input("注册成功,是否现在完善用户信息.Y/N")
        if op.upper() == "Y":
            # 获取用户输入的个人信息送去update方法的完善信息分支
            addr = input("请输入您的详细地址:")
            tel = input("请输入您的手机/固话号码:")
            self.update("perfect_personal_info",  tel, addr, user_name)

        if op == "N":
            pass

    def place_order(self):
        # 下单的方法
        pass


def main():
    goudong = GouDong()


if __name__ == "__main__":
    main()
