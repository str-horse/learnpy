def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('lisi',19,city = 'beijing',job = 'Engineer')


def product(*args):
    if args:
        s = 1
        for x in args:
            s *= x
        return s
    else:
        raise TypeError
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# def add(a, b, *args, d=10, **kwargs):  # 这是一个关于函数可变参数的实验代码
#     print('a = {}, b = {}'.format(a, b))
#     print('args = {}'.format(args))
#     c = a + b
#     for arg in args:
#         c += arg
#     return c * d


# print(add(9, 5, 4, 2, 0, 9, 5, 7, 3, 2, x=8, y=6))