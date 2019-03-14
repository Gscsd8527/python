# 数据整形

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']
                    ]))
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print('index=\n', index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=list('AB'))
print(df)

stacked = df.stack()
print('stacked=\n', stacked)  # 行索引和列索引进行转换
print(stacked.unstack())  # 装换回来
print(stacked.unstack().unstack())  # 再装换一次



# 数据透视
print('------------数据透视-------------')

df = pd.DataFrame({
    'A': ['one', 'one', 'two', 'three'] * 3,
    'B': ['A', 'B', 'C'] * 4,
    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
    'D': np.random.randn(12),
    'E': np.random.randn(12),
})
print(df)
# 以A，B为行索引，以C这一列作为列索引，看D的值，没有的值是NaN
print(df.pivot_table(values=['D'], index=['A', 'B'], columns=['C']))

# df.A 等于one的数据，并以C来分组，有多个值的话会求平均值
print(df[df.A == 'one'].groupby('C').mean())


# 时间函数
print('-----------------时间函数-----------------')

# 起始时间为20160301，创建600个值，间隔为秒
rng = pd.date_range('20160301', periods=600, freq='s')
print(rng)
s = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(s)
# 采样
print('-----------采样----------')
# 以季度为单位
rng = pd.period_range('2000Q1', '2016Q1', freq='Q')
print(rng)
print(rng.to_timestamp())  # 装换一下时间日期格式

print(pd.Timestamp('20160301') - pd.Timestamp('20160201'))
print(pd.Timestamp('20160301') + pd.Timedelta(days=5))

df = pd.DataFrame(
    {
        'id': [1, 2, 3, 4, 5, 6],
        'raw_grade': ['a', 'b', 'b', 'a', 'a', 'd']
    }
)
print(df)
df['grade'] = df.raw_grade.astype('category')
print(df)
print(df.grade)
df.grade.cat.categories = ['very good', 'good', 'bad']
print(df)
print(df.sort_values(by='grade', ascending=False))

# 格式化
s = pd.Series(np.random.randn(1000), index=pd.date_range('20000101', periods=1000))
print(s)
print('====================')
s = s.cumsum()  # 请平均值
print(s)

# 将图像画出来
print('------------将图像画出来-----------')
s.plot()


#  pandas 数据读写

df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
print(df)
# df.to_csv('a.csv')  # 写入到csv中

