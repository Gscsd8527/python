import requests
import random
import telnetlib
proxies = [
        {'http': 'http://61.224.163.185:8080'},
        {'http': 'http://219.76.245.230:3128'},
        {'http': 'http://122.138.171.43:8118'},
        {'http': 'http://112.226.195.232:8118'},
]
response = requests.get('https://www.taobao.com',proxies=random.choice(proxies))
print(response.status_code)
print(response)
try:
    print('=====')
    telnetlib.Telnet('61.224.163.185','8080',timeout=20)
except:
    print('connect failed')
else:
    print('success')