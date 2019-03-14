import requests
url = 'http://img.hb.aicdn.com/178dbee440c8bc025ff3a31f0f53816a7af647191cf67-td5UxW_fw658'
# 请求这个图片url
headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',}
response = requests.get(url,headers=headers)
# 图片的二进制响应内容
print(response.content)
# 图片编码格式
print(response.encoding)
# 打开一个文件将数据写入到文件内
with open('meinv.jpg','wb') as fd:
    # 每到128位就写入
    for chunk in response.iter_content(128):
        fd.write(chunk)