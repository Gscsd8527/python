# 通过用户输入的两个数，并计算两个数字之和
while 1:
    num1 = input('请输入第一个数字： ')
    if num1.isdigit():
        break
    else:
        print('输入错误，请重新输入：')
while 1:
    num2 = input('请输入第二个数字： ')
    if num2.isdigit():
        break
    else:
        print('输入错误，请重新输入：')
sum=int(num1)+int(num2)
print('两数之和为：%d'%sum)
