# 分别统计出字符串a中英文字母,空格,数字和其他字符的个数.
# a = '13  2rr55gd!^fg,45o 24tk!l lw&&#e4rt'
a = '13  2rr55gd!^fg,45o 24tk!l lw&&#e4rt'
lst=[]
lst1={}
for i in a:
    if i not in lst:
        # lst.append(i)
        k=i
        v=a.count(k)
        lst1[k]=v
print(lst1)
# lst={}.fromkeys(lst)
# tep=0
# lst=[]
# num=[]
# for i in a:
#     lst.append(i)
#     if lst.count(i)>1:
#         lst.remove(i)
# for j in lst:
#     tep=a.count(j)
#     num.append(tep)
# for k in range(0,len(lst)):
#     print(lst[k],num[k])
# print(dct)

