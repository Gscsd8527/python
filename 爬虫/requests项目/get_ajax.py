import requests
from bs4 import BeautifulSoup
url = 'https://www.csdn.net/api/articles?type=more&category=home&shown_offset=1529561433425066'
html = requests.get(url)
# 将得到的HTML代码设置Wieutf-8格式
html.encoding = 'utf-8'
# 获取到装换格式后的HTML代码
html = html.text
html = BeautifulSoup(html,'lxml')
nr = html.select('ul.feedlist_mod.home li.clearfix')
print(len(nr))
for i in nr:
    title = i.select('div.list_con div.title h2 a')
    print(title[0].text.split()[0])
