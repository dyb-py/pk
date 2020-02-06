import requests
from urllib import request
# url = "http://www.httpbin.org/cookies/set/ni/wo"
# s = requests.Session() # 保存的是自动登录的cookie,前后的session对象保存的是同一个cookie
# res1 = s.get(url)
# print(res1.text)
# res2 = s.get(url).text
# print(res2)
url = "http://www.iqianyue.com/login"
# p = {"http":"123.139.56.238:9999"}
with requests.session() as s:
    res = s.post(url=url,data={"number":"123","passwd":"123","submit":""})  # 第一次发送post请求，请求成功之后，session里面就存储了自动登陆的cookie
    print(res.text)
    res1=s.get(url='https://www.iqianyue.com/userindex')  # 第二次发送请求的时候，就携带了cookie登录
    print(res1.text)

#
# headers = {"User-Agent":"wangdachui","love":"xiaomei"}
# s = requests.Session()
# s.headers=headers
# print(s.get("http://www.httpbin.org/headers").text)
# print(s.get("http://www.httpbin.org/headers").text)







