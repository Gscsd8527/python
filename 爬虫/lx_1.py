# 请求
import requests
from bs4 import BeautifulSoup
import re
html = requests.get('https://www.diediaow.com/')
html.encoding='utf-8'
# print(html.text)
html = html.text
soup = BeautifulSoup(html,'lxml')
title = soup.select('ul.ul-l.mb-r li a')[0]
print(title)
for i in title:
    print(i.text)
    print(i.get_text())
