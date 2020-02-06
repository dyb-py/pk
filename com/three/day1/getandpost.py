from urllib import request,parse
# url = "http://www.baidu.com/"
# # 发送请求，并接受到响应
# res = request.urlopen(url)
# with open("baidu.html","w",encoding="utf-8") as w:
#     w.write(res.read().decode()) #存储
password = "niubiclass"
url = "https://iqianyue.com/mypost"
data = {
    "name": "wenguang",
"pass": password
}
data = bytes(parse.urlencode(data),encoding="utf-8")
print(data)
response = request.urlopen(url,data=data).read().decode()
print(response)
# ?name=wenguang&pass=123456