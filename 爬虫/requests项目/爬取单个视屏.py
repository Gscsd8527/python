import requests
import datetime
url = 'https://201806.53didi.com/20180621/2/1/xml/91_211f47127b2a4fe9acdc59cfa168e9bc.mp4'
url='https://201806.53didi.com/20180624/13/1/xml/91_f721bc15150c4ee5e920bd5d47264080.mp4'
url='https://201712mp4.89soso.com/20180618/13/1/xml/91_c9b222271e4b42a1da7d6ac3a42ae677.mp4'
# 请求要下载的url地址
html = requests.get(url)
# content返回的是bytes型也就是二进制的数据。
html = html.content
start_time = datetime.datetime.now()
print('开始输出时间{}'.format(start_time))
print(html)
start_down_time = datetime.datetime.now()
print('开始下载时间{}'.format(start_down_time))
with open('G:/my1.mp4','wb') as f:
    f.write(html)
end_time = datetime.datetime.now()
print('下载结束时间{}'.format(end_time))


