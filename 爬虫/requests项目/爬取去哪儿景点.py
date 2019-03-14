import requests
from bs4 import BeautifulSoup
import re

def parse(url):
    html = requests.get(url,headers=headers)
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    city = soup.select('div.e_destin_ct dl.m_nav dd a')
    lst =[]
    for i in city:
        # 有的城市被推荐到热门城市中去了，而在地区中也有该城市，所以要去重
        if i.text not in lst:
            lst.append(i.text)
            city_name = i.text
            city_url = i.get('href')
            city_url='https:'+city_url
            parse_url(city_name,city_url)
# 解析每个城市url中的数据
def parse_url(city_name,city_url):
    print(city_name,city_url)
    html = requests.get(city_url,headers=headers)
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    print(soup)


if __name__=='__main__':
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    start_url='https://dujia.qunar.com/p/domestic?tm=ign_origin'
    parse(start_url)
