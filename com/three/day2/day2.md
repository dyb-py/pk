### 伪装身份

```markdown
1. 告诉服务器我是个人（浏览器）
		User-Agent：告诉对方我的身份---仅指是个人
2. 人的各个要素、特点
		headers：（鼻子，眼睛，嘴...）
3. 身份证检测
		cookies : 用户信息等，证明自己是个人
4. 重新伪装--- 洗心革面（换个人去）
		ip/cookie
```

### User-Agent

```python
from urllib import  request as req
url = "http://www.httpbin.org/headers"
headers = {"User-Agent":"BaiDuSpider"}
request = req.Request(url,headers=headers)
res = req.urlopen(request).read().decode()
print(res)
```

### 其他headers

```python
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'BAIDUID=A56424D93AAEF8FA4BC9A42FB823A3D3:FG=1; BIDUPSID=A56424D93AAEF8FA4BC9A42FB823A3D3; PSTM=1571306136; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=80187_0_7_9_1_2_0_0_6_2_74_0_0_0_99_0_1577153193_0_1577153292%7C9%2326_7_1577065117%7C4; delPer=0; BD_HOME=0; H_PS_PSSID=1438_21123_30211_30284; BD_CK_SAM=1; PSINO=2; H_PS_645EC=c6c13NdgtEPBs25xHIjjlRy%2Br9ObXP15O3%2FG38SswgRzJmrrR8RTaYSpQnw; BDSVRTM=162',
'Host':'www.baidu.com',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}
request = req.Request(url,headers=headers)
res = req.urlopen(request).read().decode()
print(res)
```

### cookies

```python
from urllib import request
url = "http://www.httpbin.org/cookies"
headers = {
'Cookie':'BAIDUID=A56424D93AAEF8FA4BC9A42FB823A3D3:FG=1; BIDUPSID=A56424D93AAEF8FA4BC9A42FB823A3D3; PSTM=1571306136; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=80187_0_7_9_1_2_0_0_6_2_74_0_0_0_99_0_1577153193_0_1577153292%7C9%2326_7_1577065117%7C4; delPer=0; BD_HOME=0; H_PS_PSSID=1438_21123_30211_30284; BD_CK_SAM=1; PSINO=2; H_PS_645EC=c6c13NdgtEPBs25xHIjjlRy%2Br9ObXP15O3%2FG38SswgRzJmrrR8RTaYSpQnw; BDSVRTM=162'
}
req = request.Request(url)
res = request.urlopen(req).read().decode()
print(res)
```

### response cookie

```python
from urllib import request
from http.cookiejar import CookieJar
cookiejar = CookieJar() # 保存的是response cookie
handler = request.HTTPCookieProcessor(cookiejar)  # cookie handler
print(cookiejar)
opener = request.build_opener(handler)
url = "http://www.renren.com/972685182"
res = opener.open(url).read().decode()
# print(res)
print(cookiejar)
```

### ip代理

```python
url = "http://www.httpbin.org/ip"
proxy = {"http":"127.23.23.53:8080"}
handler = request.ProxyHandler(proxy) # 构建一个代理handler
opener = request.build_opener(handler)
res2 = opener.open(url).read()
print(proxy)
```

### 为什么用到代理

```markdown
1. 如果一直快速的发请求，会被封禁（拉黑）
	解决：
		1. 限制请求频率（效率低） 不推荐
		2. 换IP（换个小号）
2. IP的来源
		1. 硬实力（花钱买）   可用率比较高
		2. 采集免费IP   可用率及其低
3. 如果使用代理
		1. 单个代理一直采集数据，如果被封了，换一条代理
		2. 每请求一次换一条代理
```

### 处理异常

```markdown
1. 异常出现的原因
		1. 服务器不是都给力
				响应慢
		2. 网慢
			2.1 提高硬实力	
		3. 无效链接
			1. 占用资源过多（时间过长）
			2. 该链接同等情况下返回的数据不是我们想要的
2. 解决办法：
	异常处理
	设置超时时间，超过超时时间，就不等待了。配合异常处理
```

### 大批量连续获取数据出现的问题

```markdown
1. 爬虫一定会有问题（出错）  程序是否相对健壮
请求失败：配合异常处理完成  --- 请求三次-5次
ip被封：换ip
服务器本身的问题：
	1. 降低请求频率（数据量少，而且影响不大）
	2. 把失败的请求重新调度一次，根据响应的是否是我们期望值来判断
```

### 保存图片

```python
from urllib import request
url = "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1577161427,3252306349&fm=26&gp=0.jpg"
res = request.urlopen(url).read()
# 通用模式
with open("1.jpg","wb") as w:
    w.write(res)
request.urlretrieve(url,"2.jpg")  # urllib 专用
```

### 百度图片

```python
from urllib import request
import json
pagenum = 0
num = 0
while True:
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%96%97%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E6%96%97%E5%9B%BE&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn="+str(pagenum)+"&rn=30"
    pagenum += 30
    res = json.loads(request.urlopen(url).read().decode())
    for i in res['data']:
        try:
            print(i["hoverURL"])
            request.urlretrieve(i["hoverURL"],"E:\\Python186共享文件夹\\第三阶段\\代码\\day2\\image\\"+str(num)+".jpg")
            num += 1
        except:
            pass
```

### 反爬的几种常见手段及解决方案

```markdown
1. BAN User-Agent   
		解决办法：加UA，headers
2. BAN cookies
		解决办法：
		1.限制访问速度
		2.购买账号，生成多个cookie
		3.获取服务器的set cookie 值
3. BAN IP ： 误杀率大
		解决办法：换IP
4. ajax异步传输
		在响应中找到对应的json数据找到对应的url，通过找规律的方式，发送请求到对应的服务器。
5. 验证码验证：当某一个用户访问次数过多的时候，会自动跳转到一个验证码的界面，只有输入正确的验证码才能继续访问
6. JavaScript渲染（JS加密）：网页开发者不会将重要的信息写在html中，会写在js文件中，浏览器会自动渲染js中的代码并展示在浏览器中。
7. 自定义字体：部分网站会通过自定义字体的方式，对重要的数据进行伪装处理。
8. 滑块验证：部分需要验证生物行为的网站会加入滑块验证码，通过验证码才能继续访问网站。
9. apk反编译(app脱壳)：java写的。   -- 比较少
```

### 作业

```markdown
1. 百度图片100张
2. 百度失信人
	姓名  身份证号  省份  案号  被执行人履行情况
	入库  （去重案号）
	数据量要求：
	5000条及格
	10000条良好
	100000条优秀
3. 封装urllib  （选做） 帅气逼人，英俊潇洒，风流倜傥，才高八斗的王靖惠同学必做。cto，ceo必做
	cookie  代理  text 二进制的值  
	get（url，cookie，header，proxy，timeout） 
    post（url，data，cookie，header，proxy，timeout）
```

















