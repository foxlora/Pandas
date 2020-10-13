# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/10/13 12:41'


import pandas as pd
import numpy as np
df = pd.read_csv('../data/James_Harden.csv',encoding='utf8')

grouped = df.groupby(['胜负'])

print(grouped.count())