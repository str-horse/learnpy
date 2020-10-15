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
# 字典和字典之间不能使用比较运算符


def foo(ele):
    # print(ele) = {}.format(ele)
    # 通过返回值告诉sort方法，按照元素的哪个属性进行排序
    return ele['age']


# 需要传递参数key来指定比较规则，key的参数类型是函数
# 在sort内部实现的时候，调用了foo函数，并传入了一个参数，参数就是列表里的元素ele
students.sort(key=foo)
print(students)
