# 导包：webdriver，网页驱动
from selenium import webdriver
import time
import jieba
import wordcloud

# 创建一个driver对象，声明该对象使用的是谷歌浏览器的驱动
driver = webdriver.Chrome(executable_path=r'E:\Python186共享文件夹\第三阶段\代码\day10\chromedriver.exe')
# 相当于在浏览器的地址栏输入"http://www.baidu.com"，并且将浏览器页面进行展示
driver.get('https://music.163.com/#/song?id=561493928')
# 对driver对象进行操作
# driver.switch_to_frame('g_iframe')
# 切换当前页面的iframe，iframe：html里面可以嵌套一个html，数据可能在另一个html中，所以需要切换
driver.switch_to.frame('g_iframe')
# 可以选择当前页面的元素：选择方式有：
    # xpath、classname、CSS、id等等
    # 获得到的是selenium的webdelement对象，可以对该对象调用text方法，显示数据
while True:
    # 需要等待一段时间，让页面加载完毕，再对页面进行解析
    time.sleep(3)
    # 执行JS代码，让页面向下滑动1000个单位
    driver.execute_script('var q=document.documentElement.scrollTpo=1000')
    # 使用xpath选择器，获取评论的元素
    data = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]//div/div[2]/div[1]/div')
    print(data)
    commont = ''
    for i in data:
        commont_str = i.text
        s = jieba.cut(commont_str.split('：')[1])
        for j in s:
            commont += j+','
    print(commont)
    with open('wyyyy.txt','a',encoding='utf-8') as w:
        w.write(commont)
    # 点击事件
    # 使用link_text选择器获取到下一页按钮的元素
    b = driver.find_element_by_link_text('下一页')

    print(b.text)
    # 运行js代码，点击下一页，获得下一页数据。
    driver.execute_script("arguments[0].click();", b)

