# DOM解析
from xml.dom.minidom import parse
class Student:
    def __init__(self,name,age,sex,cj):
        self.name=name
        self.age=age
        self.sex=sex
        self.cj=cj
    def __str__(self):
        return '姓名：{0} 年龄：{1} 性别：{2} 成绩：{3}'.format(self.name,self.age,self.sex,self.cj)
# 得到整个dom文档树
doc=parse('./domxml/xl_1.xml')
# 得到根节点
root=doc.documentElement
print(root)
# 根据标签名获取
student=root.getElementsByTagName('stu')
lst=[]
for p in student:
    # 得到stduent下面的name
    # 为什么('name')[0]后面还要加childNodes[0].data呢，不是直接.data，因为他以为后面还是节点，所以要获取
    people=Student(p.getElementsByTagName('name')[0].childNodes[0].data,p.getElementsByTagName('age')[0].childNodes[0].data,p.getElementsByTagName('sex')[0].childNodes[0].data,p.getElementsByTagName('cj')[0].childNodes[0].data)
    lst.append(people)
for i in lst:
    print(i)