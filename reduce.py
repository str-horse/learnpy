from functools import reduce  # 导入模块的语法
scores = [100, 89, 76, 87]
# 将前两个数分别分配给ele1和ele2,求和的结果再分配给ele1,下一个数分配给ele2,以此类推.
x = reduce(lambda ele1, ele2: ele1 + ele2, scores)
print(x)

# 求所有学生的年龄的总和
students = [{
    'name': 'zhangsan',
    'age': 18,
    'score': 98,
    'height': 180
}, {
    'name': 'lisi',
    'age': 21,
    'score': 97,
    'height': 185
}, {
    'name': 'jack',
    'age': 22,
    'score': 100,
    'height': 175
}, {
    'name': 'tony',
    'age': 23,
    'score': 90,
    'height': 176
}, {
    'name': 'henry',
    'age': 20,
    'score': 95,
    'height': 172
}]


# def bar(x, y):
#     return x + y['age']


# print(reduce(bar, students, 0))
# x = 0,如果不将x设为0,那么x 将是第一个字典值,运行后会报错
# y = {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180}

print(reduce(lambda x, y: x + y['age'], students, 0))
