#   coding=utf-8
#   auth-lz
from selenium import webdriver
print('导入webdriver包')
pcc = webdriver.Chrome()
print('打开浏览器')
pcc.get("http://www.baidu.com")
print('进入百度')

