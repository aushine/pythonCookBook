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
        def call_func(a):
            out("权限验证1\n")
            out("权限验证2\n")
            func(a)
        return call_func

    @ set_func
    def test3(num):
        out("这是test3,我有一个参数{}\n".format(num))

    test3(100)


if __name__ == "__main__":
    main()