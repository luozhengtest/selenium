#   coding=utf-8
#   auth-lz
from selenium import webdriver
# from  import导入的包可以直接使用其中的方法   .get（）
import time
# import导入的包调用时需要使用包名.方法的形式     time.sleep(1)
pcc = webdriver.Chrome() #打开浏览器
pcc.get("http://www.baidu.com") #使用打开的浏览器打开百度
time.sleep(1) #等待1s
pcc.find_element_by_id('kw').send_keys('ces')   #找到元素，执行操作
'''
find_enlement_by 为查找元素的方法，常用的有name/id/classname/link_test等等，元素定位方法列表：
find_enlement_b_id()  通过ID标签查找元素
find_enlement_by_name()   通过name标签查找元素
find_enlement_by_class_name()    通过class标签查找元素
find_enlement_by_tag_name()   通过tag标签查找元素
    tag标签：结构：* html* head* body* div* span 
    Meta Information：* DOCTYPE* title* link* meta* style 
    文字：* p* h1, h2, h3, h4, h5, h6* strong* em* abbr* acronym* address* bdo* blockquote* cite* q* code* ins* del* dfn* kbd* pre* samp* var* br 
    连接：* a* base 图片、对象：* img* area* map* object* param 
    列表：* ul* ol* li* dl* dt* dd 
    表格：* table* tr* td* th* tbody* thead* tfoot* col* colgroup* caption 
    表单：* form* input* textarea* select* option* optgroup* button* label* fieldset* legend 
    脚本：* script* noscript 
    文字修饰：* b, i, tt, sub, sup, big, small, hr
find_enlement_by_link_text()  按照链接显示的文本精确定位元素
find_enlement_by_partial_link_text()  按照链接显示的文本模糊定位元素
find_enlement_by_xpath()  按照xpath路径定位元素
find_enlement_by_css_selector()   按照css标签定位元素

    
.send_keys 为找到元素后执行的操作，常用的有.send_keys() .cilck()等，执行的操作事件列表：
    .click()    左键点击
    .clear（）    清空输入
    .send_keys()    输入字符串
        若是发送中文.send_keys(n'中文')
    .submit()   提交表单（回车）
若上面的事件不能满足，则需要导入专用的键盘模拟事件包
from selenium.webdriver.common.keys import Keys
包中包含的模拟事件：
    .send_keys(Keys.F1) 发送F1-F12，需要改成对应的Fx
    .send_keys(Keys.CONTROL,'c')    复制ctrl+c
    .send_keys(Keys.CONTROL,'v')    粘贴ctrl+v
    .send_keys(Keys.CONTROL,'a')    全选ctrl+a
    .send_keys(Keys.CONTROL,'x')    剪切ctrl+c
    .send_keys(Keys.TAB)    制表符tab
    其他事件请参考说明文档
鼠标模拟事件包
from selenium.webdriver.common.action_chains import ActionChains
包含的鼠标事件：
    perform()   执行所有ActionChains中的行为
    move_to_element() 鼠标悬停
    context_click() 右击鼠标
    double_click()  双击鼠标（左键）
    其他事件请参考说明文档
多窗口
driver.current_window_handle获取当前句柄
pcchad = driver.current_window_handle
print（'pcchad'）打印句柄
window_handles  获取所有句柄
pccwindow = window_handles
切换页面，方式一：
    for i in pccwindws ：
        if i != pcchad
            pcc.switch_to_window(i)
    print(pcc.title)  打印界面的title
    pcc.find.element_by_name('kw')
切换页面，方式二：
    pcc.switch_to_window(pccwindow[1])
    print（pcc.title）    打印界面的title
    close() 关闭窗口
    quit（）  退出进程
    
    
'''

