from functools import reduce
ages = [17, 20, 19, 16, 30, 23, 28, 21]
adult = filter(lambda ele: ele > 18, ages)
print(adult)  #返回一个可迭代列表的地址
a = list(adult)
print(a)

ages_2yearold = map(lambda ele: ele + 2, ages)
print(list(ages_2yearold))

b = reduce(lambda ele1, ele2: ele1 + ele2, ages)
print(b)

w = 2


print()
