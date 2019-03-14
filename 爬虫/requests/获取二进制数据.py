import requests
response = requests.get('http://github.com/favicon.lco')
print(type(response.text),type(response.content))
print(response.text)
print(response.content)