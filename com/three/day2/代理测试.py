from urllib import request
url = "http://www.httpbin.org/ip"
proxy = {'HTTP': '183.166.163.163:9999'}
handler = request.ProxyHandler(proxy)  # 构建一个代理handler
opener = request.build_opener(handler)
res2 = opener.open(url).read().decode()
print(res2)