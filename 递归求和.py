# def get_sum(n):
#     if n == 0:
#         return 0
#     return get_sum(n - 1) + n

# print(get_sum(10))


def fibonacci(n):  # 递归法求第n个斐波那契数列
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


m = int(input('请输入一个正整数：'))
print(fibonacci(m))