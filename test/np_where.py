# -*- coding: utf-8 -*-
'''
numpy.where() 有两种用法：

1. np.where(condition, x, y)
满足条件(condition)，输出x，不满足输出y。

2. np.where(condition)
只有条件 (condition)，没有x和y，则输出满足条件 (即非0) 元素的坐标 (等价于numpy.nonzero)。这里的坐标以tuple的形式给出，通常原数组有多少维，输出的tuple中就包含几个数组，分别对应符合条件元素的各维坐标。
'''
__author__ = 'Foxlora'
__time__ = '2020/10/12 21:41'

import numpy as np
a = np.arange(10)

b = np.where(a < 3)
c = [xv if c else yv for c, xv, yv in zip(a<3, a, 10*a)]
print(b)
