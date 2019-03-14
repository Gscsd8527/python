import requests
from bs4 import BeautifulSoup

# 解析url
def main(url):
    html = requests.get(url, headers=headers)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    # 得到神墓正文的dd标签，跳过最新章节
    nr = soup.select('div.listmain dd')[12:]
    # 分别读取其中的dd标签
    for i in nr:
        # 分别取出每个标签的内容和链接
        title = i.text
        url = i.a.get('href')
        # 得到的url不完整，所以做进一步的拼接
        url = 'http://www.biqukan.com' + url
        # 调用解析网页内容的小说正文
        next_page(title,url)

# 解析得到网页的正文
def next_page(title,url):
    txt = requests.get(url)
    html = txt.text
    # 进一步解析每一张url的网页内容
    soup = BeautifulSoup(html, 'lxml')
    # 查找属性是id为'content'且class为'showtxt'的标签
    text = soup.find(id='content', class_='showtxt')
    # 获取到小说正文
    text = text.text
    # 下载该章节小说
    downlode(title,text,url)

# 下载小说
def downlode(title,text,url):
    with open('shengmu.txt', 'a+', encoding='utf-8') as f:
        f.write(title)
        f.write(text+'\n')
    print('{} 下载完成  链接地址为 {}'.format(title,url))

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    url = 'http://www.biqukan.com/3_3039/'
    main(url)