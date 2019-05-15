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

    @ set_func
    def test2():
        out("这是test2\n")

    test2()


if __name__ == "__main__":
    main()