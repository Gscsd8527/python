import sys
import pandas as pd
import json,time
import numpy as np

def Prob2Score(prob,basePoint=2100,PDO=200):
    y = np.log(prob / (1-prob))
    return int(basePoint + PDO / np.log(2) * (-y))

# 解析该模型，并将模型的数据以字典的格式返回
def read_medium_results(f='medium_value.txt'):
    # 得到的是一个多维列表
    data = np.loadtxt(f,delimiter=':',dtype=np.str)
    result = {}
                        # 得到第一维度的长度 6
    for row in range(0,data.shape[0]):
        k = np.str(data[row][0])
        result[k] = np.float(data[row][1])
    return result

# 清除数据
def clean_data(df,names,nan_lab):
    fill_dist = read_medium_results()
    names.append('erCode')
    df = df.ix[:, names].replace(nan_lab,np.nan)
                # 定位到哪个元素判断是否等于值
    df = df.mask(df.ix[:, 'erCode'] == 'E000996',-1)
    df = df.where(df.ix[:, 'erCode'] == 'E000000',-1)
    df = df.ix[:, :-1]
    df = df.fillna(fill_dist).astype(float)
    print(df)
    return df

def get_model_score(f,nan_lable='_'):
    columns = ['amount', 'bnkAmount', 'cnssAmount', 'p2pAmount', 'queryAmt', 'queryAmtM3', 'queryAmtM6']
    new_f = f['MSC8037']['records'][0]
    print(new_f)
    # df = pd.DataFrame.from_dict(new_f,orient='index').T
    # p_data = clean_data(df,columns,nan_lable)
    # idx = p_data.where(p_data == -1).dropna().index
    # p_data = p_data.mask(p_data == -1).dropna()
    # if p_data.empty:
    #     return -1
    # bst = xgb.Booster(model_file='model/qianhai.model')  # init model
    # dtest = xgb.DMatrix(p_data)
    # ptest = bst.predict(dtest)
    # get_score = np.vectorize(Prob2Score)
    # ptest_score = get_score(ptest)
    # return ptest_score
print('==============')
get_model_score()