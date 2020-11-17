# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/10/13 12:41'


import pandas as pd
import numpy as np
import tensorflow as tf
df = pd.read_csv('../data/James_Harden.csv',encoding='utf8')

grouped = df.groupby(['胜负']).count()

colorMap = {value:index for index,value in enumerate(set(df["胜负"]))}
df['胜负'] = df['胜负'].map(colorMap )


b = tf.ones((2,3)) * 3
c = tf.pow(b,2)
print(b)
print(c)
