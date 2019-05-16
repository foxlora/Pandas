'''
数据统计
df增加一行
df1.loc['行索引名'] = ''
df1.append()
df1.concat()
'''
import pandas as pd
import numpy as np
df = pd.read_excel('excel-comp-data.xlsx')
df['Total'] = df.Jan + df.Feb + df.Mar


#计算合计数
Sum = pd.DataFrame(df[['Jan','Feb','Mar']].sum()).T#行列转换
Sum = Sum.reindex(columns=df.columns) #将df1长度转换为df2长度
df_WithSum = df.append(Sum)



df_groupby = df[['state','Jan', 'Feb','Mar', 'Total']].groupby('state').sum()

def number_format(x):
    return "{:,.0f}".format(x) # 使用逗号分隔,没有小数位

formated_df = df_groupby.applymap(number_format)
formated_df.head()




#数据透视表
# pivot table
# pd.pivot_table 生成一个新的 DataFrame
'''
index 参数： 按什么条件进行汇总
values 参数：对哪些数据进行计算
aggfunc 参数：aggregation function，执行什么运算
'''
df_pivot = pd.pivot_table(df, index=['state'], values=['Jan','Feb','Mar','Total'], aggfunc= np.sum)

print(df_pivot)