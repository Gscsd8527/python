# 爬取猫眼前10名的电影
import requests
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup
def get_one_page(url):
    try:
        response =  requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern = re.compile('<h.*>')
    item =re.findall(pattern,html)
    print('-----------------------------')
    print(item)
def main():
    url = 'http://maoyan.com/board/4?'
    html = get_one_page(url)
    parse_one_page(html)
    # print(html)
    print('=========')
if __name__=='__main__':
    main()

