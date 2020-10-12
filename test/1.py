# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/10/12 11:55'

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
a = np.arange(12).reshape(2,6)
df = pd.read_csv('../data/ml-latest-small/ratings.csv')
'''
userId         int64
movieId        int64
rating       float64
timestamp      int64
dtype: object
'''


num_users = df['userId'].unique().shape[0]
num_movies  =df['movieId'].unique().shape[0]

df.drop('timestamp',axis=1,inplace=True)


# train_data,test_data = train_test_split(df,test_size=0.2)


print(f'num_users:{num_users},num_movies:{num_movies}')
#建立[num_users,num_movies]评分矩阵
ratings_matrix = df.pivot_table(index='userId',columns='movieId',values='rating',fill_value=0)

print(ratings_matrix)
items = ratings_matrix.loc[:,[1,2]]
b = items[1] !=0
c = items[2] !=0
d = [all(i) for i in zip(b,c)]
e = [ i for i in d if i]
print(len(e))
#计算相似度


