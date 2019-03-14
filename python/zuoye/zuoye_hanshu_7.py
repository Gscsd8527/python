# 7、写函数，检查传入字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
def mydct(**dct):
    for i,j in dct.items():
        if len(dct[i])>2:
            dct[i]=j[:2]
    return dct
my_dt=mydct(tan='tanzhenhua',zhen='tanzhenhua',hua='tanzhenhua')
print(my_dt)