# find_element_by_id   通过定位id来定位元素
# find_element_by_tag_name  通过标签名来定位元素
from selenium import webdriver
driver = webdriver.Firefox()
for i in range(10):
    driver.get("https://www.baidu.com")
    try:
        # 就是判断id为su的是否在这个网页中，在的话输出print中的语句
        driver.find_element_by_id('su')
        print('test pass: ID found')
    except Exception as e:
        print(e)
    # 关闭浏览器
    driver.quit()