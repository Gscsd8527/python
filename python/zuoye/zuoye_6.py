# 用户输入一个四位数，求各个为之和
# tan = int(input('请输入一个四位数:'))
# a=tan//1000
# b=(tan%1000)//100
# c=(tan%1000)//10%10
# d=tan%10
# Sum=a+b+c+d
# print(a,b,c,d)
# print(Sum)
#
# print()
# print()
#
# inp=int(input('请输入一个四位数：'))
# my_sum=0
# for i in range(0,4):
#     my_i=inp//(10**i)%10
#     my_sum+=my_i
# print(my_sum)

print()
print()
my_inp=int(input('请输入一个四位数：'))
print(type(my_inp))
my_sum=0
if my_inp in range(1000,my_inp+1):
    my_str=str(my_inp)
    my_sum=int(my_str[0])+int(my_str[1])+int(my_str[2])+int(my_str[3])
    print(my_sum)

