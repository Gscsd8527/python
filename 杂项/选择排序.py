# 对于一组关键字{K1,K2,…,Kn}， 首先从K1,K2,…,Kn中选择最小值，假如它是 Kz，则将Kz与 K1对换；
# 然后从K2，K3，… ，Kn中选择最小值 Kz，再将Kz与K2对换。
# 如此进行选择和调换n-2趟，第(n-1)趟，从Kn-1、Kn中选择最小值 Kz将Kz与Kn-1对换，
# 最后剩下的就是该序列中的最大值，一个由小到大的有序序列就这样形成。
lst=[7,2,3,8,11,22,5,1]
for i in range(0,len(lst)):
    m=i
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[m],lst[j]=lst[j],lst[i]
    print(lst)


