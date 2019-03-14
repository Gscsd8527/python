import requests
response = requests.get('http://httpbin.org/get?name=germay&age=22')
print(response.text)