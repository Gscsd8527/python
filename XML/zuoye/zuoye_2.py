from xml.etree.ElementTree import *
class Book:
    def __init__(self,bname=None,price=None,author=None):
        self.bname=bname
        self.price=price
        self.author=author
    def __str__(self):
        return '书名：{0}  价格：{1} 作者：{2}'.format(self.bname,self.price,self.author)
doc=parse('../domxml/zy_1.xml')
root=doc.findall('book')
lst=[]
for p in root:
    bk=Book()
    bk.bname = p.find('bname').text
    bk.price = p.find('price').text
    bk.author = p.find('author').text
    lst.append(bk)
for i in lst:
    print(i)