from selenium import webdriver

# 通过
def main():
    driver.get('https://www.baidu.com/?tn=62095104_15_oem_dg')
    driver.find_element_by_link_text('新闻').click()
    print(driver.current_url)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    main()
