# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    if a == 0:
        if b != 0:
            x = c / b
        else:
            x = '此方程无解'
    else:
        m = b**2 - 4 * a * c
        if m >= 0:
            x1 = (-b + math.sqrt(m)) / (2 * a)
            x2 = (-b - math.sqrt(m)) / (2 * a)
            x = (x1, x2)
        else:
            x = '此方程无解'
    return x


print('quadratic(2, 2, 1) =', quadratic(2, 2, 1))