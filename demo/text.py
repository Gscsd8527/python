# coding = utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://docs.djangoproject.com/en/2.0/')
print(driver.title)
print(driver.name)
print(driver.log_types)
driver.quit()
