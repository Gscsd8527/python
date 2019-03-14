# 以下实例通过用户输入两个变量，并相互交换：
num1=int(input('请输入第一个变量：'))
num2=int(input('请输入第二个变量：'))
print('第一个数值为：{0} 第二个数为：{1} '.format(num1,num2))
tep=num1
num1=num2
num2=tep
print('交换后---第一个数值为：{0} 第二个数为：{1} '.format(num1,num2))