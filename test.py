def add(a, b, *args, d=10, **kwargs):  # 这是一个关于函数可变参数的实验代码
    print('a = {}, b = {}'.format(a, b))
    print('args = {}'.format(args))
    c = a + b
    for arg in args:
        c += arg
    return c * d


print(add(9, 5, 4, 2, 0, 9, 5, 7, 3, 2, x=8, y=6))

