import requests
from bs4 import BeautifulSoup
import pymysql
import time
import aiohttp
import asyncio

# 解析网页
async def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find(class_='sons').find_all(class_='cont')
    for dt in data:
        jueju = dt.find_all('a')[0].text
        name_gushi_str = dt.find_all('a')[1].text
        name_gushi = name_gushi_str.split('《')
        name = name_gushi[0]
        gushi = name_gushi[1][:-1]
        print(name, gushi, jueju)

# 获取网页（文本信息）
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def download(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        await parse(html)

if __name__ == '__main__':
    # 得到200条页面链接
    url_list = ['https://so.gushiwen.org/mingju/default.aspx?p=%s&c=&t=' % i for i in range(1, 200)]
    # 开始时间
    start_time = time.time()

    # 利用asyncio模块进行异步IO处理
    loop = asyncio.get_event_loop()  # 创建了一个事件循环 loop
    tasks = [asyncio.ensure_future(download(url)) for url in url_list]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)
    # 解析每条url数据
    parse(url_list)
    # 结束时间
    end_time = time.time()
    # 花费时间
    spend_time = end_time - start_time
    print('一共花费  %s  ' % spend_time)
