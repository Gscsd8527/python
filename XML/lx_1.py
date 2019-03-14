# DOM解析
from xml.dom.minidom import parse
# 得到整个dom文档树
doc=parse('./domxml/xl_1.xml')
# 得到根节点
root=doc.documentElement
print(root)
# 根据标签名获取
student=root.getElementsByTagName('stu')
for p in student:
    # 得到stduent下面的name
    # 为什么('name')[0]后面还要加childNodes[0].data呢，不是直接.data，因为他以为后面还是节点，所以要获取
    print(p.getElementsByTagName('name')[0].childNodes[0].data)
    print(p.getElementsByTagName('age')[0].childNodes[0].data)
    print(p.getElementsByTagName('sex')[0].childNodes[0].data)
    print(p.getElementsByTagName('cj')[0].childNodes[0].data)