import time

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
    def my_align(_string, _length, _type='L'):
        """
        --->此函数来自简书作者: @Roi_Rio<---
        中英文混合字符串对齐函数
        my_align(_string, _length[, _type]) -> str

        :param _string:[str]需要对齐的字符串
        :param _length:[int]对齐长度
        :param _type:[str]对齐方式（'L'：默认，左对齐；'R'：右对齐；'C'或其他：居中对齐）
        :return:[str]输出_string的对齐结果
        """
        _str_len = len(_string)  # 原始字符串长度（汉字算1个长度）
        for _char in _string:  # 判断字符串内汉字的数量，有一个汉字增加一个长度
            if u'\u4e00' <= _char <= u'\u9fa5':  # 判断一个字是否为汉字（这句网上也有说是“ <= u'\u9ffff' ”的）
                _str_len += 1
        _space = _length-_str_len  # 计算需要填充的空格数
        if _type == 'L':  # 根据对齐方式分配空格
            _left = 0
            _right = _space
        elif _type == 'R':
            _left = _space
            _right = 0
        else:
            _left = _space//2
            _right = _space-_left
        return ' '*_left + _string + ' '*_right

    @staticmethod
    def guidance(inital):
        """开启操作引导"""
        if inital == "start":
            out("=" * 25)
            op = input("\n|请输入您想进行的操作:   |\n|登陆(L)   注册(R)       |\n|退出(Q)   下单(需登录(B)|\n|浏览(V)   注销(LOGOUT)  |\n|请输入:")
            return op.upper()
        elif inital == "personal":
            out("=" * 25)
            op = input("|修改密码(C)    修改/完善个人信息(P)|")
        elif inital =="query_filtter":
            out("=" * 25)
            op = input("\n|只看品牌(1)  只看类型(2)|\n|查看所有(3):            |\n请输入:")

            return op

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
        # sql = "select g.name as 型号,b.name as 品牌,c.name as 类型,g.is_saleoff as 是否售空 from goods as g inner join brand as b inner join cate_name as c"

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
        elif op == "update_orders":
            # 1.先往orders插入当前时间和已登录的user_id
            # 2. 把orders列表中保存的goods_id 插入到
            # 将当前用户的id保存到变量中
            sql = f"select id from user where name = '{self.user_name}'"
            local_user_id = self.execute(sql, "query")[0][0]

            #获取当前时间
            local_time = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(time.time()))

            sql = f"insert into orders(order_date_time, user_id) values('{local_time}', {local_user_id})"
            # 往orders表中插入当前时间和使用登录用户查询到的用户id
            self.execute(sql, "update")

            # 往orders_info表中插入上方表插入order_id所有下单的商品id和数量
            # 把用户id商品id和数量插入到orders

            # 如何获取到准确的当前创建的订单id
            # 根据上方存储的时间和用户id查询的订单id的sql语句
            sql = f"select id from orders where user_id = '{local_user_id}' and order_date_time = '{local_time}';"
            order_id = self.execute(sql, "query")[0][0]
            # 每次调用更新订单的函数都会刷新时间
            # 就可以保证订单详情表不会重复插入相同的订单
            for k, v in info[0].items():
                sql = f"""insert into orders_info(order_id, goods_id, quantity) values({order_id}, {k}, {v})"""
                self.execute(sql, "update")

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

    def query_goods(self, filtter):
        if filtter == "1":
            # 只看类型的查询
            pass
        if filtter == "2":
            # 只看品牌的查询
            pass
        if filtter == "3":
            # 查看所有商品的查询
            self.start = 0
            limit = f"limit {self.start}, 5"
            sql = """select g.name as 型号,b.name as 品牌,c.name as 类型, g.price, g.id, g.checked 
                    from (goods as g inner join brand as b on g.brand_id = b.id) inner join cate_name as c 
                    on c.id = g.cate_id %s; """
            # sql = sql %limit

            self.limitAndpaging(sql)
            #如何将分页和翻页的功能实现覆用
            """
                for i in query_content:
                    print(f"|型号:{self.my_align(i[0], 34)}|品牌:{i[1]}   |类型:{i[2]}    选中({query_content.index(i)+1})")
                if (len(query_content)-start) < -5:
                    op = input("|上一页(<)\n请输入:")
                if start == 0:
                    op = input("|下一页(>)\n请输入:")
                elif start >= 5:
                    op = input("|上一页(<)     下一页(>)\n请输入:")

                if op == "<" and start >= 5:
                    start -= 5
                if op == ">" and start < 21:
                    start += 5
                if op.upper() =="Q":
                    break
                print("*"*50)"""

    def execute(self, sql, type_):
        self.cursor.execute(sql)
        if type_ == "query":
            return self.cursor.fetchall()
        if type_ == "update":
            self.conn.commit()

    def limitAndpaging(self, sql):
        # 保存选中的商品id的列表
        check_list = dict()
        while True:
            limit = f"limit {self.start}, 5"
            query_content = self.execute(sql %limit, "query")
            for i in query_content:
                i_content = f"|型号:{self.my_align(i[0], 34)}|品牌:{i[1]}   |类型:{i[2]} |价格{i[3]}"
                if i[-2] not in check_list:
                    i_content += f"    勾选({query_content.index(i)+1})"
                if i[-2] in check_list:
                    i_content += f"    增加数量"
                print(i_content)
            if (len(query_content)-self.start) < - 5:
                op = input("|上一页(<)     下单(E)\n请输入:")
            if self.start == 0:
                op = input("|下一页(>)     下单(E)\n请输入:")
            elif self.start >= 5:
                op = input("|上一页(<)     下单(E)     下一页(>)\n请输入:")
            try:
                if 5 > int(op) > 1:
                    # print("++++++>Test<++++++")
                    pass
            except Exception as ret:
                pass
            else:
                # 如果输入了数字就表示选中了某一个商品
                # 就把选中的那个i值的id保存到
                # 把op-1的值索引到query_content
                goods_id = query_content[int(op)-1][-2]
                if goods_id not in check_list.keys():
                    check_list[goods_id] = 1
                else:
                    # print("========>数量增加<=========")
                    check_list[goods_id] += 1
            if op == "<" and self.start >= 5:
                self.start -= 5
            if op == ">" and self.start < 21:
                self.start += 5
            if op.upper() == "Q":
                break
            # print(check_list)
            if op.upper() == "E":
                # 如果选中了下单,就可以把已选中的商品id送去写入到订单表和订单详情表中
                self.place_order(check_list)
                break

            print("*"*100)

    def place_order(self, orders=None):
        # 下单的方法
        # 判断是否有效登录
        """登录完成后
        1. 客户端可以选择品种和品牌过滤商品
        2. 客户端可以选择价格高到低或者低到高排序
        """
        if orders:
            # 如果接收到订单
            # for k, v in orders.items():
                # print(f"商品id:{k} 数量:{v}")
            self.update("update_orders", orders)
        else:
            # 还没接收到订单
            if self.is_loging:
                filtter = self.guidance("query_filtter")
                self.query_goods(filtter)
            else:
                out("当前未登录,请登陆后再尝试")


def main():
    goudong = GouDong()


if __name__ == "__main__":
    main()
