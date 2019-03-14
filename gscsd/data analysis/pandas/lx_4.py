import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.NaN, 8, 4])
print(s)

dates = pd.date_range('20181207', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])  # 新增一列
print(df1)
df1.loc[dates[1:3], 'E'] = 2  # 给某些值赋值
print(df1)
print(df1.dropna())  # 把空值(即NaN值)删除掉
print(df1.fillna(value=5))  # 替换空值(即NaN值)
print(pd.isnull(df1))  # 判读数据集种是否包含空数据
print(pd.isnull(df1).any())  # 将数据集中包含空数据的列打印出来
print(pd.isnull(df1).any().any())  # 判断数据集中是否包含空数据 True或者False
print(df1.mean())  # 查看行的平均值， 默认是axis=0
print(df1.mean(axis=1))  # 查看列的平均值
print(df1.cumsum())  # 累加值
print('========广播概念=======')
s = pd.Series([1, 3, 5, np.NaN, 6, 8], index=dates).shift(2)
print(s)
print(df)
print(df.sub(s, axis='index'))

# 累加值
print('----------累加值--------')
print(df)
print(df.apply(np.cumsum))  # 每一行的每一列值都等于前几个值的和
print(df.apply(lambda x: x.max() - x.min()))


print('=======================')
a = pd.Series(np.random.randint(10, 20, size=20))
print(a)
print(a.value_counts())


# 拼接
print('-------拼接------')
print(pd.concat([df.iloc[:3], df.iloc[3:7], df.iloc[7:]]))

print('************************')
print(df)
print(df1)
print((df == df).all())  # 判断df和df1是否相等
print((df == df).all().all())

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(left)
print(right)
print('------联合查询-------')
# select * from left inner join right on left.key = right.key;
print(pd.merge(left, right, on='key'))

print('----------append----------')
print(df)
a = pd.Series(np.random.randint(1, 5, size=4), index=list('ABCD'))
print(a)
print(df.append(a, ignore_index=True))

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8),
})
print(df)
print(df.groupby('A').sum())
print(df.groupby(['A', 'B']).sum())


