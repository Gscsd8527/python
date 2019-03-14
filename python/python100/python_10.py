# 判断字符串是否为数字
num=input('请输入一串字符串：')
# num.isnumeric可判断中文数字，如：一、二、三、四。。。
if num.isnumeric():
    print('是')
