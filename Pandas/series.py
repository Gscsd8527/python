# Series 是一个一维数组结构，可以存入任一一种python的数据类型
# (integers, strings, floating point numbers, Python objects, etc.)。
import pandas as pd
import numpy as np
s = pd.Series([1,3,5,np.nan,7,8])
print(s)
b = pd.Series([1,2,3,4,5],index=range(5))
print(b)