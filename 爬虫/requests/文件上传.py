import requests
files = {'file':open('facicon.jco','rb')}
response = requests.post('http://httpbin.org/post',files=files)
print(response.text)