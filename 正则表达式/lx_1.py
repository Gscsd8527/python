import re
result=re.match('^1[1,3,4,5,6,7,8,9]\d{9}$','14779569000')
print(result.span())
print(result.group())
qq=re.match('^[1-9]\d{5,9}@qq.com$','2567325188@qq.com')
print(qq.span())

a=re.match('[t,b,v]','tan')
print(a.span())