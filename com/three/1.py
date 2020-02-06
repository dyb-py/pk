from urllib import request
# # url = "http://www.renren.com/973157040/newsfeed/photo"
# # headers ={
# #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
# #     'Cookie':'anonymid=k4jmqr8wui5sw3; depovince=GW; _r01_=1; JSESSIONID=abcabnaH19wIXhN2Kg38w; ick_login=93321da4-4c07-4875-a2d5-f4741dbef353; t=501bae14f9c0b46106479522364ad50e0; societyguester=501bae14f9c0b46106479522364ad50e0; id=973157040; xnsid=c8e18a76; jebecookies=3cc4eccd-eff4-410c-968d-e5ab12ac99f3|||||; jebe_key=699783ff-6492-4d17-ad0d-bea81c506a47%7C3b4de587ed19404794b9b60d2772f8c9%7C1577177742662%7C1%7C1577177742016; jebe_key=699783ff-6492-4d17-ad0d-bea81c506a47%7C3b4de587ed19404794b9b60d2772f8c9%7C1577177742662%7C1%7C1577177742017; ver=7.0; loginfrom=null; wp_fold=0'
# # }
# # req=request.Request(url,headers=headers)
# # res = request.urlopen(req).read().decode()
# # print(res)

# from urllib import request
# from http.cookiejar import CookieJar
# cookiejar = CookieJar() # 保存的是response cookie
# handler = request.HTTPCookieProcessor(cookiejar)  # cookie handler
# print(cookiejar)
# opener = request.build_opener(handler)
# url = "http://www.renren.com/972685182"
# res = opener.open(url).read().decode()
# # print(res)
# print(cookiejar)

# url = "http://www.httpbin.org/ip"
# proxy = {'HTTP': '223.199.16.78:9999'}
# handler = request.ProxyHandler(proxy) # 构建一个代理handler
# opener = request.build_opener(handler)
# res2 = opener.open(url).read()
# print(proxy,res2)
import requests
# ip={'http': '223.85.196.75:9797'}
# url='http://httpbin.org/ip'
# res=requests.get(url,proxies=ip,timeout=5).text
# # if str(ip) in str(res):
# #     print('1111')
# print(res)
# #{'http': '175.154.115.90:9999'}

import json

# import multiprocessing,time
# def fun(n):
#     print(n,'睡'+str(n)+'s')
#     time.sleep(n)
#
# if __name__ == '__main__':
#     pool=multiprocessing.Pool(3)
#     for i in range(10):
#         pool.apply_async(func=fun,args=(i,))
#
#     pool.close()
#     pool.join()
#     print('end')
# from lxml import etree
#
# url='https://bj.zu.ke.com/zufang/pg2/#contentList'
# headers ={
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
# }
# res = requests.get(url).text
# ele = etree.HTML(res)
# url = ele.xpath('//div[@class="content__list--item--main"]//p[@class="content__list--item--title twoline"]/a/@href')
# name = ele.xpath('//div[@class="content__list--item--main"]//p[@class="content__list--item--title twoline"]/a/text()')
# money = ele.xpath('//div[@class="content__list--item--main"]/span/em/text()')
# for i in url:
#     # print(i,type(i))
#     print(i)
#     print(name[url.index(i)].strip())
#     # print(address[url.index(i)])
#     print(money[url.index(i)].strip())

# u = '中文' #指定字符串类型对象u
# str = u.encode('gb2312') #以gb2312编码对u进行编码，获得bytes类型对象str
# u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，获得字符串类型对象u1
# # u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的字符串内容
# print(str)
# print(u1)
# s=u1.encode()
# s1=s.decode()
# print(s,s1)
# print(u2)


import jieba
import wordcloud
url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_1412551543'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'referer':'https://music.163.com/song?id=1412551543',
    'cookie': 'JSESSIONID-WYYY=gnavGiivnvnEu833y8aPgydDjbcqgMGoalDs9Sr%2BN2FUweArbcyiQwMhwqchub7EcpDSIFvwX%2FEJnGt5%5CxrW%2BKAgp%5CsGhc%2F0B8CFRo%2BwDsOCifXGTN1JqKCe0aqe%5ChQNrH1oNQz8sfrHnFH5q6HAKvefh4eq0wUiIKg%2BDXKaKziShWy8%3A1578553112727; _iuqxldmzr_=32; _ntes_nnid=fba360019a69867505d5c73c510f4fc7,1578551312805; _ntes_nuid=fba360019a69867505d5c73c510f4fc7; WM_NI=bboe%2FbsX9%2FpEBDnISlolawjekEpalicN95hwjKHijSkBh5OBsAffS%2FDaAl%2Fpf8ojSD1b7%2FXYRRDBCAuzLwL00t%2FwGdwRefT7I1w8%2FDMO%2B5AoidEjX1MRSLP0RvdoqMYrYVo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89b380909e97a8e261b4b48bb3d54b869b8f84f33eb8999a96f14182adc0bae62af0fea7c3b92aa2bea186ae6ab188f7d0f34f829ca2aad268adb4af98e96fa99bc082ef63a192f7d6eb7daa95888ae959a99ea8d6ce4ab19faa87d22588bf8f8dae7ca6e8a18bd250f3bef9d0db53928e8ca3c24bb7a68498cf3cf4ace198c670b58eab87d73d8befb9d9ae508f91e5d6c465abbc8b8bdb3b8f8e9dadd33c92aaac90f4479bae97b7ee37e2a3; WM_TID=q%2FY%2BRryNXkZAFQFBAEYp6oCVuueQs4I0'
}
data = {
'params': 'lpFyMcdtcPmSgA4NfDnfPXx1CRS9ThT6XYup3L+Qqp9wQkcQGEFllkH0JVT3m4CxDe4C6xRdG9X4BBr/9pHS+r9vZB5vQKBu0tdP5fM6cny4q04z/wDoO0IOPnnWOj7ItoItCVX+VYdRG4/Q8MIRAKuZEojb5A79t315cQhFhpBkKvZ52g80eTPE+cZFhleY',
'encSecKey': 'a62906ea49eabf3ba17ced7f3315ad2cf5cba2611e45df3fcb557c9b0b4305600b9f179f49d0a530d616cb31171dc3ec81dc9ab1acd69ea440a763937e43a52d88dbfb720b3a4939f9e8bf21edbeeda9599ba9928e30caf8cf61d7174e991167cbbb8ce139ae494e190d828c44f23bd8c7f05d3dd7a4b65660a6221631292c22'
}
data1 = {
'params': 'EzdWjqr6eTChZ4iuYT/hVugDkFkCqNPCUN6Yv68lX5JoQmtRjYEFSZtXnBrcLnmfyUuScgmyjqp1qH3P70cjI9L3LJ/FwePjvm62qF9hATogQ6cx//HM7oQluSQ5AvTHLHMJZtfb1CIkUieIB9M+G8o2H7VKY7C1qaTZDh+grfuxfQDG1GCqWVOsedt0DvwF',
'encSecKey': 'de415fefe94196c75a443e0159e4bc750e0e8e88a3197551c24453738cb9b07533dd355b39608274559081fa4f98665bd48cfbfa47f1b30fc939c202910f6b99a6f12c33369898a214d9793bd2e91fd34563a51b059816f26d8e07afa1488de2d96571330a45d5c49eebae93b474f6fd258f443921c96938d7fdc43b293ffa93'
}
res = requests.get(url,headers=headers)
print(res.text)
# res = res.json()
# for i in res['comments']:
#     print(i['content'])