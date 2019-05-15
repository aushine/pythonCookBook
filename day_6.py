
def main():
    # 闭包结构
    def lin_1(k,b):
        def create_y(x):
            print(k * x + b)
        # 此处返回的是内部函数的引用
        return create_y

    lin_1(1, 2)


if __name__ == "__main__":
    main()