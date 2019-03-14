from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.baidu.com')
bs = BeautifulSoup(html.read())
# 找出子节点
for child in bs.find('div',{'qrcode-text'}).children:
    print(child)
