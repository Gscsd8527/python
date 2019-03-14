import pandas as pd
import numpy as np

data = np.arange(20).reshape(4, 5)
# df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=list('ABCDE'))
df = pd.DataFrame(data, columns=list('ABCDE'))
print(df)

#  选择行
print('选择某一行---------')
print(df.loc[2, :])
print('选择多行---------')
print(df.loc[1:3, :])


# 条件筛选
print('普通条件筛选')
print(df.loc[df.loc[:, 'A'] > 2, :])  # 判断A列中所有行的值大于2的行
print(df.iloc[0:2, 1:4])

# apply和applymap
# apply和applymap是对dataframe的操作，前者操作一行或者一列，后者操作每个元素
print('apply和applymap')
print(df.iloc[0:2, 1:4].apply(lambda x: x+1))
print(df.iloc[0:2, 1:4].applymap(lambda x: x+1))


