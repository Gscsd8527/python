from pyquery import PyQuery as pq
import requests
response = requests.get('https://hao.360.cn/')
html = response.text
data = pq(html)
li = data('ul.tab.gclearfix.theme-search-tab a').items()
print(li)
for i in li:
    print(type(i))
    print(i)
    print('-----', i.text())
    print(i.attr.href)
    print(i.attr('href'))
    print(i.attr('class'))



