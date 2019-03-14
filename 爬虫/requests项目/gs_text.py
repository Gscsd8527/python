import requests
from bs4 import BeautifulSoup
import json
import re
def page(url):
    # 使用get方式请求页面，并使用user-agent
    html = requests.get(url)
    # 将得到的HTML代码设置Wieutf-8格式
    html.encoding='utf-8'
    # 获取到装换格式后的HTML代码
    html=html.text
    # 使用BeautifulSoup来解析网页
    soup = BeautifulSoup(html,'lxml')
    nr = soup.select('div.left div.sons')
    for i in nr:
        name_sr_cd= i.select('div.cont p')
        # 古诗名
        gs_name = name_sr_cd[0].text
        sr_cd =name_sr_cd[1].select('a')
        # 诗人
        sr = sr_cd[0].text
        # 朝代
        cd = sr_cd[1].text
        gs = i.select('div.contson')[0]
        gs = gs.text.split()
        # 古诗
        gs = str.join(',',gs)

        # 保存数据到json文件中
        # nr = '古诗名: '+gs_name+' 朝代 '+cd+' 诗人: '+sr+' 古诗: '+gs
        gscsd = {'古诗名':gs_name,'诗人':sr,'朝代':cd ,'古诗': gs}
        print(gscsd)
        with open('gs.txt','wb+') as f:
            f.write(json.dumps(nr,ensure_ascii=False)+ '\n')
            f.close()

    # 获取到下一页
    next_page = soup.select('div.pagesright a.amore')
    next_page=next_page[0].get('href')
    next_page='https://www.gushiwen.org'+next_page
    page(next_page)# 递归调用


def main():
    page(url)

if __name__=='__main__':
    url = 'https://www.gushiwen.org/shiwen/'
    main()




