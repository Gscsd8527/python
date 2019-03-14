import requests
from pyquery import PyQuery as pq


def getUrl():
    start_url = 'https://www.toutiao.com/search_content/?offset={}&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'
    url_list = [start_url.format(i) for i in range(0, 100, 20)]
    for url in url_list:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']
            for dt in data:
                try:
                    title = dt['title']
                    print(title)
                except:
                    pass
        print('-----------------------------')

def main():
    getUrl()

if __name__ == '__main__':
    main()
