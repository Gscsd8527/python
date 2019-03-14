import pandas as pd
import numpy as np
d = {'A':1,'B':pd.Timedelta('20180515'),'C':range(4),'D':np.arange(4)}
print(d)
df = pd.DataFrame(d)
print(df.dtypes)
# 访问A这一列的数据
print('df.A=',df.A)
print('df.B=',df.B)
# tpye(df.B)= <class 'pandas.core.series.Series'>
print('tpye(df.B)=',type(df.B)) #是一个series类型