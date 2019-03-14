from xml.dom.minidom import parse
class Book:
    def __init__(self,bname=None,price=None,author=None):
        self.bname=bname
        self.price=price
        self.author=author
    def __str__(self):
        return '书名：{0}  价格：{1} 作者：{2}'.format(self.bname,self.price,self.author)
# 得到整个文档树
doc=parse('../domxml/zy_1.xml')
# 得到根节点
root=doc.documentElement
# 通过标签名获取
stu=root.getElementsByTagName('book')
# 新建一个空列表用来存储数据
lst=[]
for p in stu:
    bk=Book()
    bk.bname = p.getElementsByTagName('bname')[0].childNodes[0].data
    bk.price = p.getElementsByTagName('price')[0].childNodes[0].data
    bk.author = p.getElementsByTagName('author')[0].childNodes[0].data
    lst.append(bk)
for i in lst:
    print(i)