import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dates = pd.date_range('20180516',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)
df['TAG']=['a','a','b','b','c','c']
# df1=df.reindex(index=dates[0:4],columns=list(df.columns)*['E'])
print(df)
print(df[df.TAG.isin(['a','b'])])