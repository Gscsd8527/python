# 推导
number=[x*x for x in range(1,10)]
print(number)
for x in range(1,10):
    print(x*x)
# (x,y)其中x是0-5之间的偶数
# y是0-5之间的奇数组成元祖列表
# num1=[x for x in range(0,6,2)]
# num2=[y for y in range(0,6) if y%2==1]
# print(num1)
# print(num2)

# num=[(x,y) for x in range(0,6,2) for y in range(0,6) if y%2==1]
# print(num)