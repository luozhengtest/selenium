#   coding:utf-8
#   auth:@lz
from selenium import webdriver
# from  import导入的包可以直接使用其中的方法   .get（）
import time
# import导入的包调用时需要使用包名.方法的形式     time.sleep(1)
pcc = webdriver.Chrome() #打开浏览器
pcc.get("http://mail.163.com") #使用打开的浏览器打开百度
pcc.implicitly_wait(100) #等待1s
pcc.find_element_by_id('switchAccountLogin').click()
pcc.implicitly_wait(1)
a = pcc.find_elements_by_tag_name('iframe')
for i in a :
    print (i)
pcc.switch_to.frame('cnt-box-parent')
pcc.find_element_by_name('email').send_keys('ces')   #找到元素，执行操作
'''
find_element_by 为查找元素的方法，常用的有name/id/classname/link_test等等，元素定位方法列表：
find_element_b_id()  通过ID标签查找元素
find_element_by_name()   通过name标签查找元素
find_element_by_class_name()    通过class标签查找元素
find_element_by_tag_name()   通过tag标签查找元素
    tag标签：结构：* html* head* body* div* span 
    Meta Information：* DOCTYPE* title* link* meta* style 
    文字：* p* h1, h2, h3, h4, h5, h6* strong* em* abbr* acronym* address* bdo* blockquote* cite* q* code* ins* del* dfn* kbd* pre* samp* var* br 
    连接：* a* base 图片、对象：* img* area* map* object* param 
    列表：* ul* ol* li* dl* dt* dd 
    表格：* table* tr* td* th* tbody* thead* tfoot* col* colgroup* caption 
    表单：* form* input* textarea* select* option* optgroup* button* label* fieldset* legend 
    脚本：* script* noscript 
    文字修饰：* b, i, tt, sub, sup, big, small, hr
find_element_by_link_text()  按照链接显示的文本精确定位元素
find_element_by_partial_link_text()  按照链接显示的文本模糊定位元素
find_element_by_xpath()  按照xpath路径定位元素
find_element_by_css_selector()   按照css标签定位元素

    
.send_keys 为找到元素后执行的操作，常用的有.send_keys() .cilck()等，执行的操作事件列表：
    .text   输出定位的元素的说明
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

定位一组元素
    .find_elements
    pcc.find_elements_by_css_selector('h3.t>a')
    h3为标签   t为class a为 href
    确认所取的值正确
    for i in pcc
        print i.get_attribute('href')

等待函数
    time.sleep(1)   #从time包中导入的方法，使用后，等待1s后执行后面的操作
    pcc.implicitly_wait(10) #webdriver自带的方法，使用后，等待10s
        如果10s内能找到了后面的元素，则直接开始下面的步骤

定位一组随机函数
    import random
    ran = random.randint(0,9) #随机取一个0-9的整数
    print (ran) #打印取的随机数
    #随机获取一个结果的URL地址
        Urls = pcc.find_elements_by_css_selector('h3.t>a')
        ran = random.randint(0,9)
        urlone = Urls[ran].get_attribute('href')
        Urls[ran].click()   #随机取一个url点击
释放iframe（回到主界面）
    .switch_to_default_content()
    
二次定位
    pcc.find_element_by_id('kw').find_element_by_xpath("//option[@value='50']").click
    ActionChains方法列表
        click(on_element=None) ——单击鼠标左键

        click_and_hold(on_element=None) ——点击鼠标左键，不松开

        context_click(on_element=None) ——点击鼠标右键

        double_click(on_element=None) ——双击鼠标左键

        drag_and_drop(source, target) ——拖拽到某个元素然后松开

        drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

        key_down(value, element=None) ——按下某个键盘上的键

        key_up(value, element=None) ——松开某个键

        move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标

        move_to_element(to_element) ——鼠标移动到某个元素

        move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置

        perform() ——执行链中的所有动作

        release(on_element=None) ——在某个元素位置松开鼠标左键

        send_keys(*keys_to_send) ——发送某个键到当前焦点的元素

        send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素 
'''

