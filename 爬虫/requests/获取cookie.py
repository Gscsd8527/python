import requests
response = requests.post('http://www.baidu.com')
print(response.cookies)
for key,value in response.cookies.items():
    print(key+''+key)