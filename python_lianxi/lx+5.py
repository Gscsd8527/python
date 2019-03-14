# 动态给字典输入5个学生的姓名和手机号
dit={}
for i in range(0,5):
    name=input('输入姓名：')
    tel=input('输入手机号：')
    dit[name]=tel
print(dit.items())
print(dit)