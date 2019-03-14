# 10个数围成一个圈，按3的倍数去掉，剩下的数剩什么？
lst=list(range(1,11))
lst1=[]
for i in lst:
    if i%3==0:
        a=lst.index(i)
        lst.pop(a)
