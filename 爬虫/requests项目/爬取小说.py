import requests
from bs4 import BeautifulSoup
import re
headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',}
url = 'http://www.biqukan.com/3_3039/1351331.html'
html = requests.get(url,headers=headers)
# 获取到网页的文本格式
html = html.text
soup = BeautifulSoup(html,'lxml')
# 选择器得到的是一个列表，只有一个元素，要选取第一个
zhangjie = soup.select('div.content h1')[0]
# 得到章节的文本内容
zhangjie = zhangjie.text
print(zhangjie)
# 查找属性是id为'content'且class为'showtxt'的标签
text = soup.find(id='content', class_='showtxt')
# 得到文本内容
text=text.text
# 将得到的文本存入文件中
with open('xiaoshuo.txt','w',encoding='utf-8') as f:
    f.write(zhangjie)
    f.write(text)