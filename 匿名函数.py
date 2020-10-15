def cacl(a, b, fn):
    c = fn(a, b)
    return c


x1 = cacl(5, 7, lambda x, y: x + y)
x2 = cacl(19, 3, lambda x, y: x - y)
print(x1, x2)