# from urllib import request
# # import re
# # from com.two.dyb作业.dyb_10_23.mysqltools import MySqlTools
# # import MySQLdb
# # num=0
# # url='https://movie.douban.com/top250?start='+str(num)+'&filter='
# # def getname(url):
# #     t=request.urlopen(url)
# #     html=t.read().decode('utf-8')
# #     rule='<span class=("title"|"other")>(.+)</span>'
# #     text_cp=re.compile(rule)
# #     url1=text_cp.findall(html)
# #     return url1
# # tool=MySqlTools.get_tool()
# # num=0
# # while num<230:
# #     url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
# #     url1 = getname(url)
# #     for i in url1:
# #         name = i[1].replace('&nbsp;/&nbsp;', '')
# #         print(name)
# #         # sql = "insert into movie(name)values(%s) "
# #         tool.add('movie',name)
# #     num += 25
