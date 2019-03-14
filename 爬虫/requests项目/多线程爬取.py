import requests
from bs4 import BeautifulSoup
import re
import time
import threading
def parse(url):
    http = requests.get(url,headers=headers)
    http = http.text
    soup = BeautifulSoup(http,'lxml')
    # 第一个不是，所以要过滤掉
    nr = soup.find_all('tbody')[0].find_all('tr')[1:]
    for i in nr:
        lb = i.find_all('td',{'class':'td2'})[0].a.text
        book_name = i.find_all('td',{'class':'td3'})[0].span.a.text
        zuoze = i.find_all('td',{'class':'td6'})[0].a.text
        zishu = i.find_all('td',{'class':'td5'})[0].text
        zishu = int(zishu)
        zhuangtai = i.find_all('em',{'class':'fc2'})[0].text.split()[0]
        print('{0}\t{1}\t{2}\t{3}\t{4}'.format(lb,book_name,zuoze,zishu,zhuangtai))


def next_page(url):
    http = requests.get(url,headers=headers)
    http = http.text
    soup = BeautifulSoup(http,'lxml')
    page = soup.find_all('div',{'class':'page'})[0].find_all('a')[3]['href']
    page = re.findall('.*2_0_0_0_0_0_0_0_',page)[0]
    for i in range(1,5):
        pg = 'http://all.17k.com' + page + str(i) + '.html'
        parse(pg)
        print(pg)

if __name__ == '__main__':
    url = 'http://all.17k.com/lib/book/2_0_0_0_0_0_0_0_1.html'
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    start_time = time.time()
    print('开始爬取的时间是：',start_time)
    next_page(url)
    end_time = time.time()-start_time
    print('花了{}秒'.format(end_time))
