import pandas as pd
import numpy as np

#
s = pd.Series([1, 3, 5, 6, 8], index=list('acefh'))
print(s)
print(s.index)

# 增加行
print('-----------增加行---------')
print(s.reindex(list('abcdefgh'), fill_value=0))
# 空值的话拿前面的值来填充
print(s.reindex(list('abcdefgh'), method='ffill'))
