# 自定义异常
class TanError(Exception):
    def __init__(self,age):
        self.age=age
    def __str__(self):
        return self.age

def ag():
    age=int(input('输入年龄：'))
    if age<=0 or age>100:
        raise TanError('年龄只能在0到100岁之间')
try:
     ag()
except TanError as tan:
    print(tan)

