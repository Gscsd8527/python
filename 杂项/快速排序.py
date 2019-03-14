# 循环一遍把最大的得出来
lst=[1,7,2,3,8,11,22,5]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
    print(lst)
