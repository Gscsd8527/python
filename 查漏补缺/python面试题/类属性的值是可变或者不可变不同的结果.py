# 类属性的值是可变和不可变的区别
# class Person:
#     name='tanzhenhua'
# p1=Person()
# p2=Person()
# p1.name='tanpengfei'
# print(p1.name)
# print(p2.name)
class Person:
    name=[1,2,3,4,5]
p1=Person()
p2=Person()
p1.name.append(6)
print(p1.name)
print(p2.name)