import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.diediaow.com/'
headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',}
html = requests.get(url=url,headers=headers)
# 编码格式设置为utf-8
html.encoding='utf-8'
html = html.text
soup = BeautifulSoup(html,'lxml')
# 循环li
img = soup.select('div.row-l ul.clearfix li')
print(len(img))
a=1
for i in img:
    # 得到img标签，因为得到的是一个列表，所以取第一位
    ig = i.select('a div.img img')[0]
    # 得到img标签的img链接地址，这个标签里面也放了url，当然也可以获取src的url
    img_url = ig.get('data-original')
    # 得到的链接有的格式不正确，所以筛选一下看是否是str类型
    if isinstance(img_url,str):
        print(img_url)
        # 得到图片
        response = requests.get(img_url)
        # 将图片放入G盘的img文件夹下，并给每一张图片命名
        with open('G:/img/'+'a'+str(a)+'.jpg','wb') as fd:
            # 以128字节写入
            for chunk in response.iter_content(128):
                fd.write(chunk)
        a+=1

