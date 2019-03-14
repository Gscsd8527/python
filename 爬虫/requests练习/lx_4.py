import requests
from bs4 import BeautifulSoup

def page(url):
    # 使用get方式请求页面，并使用user-agent
    html = requests.get(url,headers = head)
    # 将得到的HTML代码设置Wieutf-8格式
    html.encoding='utf-8'
    # 获取到装换格式后的HTML代码
    html=html.text
    # 使用BeautifulSoup来解析网页
    soup = BeautifulSoup(html,'lxml')
    name = soup.select('div.left div.sons div.cont p.source')
    for na in name:
        sr = na.text
        print(sr)
    print('======================')
    gs = soup.select('div.left div.sons div.cont div.contson')
    gs = gs[0].text.split()
    print(gs)
    next_page = soup.select('div.pagesright a.amore')
    next_page=next_page[0].get('href')
    next_page='https://www.gushiwen.org'+next_page
    print(next_page)
    page(next_page)# 递归调用


def main():
    page(url)
    # print('下一页链接：',page_next)
    # if page_next is not None:
    #     page(page_next)
    # page(page_next)

if __name__=='__main__':
    head = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    }
    url = 'https://www.gushiwen.org/shiwen/'
    main()




