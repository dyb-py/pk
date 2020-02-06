import requests
from bs4 import BeautifulSoup
url=r'http://www.yuetutu.com/cbook_22797/4.html'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
print(type(soup))
# print(soup.find_all('a',))
t=soup.find_all('div',{'id':'content'})[0]
t.text.replace('\xa0'*4,'\n')

