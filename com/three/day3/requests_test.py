import requests
# r = requests.get('https://www.python.org')
# print(r.content)
# print(b'Python is a programming language' in r.content)
# payload = {
#     "key2": "value2",
#     "key1": "value1"
# }
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.content.decode())
# url = "https://httpbin.org/headers"
#
# headers = {
#     "User-Agent":"BaizhiSpider",
#     "hello":"i am a spider"
# }
# res = requests.get(url,headers=headers)
# print(res.text)

# url = "https://httpbin.org/cookies"
#
# headers = {
#     "cookie":"helloworld=hi;haha=leihou"
# }
# res = requests.get(url,headers=headers)
# print(res.text)


# url = "https://httpbin.org/cookies"
# # # 比较推荐的
# cookies = {
#     "hello":"world",
#     "hio":"heihei"
# }
# cookies = {"cookie":"helloworld=hi;haha=leihou"}
# res = requests.get(url,cookies=cookies)
# print(res.text)

# req = requests.Request(url=url,cookies=cookies)
# res = requests.get(req)
import random
# with open("ip.txt","r") as r:
#     proxies = r.readlines()
# proxy = random.choice(proxies)
# proxy = proxies.pop()

# print(type(eval(proxy)))

# proxy = {
#     "http":"120.41.115.137:80"
# }
# res = requests.get("http://www.httpbin.org/ip",proxies=proxy,timeout=3)
# print(res.text)

# res = requests.get("http://www.httpbin.org/ip",timeout=3)
# url = "http://www.renren.com/973162784"
# cookies = {"t":"2beb74a8da37dae63782091f61b2849b4"}
# result = requests.get(url,cookies=cookies)
# with open("renren1.html","w",encoding="utf-8") as w:
#     w.write(result.text)
# result = requests.get(url)
# with open("renren2.html","w",encoding="utf-8") as w:
#     w.write(result.text)
# with open("1.jpg","wb") as w:
#     w.write(result)
# import time
# url = "http://www.renren.com/973162784"
# cookies = {"t":"2beb74a8da37dae63782091f61b2849b4"}
# result = requests.get(url,cookies=cookies).cookies
# time.sleep(2)
# result2 = requests.get(url,cookies=result)
# print(result2.text)




















