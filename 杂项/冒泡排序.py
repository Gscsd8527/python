lst=[1,7,2,3,8,11,22,5]
for i in range(0,len(lst)):
    for j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)