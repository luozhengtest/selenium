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

    
执行的操作事件列表：
    .text   输出定位的元素的文本说明
    pcc.title   获取页面title
    .tag_name   获取标签属性
    pcc.name    获取浏览器名称
    pcc.page_source 获取页面源码
    .get_attribute('属性')    获取标签的某个属性
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
        
select选项模块（为下拉选，单选和多选直接定位然后.click()就行了）
    注：
        1全选按钮点击
            clicks = pcc.find_elements_by_xpath("//*[@type='chechbox']")
            for i in clicks
                i.click()
        2.判断是否选中，找到选项元素.is_selected(),选中返回true，未选中返回false
    from selenium.webdriver.support.select import Select #导入select方法
    pccselect = pcc.find_element_by_id('nr')    #找到下拉选按钮
    Select(pccselect).select_by_index(2)    #选择找到的第二个选项
    Select(pccselect).select_by_value('20') #选择找到的第二个选项"<option value='20'>每页显示20条</option>"
    Select(pccselect).select_by_visible_text("每页显示20条") #选择找到的第二个选项
    select其他方法列表：
        select_by_index() :通过索引定位 
        select_by_value() :通过 value 值定位 
        select_by_visible_text() :通过文本值定位
        deselect_all()  :取消所有选项
        deselect_by_index() :取消对应的index选项
        deselect_by_value() :取消对应的value选项
        deselect_by_visible_text() :取消对应文本选项 
        first_selected_option() :返回第一个选项 
        all_selected_options() :返回所有的选项

alart/confirm/prompt弹框
    switch_to_alart()   #切换到弹框
    操作主要方法：
        alert\confirm\prompt 弹出框操作主要方法有: 
        text:获取文本值
        accept() :点击"确认"
        dismiss() :点击"取消"或者叉掉对话框
        send_keys() :输入文本值 --仅限于 prompt,在 alert 和 confirm 上没有输入 框
表格用xpath定位，若表格在iframe上，需先切换

send_keys()可以通过输入文件路径上传文件（用于input标签）
    非input标签上传文件， autoit 工具或者 SendKeys 第三方库

re非贪婪模式，用于筛选，具体用法百度
    import re
    lists = re.findall('href=\"(.*?)\"',page,re.S)
    urls = []
        for url in lists :
            if 'http' in url :
                print url
                urls.append(url)
    获取页面所有的href的地址列表,打印并获取带有http的所有url

获取cookies
    改方法一般用于打开地址之后
    pcc.get('http://www.baidu.com')
    a = pcc.get_cookies()
    print(a)    #这是未登录时的cookies，登陆后获取的为登陆成功的cookies
    a = pcc.get_cookie(name='lz')    #获取指定用户lz的cookie
    pcc.delete_cookie() #清除cookie
    pcc.delete_all_cookies()    #清除所有cookies
    注：清除cookies后，登陆状态会失效
    pcc.add_cookie(cookie_dict) #添加cookie，可用于跳过登陆,具体使用参考百度

execute_script()    #执行JS脚本

常用JS脚本
    动条回到顶部:一般浏览器：js="var q=document.getElementById('id').scrollTop=0" 
                            driver.execute_script(js)
                谷歌浏览器：js = "var q=document.body.scrollTop=0" 
                            driver.execute_script(js)
    滚动条拉到底部:一般浏览器：js="var q=document.documentElement.scrollTop=10000" 
                            driver.execute_script(js)
                谷歌浏览器：略
    元素聚焦：target = driver.find_element_by_xxxx()
            driver.execute_script("arguments[0].scrollIntoView();", target)
    可以修改 scrollTop 的值，来定位右侧滚动条的位置，0 是最上面，10000 是最底部
    scrollTo(x, y)js = "window.scrollTo(100,400);"driver.execute_script(js)
    第一个参数 x 是横向距离，第二个参数 y 是纵向距离(左右滚动条比较少见)
    scrollTo函数
        --scrollHeight 获取对象的滚动高度。
        --scrollLeft 设置或获取位于对象左边界和窗口中目前可见内容的最左端之 间的距离。
        --scrollTop 设置或获取位于对象最顶端和窗口中可见内容的最顶端之间的距 离。
        --scrollWidth 获取对象的滚动宽度。   
        #滚动到底部
        js = "window.scrollTo(0,document.body.scrollHeight)" 
        driver.execute_script(js)
        #滚动到顶部
        js = "window.scrollTo(0,0)" 
        driver.execute_script(js)
readonly 属性的日历控件
    js = document.getElementById("train_date").removeAttribute("readonly");    #清除日期只读属性
    pcc.execute_script(js)  #聚焦日期插件
    pcc.find_element_by_id('train_date').clear()    #清除已有的日期
    pcc.find_element_by_id('train_date').send_keys('2011-1-1')  #输入日期
    js_value = 'document.getElementById("train_date").value="2016-12-25"'   #定义JS修改日期脚本 
    driver.execute_script(js_value) #执行修改
        
        
        
        
        
        
        
'''

