# 元素树ElementTree解析
from xml.etree.ElementTree import*
root=parse('./domxml/xl_1.xml')
people=root.findall('stu')
for p in people:
    n=p.find('name')
    print(n.text)