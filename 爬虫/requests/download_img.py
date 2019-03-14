import requests
url = 'http://img.hb.aicdn.com/494d7bb95fd7338882b009beec454413f168726910c65-e7di7o_fw658'
# 请求这个图片url
headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',}

# 打开一个文件将数据写入到文件内
from contextlib import closing
with closing(requests.get(url,headers=headers)) as response:
    with open('tangyan.jpg','wb') as fd:
        # 每到128位就写入
        for chunk in response.iter_content(128):
            fd.write(chunk)