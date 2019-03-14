from urllib.request import urlopen
from bs4 import BeautifulSoup
http = urlopen('http://www.baidu.com')
bs=BeautifulSoup(http.read())
#bs1=bs.findAll('body',{'class':{"qrcodeCon","qrcode-img"}})
#bs1=bs.findAll('',{'class':{"qrcodeCon","qrcode-img"}})
#bs1=bs.findAll(id='lh')
bs1=bs.findAll('img')
print(bs1)