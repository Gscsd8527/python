from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

driver.get('http://home.baidu.com/contact.html')
#得到页面源代码
doc = driver.page_source
# 利用BeautifulSoup来解析该网页
soup = BeautifulSoup(doc,'lxml')
data = soup.find_all('p',class_='m-phone-num-line')[0].find_all('span')
print(data)
for i in data:
    print(i.text)
