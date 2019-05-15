from sys import stdout


def out(Any):
    stdout.write(Any)


def main():
    # 闭包结构
    def lin_1(k, b):
        def create_y(x):
            print(k * x + b)
        # 此处返回的是内部函数的引用
        return create_y

    def set_func(func):
        def call_func():
            out("这是权限验证1______\n")
            out("这是权限验证2______\n")
            func()
        return call_func

    def test1():
        out("这是test1\n")

    test1 = set_func(test1)
    test1()

    out("==========================\n")

    # 对有参数无返回值的函数进行装饰
    @ set_func  # 等价于test2 = set_func(test2)
    def test2():
        out("这是test2\n")

    test2()

    # 对有一个参数的函数进行装饰
    def set_func(func):
        out("开始进行装饰_________\n")  # 当圈上了这个闭包函数时就已经调用了这个装饰
        def call_func(a):
            out("权限验证1\n")
            out("权限验证2\n")
            func(a)
        return call_func
    out("==========================\n")

    @ set_func
    def test3(num):
        out("这是test3,我有一个参数{}\n".format(num))

    # test3(100)

    # 对带有收集参数的函数进行装饰
    def set_func(func):
        def call_func(*args, **kwargs):
            out("这是权限验证1\n")
            out("这是权限验证2\n")
            func(*args, **kwargs)
        return call_func

    @ set_func
    def test4(num, *args, **kwargs):
        out("test4______%d\n" %num)
        print("test4______", args)
        print("test4______", kwargs)

    test4(100)
    test4(100, 200)
    test4(100, 200, 300, m=100)


if __name__ == "__main__":
    main()