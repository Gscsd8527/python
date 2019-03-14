# SAX事件驱动的过程
from xml.sax import ContentHandler
from xml.sax import parse
import parser
class Student:
    def __init__(self):
        self.name=None
        self.age=None
        self.sex=None
        self.cj=None
    def __str__(self):
        return '姓名：{0} 年龄：{1} 性别：{2} 成绩：{3}'.format(self.name,self.age,self.sex,self.cj)
lst=[]
class mysaxxml(ContentHandler):
    def __init__(self):
        self.stud=None
        self.tag=None
    def startDocument(self):
        print('startDocument')
    def startElement(self, name, attrs):
        # 将一开始得到的元素节点名字赋值给tag
        self.tag=name
        if name=='stu':
            # 开始时碰见标记stu时创建对象并赋值给stud
            self.stud=Student()
        print('startElement')
    def characters(self, content):
        if self.tag=='name':
            self.stud.name=content
        if self.tag=='age':
            self.stud.age=content
        if self.tag=='sex':
            self.stud.sex=content
        if self.tag=='cj':
            self.stud.cj=content
        print('characters')
    def endElement(self, name):
        if name=='stu':
            lst.append(self.stud)
            self.stud=None
        self.tag=None
        print('endElement')
    def endDocument(self):
        print('endDocument')

st=mysaxxml()
parse('./domxml/xl_1.xml',st)
for p in lst:
    print(p)
