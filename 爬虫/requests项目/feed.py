import requests
import re
from bs4 import BeautifulSoup
# 解析下一页的链接
def page(url):
    html = requests.get(url)
    html.encoding='gbk'
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    page_url = soup.select('ul.pagelist a')[0].get('href')
    page_url = 'http://www.75bo.info'+page_url
    page_next = re.findall('.*_',page_url)[0]
    for i in range(1,20):
        if i == 1:
            page_url = 'http://www.75bo.info/list/index57.html'
        else:
            page_url = page_next + str(i) + '.html'
        print('解析的页面为：',page_url)
        parse(page_url)
# 解析每一页
def parse(page_url):
    html = requests.get(page_url)
    html.encoding='gbk'
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    nr = soup.find_all('ul',{'class':'m_Box1'})[0].find_all('a',{'class':'txt','target':'_blank'})
    for i in nr:
        name = i.text
        name = re.findall('(.*)..',name)[0]
        href = i['href']
        href = 'http://www.75bo.info'+href
        print('片名：{}   对应的链接：{}'.format(name,href))
        parse_url(name,href)

# 解析到MP4的链接
def parse_url(name,href):
    html = requests.get(href)
    html.encoding='gbk'
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    href_url = soup.find_all('div',{'class','l'})[0].find_all('a',{'class':'txt'})[0]['href']
    href_url = 'http://www.75bo.info'+href_url
    print('对应链接的播放地址',href_url)
    parse_mp4(name,href_url)

# 解析出对应的MP4地址
def parse_mp4(name,href_url):
    html = requests.get(href_url)
    html.encoding = 'gbk'
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    soup =str(soup)
    mp4 = re.findall("f:'(.*)',",soup)[0]
    print('mp4的地址为：',mp4)
    load(name,mp4)

# 下载视屏
def load(name,mp4):
    print('开始下载')
    file = 'E:/feed/'+name+'.mp4'
    nr = requests.get(mp4).content
    with open(file,'wb') as f:
        f.write(nr)
    print('下载完成')

if __name__ == '__main__':
    url='http://www.75bo.info/list/index57.html'
    page(url)



