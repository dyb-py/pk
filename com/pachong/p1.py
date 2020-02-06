# from bs4 import BeautifulSoup
# import requests
# def A(url):
#     r=requests.get(url)
#     soup=BeautifulSoup(r.text,'html5lib')
#     div=soup.find_all('div',id='content')[0]
#     text=div.text.replace('\xa0' * 4, '\n\n')
#     return text
#
#
# url=r'http://www.yuetutu.com/cbook_2960/'
# r=requests.get(url)
# soup=BeautifulSoup(r.text,'html.parser')
# div=soup.find_all('div',id='list')[0]
# soup2=BeautifulSoup(str(div),'html5lib')
# a=soup2.find_all('a')[8:]
# for i in a:
#     l=i.text
#     t=A(r'http://www.yuetutu.com'+i.get('href'))
#     print(l,t)


# from urllib import request
# import re
# import MySQLdb
# num=0
# url='https://movie.douban.com/top250?start='+str(num)+'&filter='
# def getname(url):
#     t=request.urlopen(url)
#     html=t.read().decode('utf-8')
#     rule='<span class=("title"|"other")>(.+)</span>'
#     text_cp=re.compile(rule)
#     url1=text_cp.findall(html)
#     return url1
# def save():
#     conn=MySQLdb.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='123456',
#         db='user',
#         charset='utf8'
#     )
#     num=0
#     cur=conn.cursor()
#     while num<230:
#         url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
#         url1 = getname(url)
#         for i in url1:
#             name = i[1].replace('&nbsp;/&nbsp;', '')
#             print(name)
#             sql = "insert into movie(name)values(%s) "
#             cur.execute(sql, (name,))
#             conn.commit()
#         num += 25
# save()
