from urllib import request,parse
import json
import gzip
from http.cookiejar import CookieJar
from lxml import etree
cookiejar = CookieJar()
# cookie hander
cookiejarHandler = request.HTTPCookieProcessor(cookiejar)
# get 格式封装
def get(url,headers={},cookies={},proxy={},timeout=None):
    return __request(url=url,method="get",headers=headers,cookies=cookies,proxy=proxy,timeout=timeout)
# post格式封装
def post(url,data={},headers={},cookies={},proxy={},timeout=None):
    return __request(url=url,method="post",data=data,headers=headers,cookies=cookies,proxy=proxy,timeout=timeout)
# request请求
def __request(url,method=None,data={},headers={},cookies={},proxy={},timeout=None):

    if method=="post": # 区分方法为post，对data的处理
        data = bytes(parse.urlencode(data),encoding="utf-8") # 处理data
        req = request.Request(url, headers=headers,data=data)  # req对象
    else: # 方法为get方式，data的处理
        data =  parse.urlencode(data) # get传参
        req = request.Request(url, headers=headers)  # req对象
    url += "?"+data  # 对url进行拼接
    req.full_url=url
    value = ""
    if cookies: # 对cookies的处理
        for k,v in cookies.items():
            value += k+"="+v+";"  # 拼接好的cookie格式
        req.add_header(key="Cookie",val=value[:-1])  # 把拼接好的cookie加入到headers里面
    if proxy:  # 对代理的处理
        proxyhandler = request.ProxyHandler(proxy)
        opener = request.build_opener(proxyhandler,cookiejarHandler)
    else:
        opener = request.build_opener(cookiejarHandler)
    body = opener.open(req,timeout=timeout).read()  # 最终返回一个opener.open对象
    return Response(body)  # 返回的对象扔给Response处理
class Response():
    def __init__(self,body):
        self.body = body
    @property #text格式处理
    def text(self):
        try:
            return self.body.decode()
        except:
            return self.body.decode("gbk")
    @property  # json格式处理
    def json(self):
        return json.loads(self.body)
    @property
    def unzip(self): # 压缩流格式处理
        return gzip.decompress(self.body)
    # 处理xpath（额外功能）
    def xpath(self,str):
        try:
            str2 = self.text
        except:
            str2 = self.unzip
        return etree.HTML(str2).xpath(str)


