import requests
from bs4 import BeautifulSoup
url=r'http://www.yuetutu.com/cbook_1890/'
def gett(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    s=soup.find('div',id='content')
    return s.text.replace('\xa0'*4,'\n\n')
r=requests.get(url)
s=BeautifulSoup(r.text,'html.parser')
s1=s.find_all('dd')[8:]
for i in s1:
    print(i.find('a').text)
    url1='http://www.yuetutu.com'+i.find('a').get('href')
    print(gett(url1))



