# coding=utf-8
# auth@luozhengtest
from selenium import webdriver
from selenium.webdriver.common.by import By
pccmini = webdriver.Chrome()
pccmini.get('http://www.baidu.com')
a = pccmini.find_element('link text','hao123').text
print (a)
class lest() :
    def test(a,b):
        print (a,b)
        if a != b :
            return '请输入数字'
        return a + b
c = lest.test(2,2)
print (c)