# 定义一个列表，让用户动态输入5个值，让后遍历输出列表
lst=[]
for i in range(0,5):
    my_str=input('输入值:')
    lst.append(my_str)
print(lst)
for j in lst:
    print(j,end=' ')