import requests
import re
from bs4 import BeautifulSoup

def parse(url, headers):
    search = '神州专车'
    limitType = 'all'
    params = {
        'search':search,
        'limitType':limitType
    }
    http = requests.get(url, params=params, headers=headers)
    print(http.status_code)
    http = http.text
    soup = BeautifulSoup(http,'lxml')
    wz = soup.find_all('p',class_='link_title2')
    for i in wz:
        print(i)
if __name__ == '__main__':
    url = 'http://s.weibo.com/list/relpage'
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    parse(url, headers)