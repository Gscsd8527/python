import random
import requests
def agent():
    age = [
        { 'https': 'https://106.75.71.122:80'},
        { 'https': 'https://221.228.17.172:8181'},
        { 'http': 'http://219.141.153.3:80'},
        { 'http': 'http://61.135.217.7:80'},
        { 'http': 'http://118.190.95.43:9001'},
        { 'http': 'http://219.141.153.40:80'},
        { 'http': 'http://111.155.116.249:8123'},
        { 'http': 'http://61.135.217.7:80'},
        { 'http': 'http://221.228.17.172:8181'},
        { 'http': 'http://112.95.191.17:9797'},
        { 'httsp': 'https://218.60.8.98:3129'},
        { 'https': 'https://203.130.46.108:9090'},
        { 'https': 'https://218.86.87.171:53281'},
        { 'https': 'https://221.228.17.172:8181'},
        { 'https': 'https://58.48.193.180:3128'},
        { 'https': 'https://218.60.8.83:3129'},
        { 'https': 'https://218.60.8.98:3129'},
        { 'https': 'https://203.130.46.108:9090'},
        { 'http':  'http://112.95.191.17:9797'},
        { 'http': 'http://61.135.217.7:80'},
        { 'http': 'http://118.190.95.43:9001'},
    ]
    return age

def parse(url,headers):
    age = agent()
    try:
        response = requests.get(url,headers=headers,proxies=random.choice(age))
        if response.status_code == 200:
            response.encoding = 'utf-8'
            print('------')
            return response.status_code
        else:
            while True:
                pro = agent()
                response = requests.get(url, headers=headers, proxies=random.choice(age))
                if response.status_code == 200:
                    response.encoding = 'utf-8'
                    print('========')
                    return response.status_code
    except:
        print('IP 已过期')
if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    a=parse(url,headers)
    print(a)