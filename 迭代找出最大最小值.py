# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        L_max = L[0]
        L_min = L[0]
        for i in L:
            if i > L_max:
                L_max = i
            if i < L_min:
                L_min = i

    # # 下面这种方法省略了初始判空
    # L_min = None
    # L_max = None
    # for i in L:
    #     if not L_min or i < L_min:
    #         L_min = i
    #     if not L_max or i > L_max:
    #         L_max = i
    

    return (L_min, L_max)


# 测试
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')