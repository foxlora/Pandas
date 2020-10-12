# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/10/12 14:41'

import pandas as pd
import numpy as np
df = pd.read_csv('../data/James_Harden.csv',encoding='utf8')
print(df.tail(5))

b = pd.pivot_table(df,index=['胜负'],columns=['主客场'],values=['命中'])
c = pd.pivot_table(df,index=[u'主客场',u'胜负'],values=[u'得分',u'助攻',u'篮板'])
d = pd.pivot_table(df,index=[u'主客场',u'胜负'],columns=[u'得分',u'助攻',u'篮板'])
print(c)
print(d)