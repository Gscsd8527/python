import pandas as pd
import numpy as np

# 创建一个默认的整数索引
s = pd.Series([1, 3, 5, np.nan, 9])
print(s)

# 通过传递numpy数组，使用datetime索引和标记列来创建DataFrame
print('通过传递numpy数组，使用datetime索引和标记列来创建DataFrame')
dates = pd.date_range('20181201', periods=7)
print(dates)
df = pd.DataFrame(np.random.rand(7, 4), index=dates, columns=list('ABCD'))
print(df)
print(df.values)
data = df.values
print(data.shape)
