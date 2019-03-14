# 定位元素后给他个点击事件
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
try:
    # 会点击这个 把百度设为主页 这个链接
    driver.find_element_by_partial_link_text('把百度设为主页').click()
    print('test pass: element found by partial link text')
except Exception as e:
    print('Exception found'.format(e))
# 关闭浏览
driver.quit()