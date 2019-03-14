import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime
import json
import re
# URL = 'http://tianqi.2345.com/t/wea_history/js/54511_2011'
# u2 = 'http://tianqi.2345.com/t/wea_history/js/54511_20112.js'
# u3 = 'http://tianqi.2345.com/t/wea_history/js/54511_20113.js'
# u3 = 'http://tianqi.2345.com/t/wea_history/js/54511_20115.js'
# 2011+6 = 2011年6月份数据
# 2015年之前都是以上
# 2016年：201606这种情况
# 2016 2月后变了
def main():
    UrlList = []
    now = datetime.datetime.now()
    now_year = now.strftime('%Y')
    now_month = now.strftime('%m')
    for year in range(2011,int(now_year)+1):
        if year < 2016:
            for month in range(1,13):
                url = 'http://tianqi.2345.com/t/wea_history/js/54511_{}{}.js'.format(year,month)
                UrlList.append(url)
        elif year >= 2016 and year < int(now_year):
            for month in range(1, 13):
                if year == 2016 and month < 3:
                        url = 'http://tianqi.2345.com/t/wea_history/js/54511_{}{}.js'.format(year,month)
                        UrlList.append(url)
                else:
                    if len(str(month)) == 1:
                        month = '0'+ str(month)
                    time1 = str(year) + str(month)
                    url = 'http://tianqi.2345.com/t/wea_history/js/{}/54511_{}{}.js'.format(time1,year,month)
                    UrlList.append(url)
        elif year == int(now_year):
            for month in range(1,int(now_month)+1):
                if len(str(month)) == 1:
                    month = '0'+ str(month)
                time1 = str(year) + str(month)
                url = 'http://tianqi.2345.com/t/wea_history/js/{}/54511_{}{}.js'.format(time1, year, month)
                UrlList.append(url)
    return UrlList

def parse_url(urlList):
    print('parse----url')
    # 禁用服务器缓存
    ua = UserAgent()
    for url in urlList[:1]:
        headers = {
            'User-Agent': ua.random
        }
        print(url)
        response = requests.get(url,headers=headers)
        data_text = response.text
        re_data = re.compile('{.*}')
        str_data = re.findall(re_data,data_text)[0]

        re_city = re.findall('city:(.*?),', str_data)[0].strip("'")
        every_date1 = re.findall('tqInfo:\[(.*)]', str_data)[0]
        every_date2 = every_date1.rstrip('{}').rstrip(',')
        every_date3 = re.findall('{.*?}', every_date2)
        datalist = []
        for every in every_date3:
            everyData = every.strip('{}').split(',')
            # print('every----', everyData)
            dalist = []
            for eve in everyData:
                da = eve.replace("'", '').split(':')  # "ymd:'2011-01-01'",
                dalist.append(da[1])
            print('-----',dalist)
            datalist.append(dalist)
        # print(datalist)



if __name__ == '__main__':
    UrlList = main()
    parse_url(UrlList)


# parse----url
# http://tianqi.2345.com/t/wea_history/js/54511_20111.js
# ----- ['2011-01-01', '-2℃', '-7℃', '多云~阴', '无持续风向', '微风']
# ----- ['2011-01-02', '-2℃', '-7℃', '多云', '无持续风向', '微风']
# ----- ['2011-01-03', '-2℃', '-6℃', '多云~阴', '西北风~北风', '3-4级~4-5级']
# ----- ['2011-01-04', '-2℃', '-9℃', '晴', '北风', '5-6级']
# ----- ['2011-01-05', '-2℃', '-10℃', '晴', '北风~无持续风向', '3-4级~微风']
# ----- ['2011-01-06', '-1℃', '-10℃', '晴~多云', '无持续风向', '微风']
# ----- ['2011-01-07', '-1℃', '-9℃', '多云', '无持续风向~北风', '微风~3-4级']
# ----- ['2011-01-08', '0℃', '-9℃', '晴', '无持续风向', '微风']
# ----- ['2011-01-09', '0℃', '-9℃', '晴', '无持续风向', '微风']
# ----- ['2011-01-10', '0℃', '-9℃', '晴', '无持续风向', '微风']
# ----- ['2011-01-11', '-1℃', '-9℃', '晴~多云', '无持续风向', '微风']
# ----- ['2011-01-12', '-1℃', '-8℃', '多云~晴', '北风', '3-4级']
# ----- ['2011-01-13', '-1℃', '-9℃', '多云', '无持续风向~北风', '微风~3-4级']
# ----- ['2011-01-14', '-2℃', '-10℃', '晴', '无持续风向', '微风']
# ----- ['2011-01-15', '-2℃', '-9℃', '晴~多云', '无持续风向', '微风']
# ----- ['2011-01-16', '-1℃', '-9℃', '阴~晴', '无持续风向', '微风']
# ----- ['2011-01-26', '0℃', '-8℃', '晴', '无持续风向', '微风']
# ----- ['2011-01-29', '-1℃', '-10℃', '晴', '无持续风向', '微风']
# ----- ['2011-01-30', '3℃', '-7℃', '晴', '无持续风向', '微风']
# ----- ['2011-01-31', '7℃', '-7℃', '晴', '无持续风向', '微风']