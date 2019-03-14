from xml.sax import ContentHandler,parse
class Book(object):
    def __init__(self,bname=None,price=None,anthor=None):
        self.a=bname
        self.b=price
        self.c=anthor
    def __str__(self):
        return ("书名:{} 价格:{} 作者:{}".format(self.a,self.b,self.c))
BookList=[]
class bookSax(ContentHandler):
    def __init__(self):
        self.Ber=None
        self.Tag=None
    def startDocument(self):
        pass
    def startElement(self, name, attrs):
        self.Tag=name
        if name=="book":
            self.Ber=Book()
    def characters(self, content):
        if self.Tag == "bname":
            self.Ber.a=content
        if self.Tag == "price":
            self.Ber.b = content
        if self.Tag == "author":
            self.Ber.c = content
    def endElement(self, name):
        if name=="book":
            BookList.append(self.Ber)
            self.Ber=None
        self.Tag=None
    def endDocument(self):
        pass
B=bookSax()
parse('../domxml/zy_1.xml',B)
for i in BookList:
    print(i)
