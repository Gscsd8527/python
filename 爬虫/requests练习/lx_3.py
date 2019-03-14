import requests
r = requests.get(url='https://www.baidu.com/')  # 最基本的GET请求
print(r.status_code)  # 获取返回状态
r = requests.get(url='https://www.baidu.com/', params={'name': '流水无情','age':20})  # 带参数的GET请求
r1 = requests.get(url='https://www.baidu.com/', params={'name': 'tan','age':[20,21,22]})
print(r.url)
print(r1.url)
print(r.text)  # 打印解码后的返回数据