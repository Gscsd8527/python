# 元素树ElementTree解析
from xml.etree.ElementTree import*
class Student:
    def __init__(self,name,age,sex,cj):
        self.name=name
        self.age=age
        self.sex=sex
        self.cj=cj
    def __str__(self):
        return '姓名：{0} 年龄：{1} 性别：{2} 成绩：{3}'.format(self.name,self.age,self.sex,self.cj)
root=parse('./domxml/xl_1.xml')
people=root.findall('stu')
lst=[]
for p in people:
    person=Student(1,2,3,4)
    person.name=p.find('name').text
    person.age = p.find('age').text
    person.sex = p.find('sex').text
    person.cj = p.find('cj').text
    lst.append(person)
for i in lst:
    print(i)