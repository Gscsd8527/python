# 任意输入年月日，计算出这是这一年的第几天
year=int(input('请输入年份：'))
month=int(input('请输入月份：'))
day=int(input('请输入日：'))
lst=[31,29,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100==0) or (year%100 and year%400==0):
    lst[1]=29
else:
    lst[1]=28
sun=0
if month==1:
    sun_day=day
else:
    while month>=2:
        sun+=lst[month-2]
        month-=1
sun_day=sun+day
print('这是一年中的第%d天'%sun_day)

