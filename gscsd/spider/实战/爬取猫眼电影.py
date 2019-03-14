import requests
from pyquery import PyQuery as pq
import traceback

def getHtml():
    url = 'https://maoyan.com/board'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = response.text
        parseHtml(html)
    else:
        print('code is: ', response.status_code)

def parseHtml(html):
    data = pq(html)
    dd = data('dl.board-wrapper div.movie-item-info').items()
    for i in dd:
        name = i('p.name a').text()
        star = i('p.star').text().strip('')
        releasetime = i('p.releasetime').text()[5:]
        print(name, star, releasetime)

def main():
    getHtml()

if __name__ == '__main__':
    main()
