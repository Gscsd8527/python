from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

def main():
    # 获取链接
    driver.get('https://booking.1hai.cn/?from=Nav&IsBatch=false')
    driver.find_element_by_xpath('//*[@id="PickupCity"]').click()
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="ydcityBox"]/ul/li[1]/div/dl/dd[2]/span')).perform()
    driver.find_element_by_xpath('//*[@id="ydcityBox"]/ul/li[1]/div/dl/dd[2]/span').click()
    driver.find_element_by_xpath('//*[@id="getStore"]').click()
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="ydkBox"]/div[2]/ul/li[1]/div[1]/dl/dd[2]/span/em')).perform()
    driver.find_element_by_xpath('//*[@id="ydkBox"]/div[2]/ul/li[1]/div[1]/dl/dd[2]/span/em').click()
    driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

    content = driver.find_element_by_xpath('//*[@id="carTypeList"]').get_attribute('outerHTML')
    parse(content)

def parse(html):
    print(html)
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all('div', class_='wraplist')[0].find_all('div', class_='det-carlist')  # [0].find_all('ul')
    datalist = []  # 筛选出包含价格的车辆
    for i in data:
        if 'style' in i.attrs:
            datalist.append(i)
    for i in datalist:
        carname = i.find_all('ul', class_='clearfix')[0].find_all('li', class_='licar-name')[0].find_all('span')[0].text  # 上汽大通G10
        carintroinfo = i.find_all('ul', class_='clearfix')[0].find_all('li', class_='licar-name')[0].find_all('p',class_='car-introinfo')[0].find_all('span')[0].text  # MPV|自动
        parse = i.find_all('p', class_='condition1')[0].find_all('span', {'class': {'typebtn', 'btntop1'}})[0]
        aTab = parse.find_all('a')  # 一日租价 a标签的个数
        if len(aTab) == 3:
            flashRentParse = ''  # 无闪租价
            oneDayParse = aTab[0].find_all('em', class_='total-price')[0].text.strip('')  # 门店现付
            returnParse = aTab[1].find_all('em', class_='total-price')[0].text.strip('')  # 返现价
            payMentParse = aTab[2].find_all('em', class_='total-price')[0].text.strip('')  # 在线预付
        if len(aTab) == 4:
            flashRentParse = aTab[0].find_all('em', class_='total-price')[0].text.strip('')  # 闪租价
            oneDayParse = aTab[1].find_all('em', class_='total-price')[0].text.strip('')  # 门店现付
            returnParse = aTab[2].find_all('em', class_='total-price')[0].text.strip('')  # 返现价
            payMentParse = aTab[3].find_all('em', class_='total-price')[0].text.strip('')  # 在线预付
        print(carname, carintroinfo, flashRentParse, oneDayParse, returnParse, payMentParse)

if __name__ == '__main__':
    # 生成驱动对象，使用的浏览器为火狐
    driver = webdriver.Firefox()
    main()
