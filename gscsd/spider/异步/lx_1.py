import requests
from bs4 import BeautifulSoup
import pymysql
import time

def parse(urls):
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            data = soup.find(class_='sons').find_all(class_='cont')
            for dt in data:
                jueju = dt.find_all('a')[0].text
                name_gushi_str = dt.find_all('a')[1].text
                name_gushi = name_gushi_str.split('《')
                name = name_gushi[0]
                gushi = name_gushi[1][:-1]
                print(name, gushi, jueju)
                down_mysql(name, gushi, jueju)
        else:
            code = response.status_code
            print('请求出错,响应： %d' % code)

# 调用mysql数据库
class down_mysql_model:
    def __init__(self, name, gushi, jueju):
        self.name = name
        self.gushi = gushi
        self.jueju = jueju
        self.connect = pymysql.connect(
            host='localhost',
            db='test_one',
            port=3306,
            user='root',
            passwd='123456',
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()
    # 保存数据到MySQL中
    def save_mysql(self):
        sql = "insert into gs(`name`, gushi, jueju) VALUES (%s,%s,%s)"
        try:
            self.cursor.execute(sql, (self.name, self.gushi, self.jueju))
            self.connect.commit()
            print('数据插入成功')
        except Exception as e:
            self.connect.rollback()
            print('数据插入错误', e)

def down_mysql(name, gushi, jueju):
    down = down_mysql_model(name, gushi, jueju)
    down.save_mysql()

if __name__ == '__main__':
    # 得到200条页面链接
    url_list = ['https://so.gushiwen.org/mingju/default.aspx?p=%s&c=&t=' % i for i in range(1, 200)]
    # 开始时间
    start_time = time.time()
    # 解析每条url数据
    parse(url_list)
    # 结束时间
    end_time = time.time()
    # 花费时间
    spend_time = end_time - start_time
    print('一共花费  %s  ' % spend_time)
# 一共花费  160.33977913856506  