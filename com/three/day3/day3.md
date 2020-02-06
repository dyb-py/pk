### urllib反人类的处理

```markdown
难用的地方：
	1. headers  
		Request对象 ---  urlopen()  。。。
	2. cookie
		handler   opener   opener.open()   
	3. proxy
		handler   opener   opener.open()
	4. timeout   
	5. get post
		传入的是什么数据，都要经过parse处理
		get 和 post请求应该区分出来
封装urllib
	get(url,headers={},cookie={},proxy={},timeout)
	post(url,data={},headers={},cookie={},proxy={},timeout)
响应的处理
	text 文本处理   
	zip ： 压缩流处理
	json ： loads()
```

```python
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
    req = request.Request(url,headers=headers)  # req对象
    if method=="post": # 区分方法为post，对data的处理
        data = bytes(parse.urlencode(data),encoding="utf-8") # 处理data
    else: # 方法为get方式，data的处理
        data =  parse.urlencode(data) # get传参
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
```

### requests高级请求库

```markdown
1. 用起来比urllib更加高级（简便，功能更健全）
2. requests库是对urllib的封装
3. 企业开发中（爬虫）最常用的手段
	框架：
		1. 功能比较少，用起来难受，速度快
		2. 功能比较多，用起来舒服，速度慢
4. 第三方的HTTP请求库
		pip install requests
```

### requests对应的函数

```markdown
1. get(url, params=None, **kwargs)
		作用：发送get请求
		url：统一资源定位符
		params：get请求的参数
		**kwargs: 可变长参数
2. post(url, data=None, json=None, **kwargs)
		作用：发送post请求
		url：统一资源定位符
		data:post请求携带的参数
		json：post请求带的参数（以json格式）
		**kwargs: 可变长参数
3. put(url, data=None, **kwargs)
		作用：向服务器发送一条存储的请求
4. patch(url, data=None, **kwargs)
		作用：向一条局部修改的请求
5. delete(url, **kwargs)
		作用：向服务器发送一条删除资源的请求
6. head(url, **kwargs)
		作用：返回url携带的headers
7. options(url, **kwargs)
		作用：返回当前url所指出的请求类型（一般就是get和post）
```

- get请求

```python
import requests
r = requests.get('https://www.python.org')
print(r.content)
```

- post请求

```python
import requests
payload = {
    "key2": "value2",
    "key1": "value1"
}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.content)
```

- 添加headers

```python
url = "https://httpbin.org/headers"
headers = {
    "User-Agent":"BaizhiSpider",
    "hello":"i am a spider"
}
res = requests.get(url,headers=headers)
print(res.text)
```

- 添加cookies

```python
1. 
url = "https://httpbin.org/cookies"

headers = {
    "cookie":"helloworld=hi;haha=leihou"
}
res = requests.get(url,headers=headers)
print(res.text)
2.
url = "https://httpbin.org/cookies"
# 比较推荐的
cookies = {
    "hello":"world",
    "hio":"heihei"
}
cookies = {"cookie":"helloworld=hi;haha=leihou"}
res = requests.get(url,cookies=cookies)
print(res.text)
```

- 添加代理

```python
proxy = {
    "http":"120.41.115.137:80"
}
res = requests.get("http://www.httpbin.org/ip",proxies=proxy,timeout=3)
print(res.text)

随机代理
import random
with open("ip.txt","r") as r:
    proxies = r.readlines()
proxy = random.choice(proxies)
print(type(eval(proxy)))
```

- 设置超时时间

```python
res = requests.get("http://www.httpbin.org/ip",proxies=proxy,timeout=3)
```

### response对应的属性

```markdown
1. text
	文本对象（html字符串），如果乱码问题，可以在前面定义好encoding
2. content（保存流媒体的同时，也可以解决乱码问题）
	二进制字符串
3. request : 返回给我们请求的对象（Request对象）
4. cookies ： 返回响应的cookie
5. headers： 返回响应的header
6. url: 响应该次请求所请求的url
7. status_code：返回本次请求的响应状态码
```

### 会话保持

```markdown
session
```

- 方式1(用于服务器检测set-cookie用)

```python
url = "http://www.renren.com/973162784"
cookies = {"t":"2beb74a8da37dae63782091f61b2849b4"}
result = requests.get(url,cookies=cookies)
response_cookie = result.cookie
time.sleep(2)
result2 = requests.get(url,cookies=result)
print(result2.text)
```

- 方式二

```python
import requests
url = "http://www.httpbin.org/cookies/set/ni/wo"
s = requests.Session() # 保存的是自动登录的cookie,前后的session对象保存的是同一个cookie
res1 = s.get(url)
print(res1.text)
res2 = s.get(url).text
print(res2)
```

- 方式3

```python
url = "http://www.iqianyue.com/login"
p = {"http":"123.139.56.238:9999"}
with requests.session() as s:
    res = s.post(url=url,data={"user":"123","password":"123","submit":""},proxies=p)  # 第一次发送post请求，请求成功之后，session里面就存储了自动登陆的cookie
    print(res.text)
    s.get(url=new_url)  # 第二次发送请求的时候，就携带了cookie登录
```

- session维持headers

```python
headers = {"User-Agent":"wangdachui","love":"xiaomei"}
s = requests.Session()
s.headers=headers
print(s.get("http://www.httpbin.org/headers").text)
print(s.get("http://www.httpbin.org/headers").text)
```

### 小结

```markdown
1. requests使用起来更加简单，功能强大，慢
2. requests独有的session机制，可以进行会话保持
		1. 消耗资源大
		2. 不安全
3. 一般情况下，多使用手动的cookie和header
学习一个新的爬虫框架：
	1. 如何发请求
	2. 如何解析响应
```

### 作业

```markdown
1. 前面的作业换成requests
2. 淘宝网女装 / 男装 
	名称   价格   发货地
	1000个
3. 招聘类网站 --- 长期
	智联，拉钩，51job，boss直聘
	500W  （不限工作）
4. 人人网（选做）
	1000条
```















