import requests
#获取该网页的源代码
response = requests.get('http://news.baidu.com/')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)