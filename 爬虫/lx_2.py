import requests
from bs4 import BeautifulSoup
import re
html = requests.get('https://www.gushiwen.org/shiwen/')
html.encoding='utf-8'
html=html.text
soup = BeautifulSoup(html,'lxml')
name = soup.select('div.left div.sons div.cont p')
url = soup.select('div.pagesright')
for n in name:
    nt = n.text
    print(nt)
for i in url:
    i=i.find('a')['href']
    print(i)
url = 'https://www.gushiwen.org/'+i
print(url)
if url is not None:
    html = requests.get(url)
    html.encoding = 'utf-8'
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    name = soup.select('div.left div.sons div.cont p')
    url = soup.select('div.pagesright')
    for b in url:
        b = b.find('a')['href']
        print(b)
    url = 'https://www.gushiwen.org/' + b
    print('url==',url)
    for n in name:
        nt = n.text
        print(nt)