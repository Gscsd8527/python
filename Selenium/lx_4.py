# 通过class属性来定位元素的

from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
try:
    driver.find_element_by_class_name('s_ipt')
    print('test pass: element found by class name')
except Exception as e:
    print('Exception found',format(e))
# driver.quit()