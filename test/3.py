# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/10/13 12:31'
import pandas as pd
import numpy as np
df = pd.DataFrame({'BoolCol': [1, 2, 3, 3, 4],'attr': [22, 33, 22, 44, 66]})
a = df[(df.BoolCol>=3)&(df.attr>30)].index.tolist()

b = df.index
print(type(b))