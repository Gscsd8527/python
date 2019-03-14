import requests
from bs4 import BeautifulSoup

# 得到每个offset值
def off_set():
    offset = 18
    # 先取99个ajax，
    for i in range(1,100):
        if i == 1:
            parse_url(offset)
        else:
            offset = limit + offset
            parse_url(offset)

# 将得到的offset传入
def parse_url(offset):
    # 带参传递
    data = {
        'retrieve_type':'by_subject',
        'limit':'20',
        'offset':offset
    }
    # 请求这个ajax地址
    response = requests.get(start_ajax,params=data,headers=headers)
    # 得到的数据是个json格式，所以用requests自带的json函数来解析它
    ajax_data=response.json()
    # 解析得到每篇文章的url，因为ajax是个字典格式，而其中result的值却是个列表，所以要用[0]取出
    lst=ajax_data['result']
    for i in lst:
        url = i['url']
        print(url)
        parse(url)

def parse(url):
    html = requests.get(url,headers=headers)
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    data = soup.find_all('div',class_='content-th')
    for i in data:
        title = i.find_all('a')[0].text
        name = i.find_all('h1')[0].text.split()[0]
        zuoze = i.find_all('div','content-th-info')[0].find_all('a')[0].text
        time = i.find_all('div','content-th-info')[0].find_all('meta')[0]['content']
        print('{}\t\t{}\t\t{}\t\t{}'.format(title,name,zuoze,time))

if __name__ == '__main__':
    start_ajax = 'https://www.guokr.com/apis/minisite/article.json?'
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    # 每个offset都是以18为基数，每次叠加20
    limit = 20
    off_set()


