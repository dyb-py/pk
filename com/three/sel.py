from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path=r'F:\pywork\com\three\day10\chromedriver.exe')
driver.get('http://www.baidu.com')
driver.execute_script("document.getElementById('kw').value='续馥霖'")
baidu = driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.find_element_by_xpath('/html/body/div/div[2]/div/a[3]').click()

driver.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%BB%AD%E9%A6%A5%E9%9C%96')
num=1
while num<6:
    ac = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/ul/li['+str(num)+']/div/a/img')
    ActionChains(driver).move_to_element(ac).perform()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/ul/li['+str(num)+']/div[2]/div/div/div/a[2]').click()
    num+=1
