# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
# 以下实例为通过用户输入一个数字，并计算这个数字的平方根：
while 1:
    num=input('请输入一串数字：')
    if num.isdigit():
        break
    else:
        print('输入错误，请您重新输入：')
for i in range(1,100):
    if i**2==int(num):
        print('该数的平方根为：%d'%i)


