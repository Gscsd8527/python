# 判断用户输入的年份是否为闰年
year=int(input('请输入一个年份：'))
if (year%4==0 and year%100==0) or (year%100 and year%400==0):
    print('该年是闰年')
else:
    print('该年是平年')