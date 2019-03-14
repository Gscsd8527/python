from xml.sax import ContentHandler
from xml.sax import parse
import parser
class Book:
    def __init__(self,bname=None,price=None,author=None):
        self.bname=bname
        self.price=price
        self.author=author
    def __str__(self):
        return '书名：{0}  价格：{1} 作者：{2}'.format(self.bname,self.price,self.author)
lst=[]
class mysaxxml(ContentHandler):
    def __init__(self,bok=None,tag=None):
        self.bok=bok
        self.tag=tag
    def startDocument(self):
        print('startDocument')
    def startElement(self, name, attrs):
        # 将一开始得到的元素节点名字赋值给tag
        self.tag=name
        # 开始时碰见标记book时创建对象并赋值给bok
        if name=='book':
            self.bok=Book()
        print('startElement')
    def characters(self, content):
        # tag获取到的标签分别判断，判断后再赋值
        if self.tag=='bname':
            self.bok.bname=content
        if self.tag=='price':
            self.bok.bname=content
        if self.tag=='author':
            self.bok.bname=content
        print('characters')
    def endElement(self, name):
        # 元素节点结束时如果遇到结尾的book，那么将这个对象添加到这个列表中，对象里面有3个属性值
        if name=='book':
            lst.append(self.bok)
            self.bok=None
        # 每判断一次属性就要将tag清空，比如先判断dname后，那么清空后它又能接着放price了
        self.tag=None
        print('endElement')
    def endDocument(self):
        print('endDocument')

bk=mysaxxml()
parse('../domxml/zy_1.xml',bk)
for i in lst:
    print(i)
