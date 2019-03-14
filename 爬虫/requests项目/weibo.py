import requests
from bs4 import BeautifulSoup
import json
headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',}
url = 'https://www.toutiao.com/api/pc/focus/'
response = requests.get(url).text
data = json.loads(response)
news = data['data']['pc_feed_focus']
for i in news:
    title = i['title']
    img_url = i['image_url']
    url  = i['media_url']
    print(title,img_url,url)