# Python内置了求和函数sum()，但没有求积的函数，请利用reduce()来求积：
# 输入：[2, 4, 5, 7, 12]
# 输出：2*4*5*7*12的结果
# lst=[2, 4, 5, 7, 12]
# mysum=filter(lambda x:x**3,lst)
# for i in mysum:
#     print(i)

lst=[2, 4, 5, 7, 12]
mysum=map(lambda x:x**2,lst)
for i in mysum:
    print(i,end=' ')
