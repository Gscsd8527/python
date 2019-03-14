#  5、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。
def my_lst(mylst):
    lst=[]
    if len(mylst)>2:
        lst=mylst[:2]
    else:
        print('列表长度小于2')
    return lst
Mylst=my_lst([1,2,3,4,5,6])
print(Mylst)