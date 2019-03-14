import requests
import json
from bs4 import BeautifulSoup

def main(url):
    data = soup.select('div#searchResult div.view div.item')
    for i in data:
        name = i.select('div.info span.title')[0].text
        price = i.select('div.info p.price span strong')[0].text.split()
        shopNick = i.select('div.info p.shopName span')[0].text
        payNum = i.select('div.info p.shopName span')[1].text
        print('{0}    {1}    {2}    {3}'.format(name,price,shopNick,payNum))
    # next_page()

def next_page():
    next_page = soup.select('div.pagination-page a.page-next')[0].get('href')
    print(type(next_page))
    print(next_page)
    if next_page is not None:
        main(next_page)

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    url = 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&keyword=女装&clk1=107ee08d32780fb3994edf785e4a33be&upsid=107ee08d32780fb3994edf785e4a33be'
    response = requests.get(url, headers=headers)
    response = response.text
    soup = BeautifulSoup(response, 'lxml')
    main(url)
