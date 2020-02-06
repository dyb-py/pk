























































































































































































### 1.什么是爬虫？

```markdown
爬虫是一种自动化的从互联网上大批量获取数据的一段程序
自动化：只需要把代码写好，就可以慢慢执行，不需要管理
互联网：因特奈特
数据：文本，二进制流，压缩流（GZIP）等数据
程序：程序员手动敲的，可以执行的的一段代码或者文件。
Spider
```

### 2.为什么用爬虫？

```markdown
1. 需要大批量数据
		给公司（数据公司，数据分析，人智。。。）
2. 减少人力
3. 搜索引擎需要实时采集数据
4. 钱多，前景好（人智，大数据）
```

### 3.爬虫的种类

```markdown
1. 通用爬虫（大而全）
		功能强大，采集面广，通常用于搜索引擎
		百度，360，谷歌
2. 聚焦爬虫,主题爬虫（小而精）
		功能相对比较单一（只针对特定的网站的特定内容进行爬取）
3. 增量式爬虫（只采集更新后的内容）
		爬取更新后的内容，新闻，漫画，视频...(区分新老数据)
```

### 4.什么样的网站不能爬？

```markdown
1. 法律明文禁止不允许爬取的信息   --- 跟领导说明，并且签免责协议
		大部分都是个人隐私信息（征信）
2. 有robots.txt协议的，并且明文规定不允许采集的网站。  
		robots协议，又叫君子协议。并没有法律效应。但是需要注意，如果没有遵循君子协议，并且数据用于商用，做好上法庭的准备。
```

### 5.sitemap

```markdown
sitemap 网站地图
方便搜索引擎抓取数据的地图（目录）
```

### 6.HTTP请求的主要方式

```markdown
1. GET： 向服务器请求资源
		1. 以get方式携带数据（以？形式拼接）
		2. 以明文形式携带数据
		3. 不安全
		4. 数据类型和大小都有限制
		5. 效率相对高
2. POST：向服务器请求资源
		1. 以post方式携带数据（通常使用form表单提交的方式）
		2. 以密文的形式携带数据
		3. 相对比较安全
		4. 数据类型和大小没有限制
		5. 效率相对低
3. PUT：请求服务器存储一个资源
4. DELETE：请求服务器删除一个资源
5. head请求：请求获取HTTP头信息
6. OPTIONS请求：请求返回当前url所支持的请求类型
		get post
```

URL:统一资源定位符

```markdown
1. 协议部分
2. 域名部分，有以网址的形式展现的，也有以ip地址形式展现的
3. 端口部分：域名和端口号之间使用：分割，如果不指定端口号，将使用默认端口号。
4. 虚拟目录部分：从域名最后一个/开始到最后一个/结束的部分。并不是url必须的部分
5. 文件名部分：从域名最后一个/到？为止是文件名部分。如果没有？就会到# 结束。并不是url必须的部分，如果省略该部分，则使用默认的文件名
6. 参数部分：从？到#结束之间。可以有多个参数，多个参数使用&作为分割符
7. 锚部分：从#开始到结束的部分
```

### 爬虫的原理

```markdown
1. 请求和响应（本质）
2. 一切以数据为导向（不择手段）
```

### 请求头

```markdown
1. User-Agent : 身份认证
2. referer：我从哪来
3. cookie： 记录用户信息（登录状态等）
4. 接受的响应：编码，语言类型，响应的类型
5. HOST主机
6. 安全认证
```

![请求头](E:\Python186共享文件夹\第三阶段\笔记\pic\请求头.png)

### 发送请求urllib

```python
1. get请求
from urllib import request
url = "http://www.baidu.com/"
# 发送请求，并接受到响应
res = request.urlopen(url)  # res是HTTPResponse对象
with open("baidu.html","w",encoding="utf-8") as w:
    w.write(res.read().decode()) #存储	
2. post请求
from urllib import request，parse
password = "niubiclass"
url = "https://iqianyue.com/mypost"
data = {
    "name": "wenguang",
"pass": password
}
data = bytes(parse.urlencode(data),encoding="utf-8") # 转成bytes类型的form参数
print(data)
response = request.urlopen(url,data=data).read().decode()
print(response)
```

## 解析响应

### json数据

```python
from urllib import request
import json
url = "https://baike.baidu.com/api/wikiui/getlemmaconfig?r=0.3921626663618556"
res = request.urlopen(url)
data = json.loads(res.read().decode())  # json数据解析成python可以解析的数据类型
print(data['announcement']['data']['content'])
```

### 压缩流

```python
import gzip
from urllib import request
from lxml import etree
url = "http://www.xbiquge.la/xiaoshuodaquan/"
res = request.urlopen(url)
try:
    data = gzip.decompress(res.read()).decode()  # 解压缩
except:
    data = res.read().decode()  # 正常的格式
ele = etree.HTML(data)  # 获取到element对象
book_name = ele.xpath("//a/text()")
print(book_name)
```

### text格式数据

```python
1. 正则
from urllib import request
import re
url = "http://www.xbiquge.la/xiaoshuodaquan/"
res = request.urlopen(url).read().decode()  # 发送请求
rule = '">(.*?)</a>'  # 正则规则
print(re.findall(rule,res))# 正则匹配结果
2. xpath
	1. 是一个语法
  	2. 是lxml中的一个方法
    	lxml是第三方库
    3. 使用：from lxml import etree
    	ele = etree.HTML(html字符串)  # 构建一个element对象
      	对element对象进行解析
        ele.xpath("xpath语法")
3.xpath语法
	1. // ： 从根节点开始选择
  	2. /  ： 从当前节点开始选择
    3. []  : 里面规定筛选的条件
    4. @属性名  ： 返回对应属性的值
    内置函数：
    	text() 获取当前节点的内容（字符串格式的）
```

### 抓取笔趣阁

```python
import gzip
from urllib import request
from lxml import etree
url = "http://www.xbiquge.la/xiaoshuodaquan/"
res = request.urlopen(url)
try:
    data = gzip.decompress(res.read()).decode()  # 解压缩
except:
    data = res.read().decode()  # 正常的格式
ele = etree.HTML(data)  # 获取到element对象
book_names = ele.xpath("//*[@id='main']/div/ul/li/a/text()")  # 书名
book_urls = ele.xpath("//*[@id='main']/div/ul/li/a/@href")  # 书籍url
for book_url in book_urls:
    ind = book_urls.index(book_url)
    book_name = book_names[ind]
    res = request.urlopen(book_url)
    try:
        data = gzip.decompress(res.read()).decode()  # 解压缩
    except:
        data = res.read().decode()  # 正常的格式
    ele = etree.HTML(data)  # 获取到element对象
    chapter_names = ele.xpath("//div[@id='list']//dd/a/text()") # 获取章节名字
    chapter_urls = ele.xpath("//div[@id='list']//dd/a/@href") # 获取章节url
    for chapter_url in chapter_urls:
        index = chapter_urls.index(chapter_url)  # 通过值获取下标
        chapter_name = chapter_names[index]
        res = request.urlopen("http://www.xbiquge.la"+chapter_url)
        try:
            data = gzip.decompress(res.read()).decode()  # 解压缩
        except:
            data = res.read().decode()  # 正常的格式
        ele = etree.HTML(data)
        conts = ele.xpath("//div[@id='content']/text()") # 获取章节内容
        s = ""
        for cont in conts:
            s+=cont.strip()
        with open(book_name+".txt","a",encoding="utf-8") as w:
            print("保存"+chapter_name)
            w.write(chapter_name+"\n"+s+"\n")
```

### 作业：

```markdown
1. 笔趣阁5本书及以上
	http://www.xbiquge.la/xiaoshuodaquan/
		1. 函数版本
		2. 面向对象版本
2. 爬取猫眼电影top100
	https://maoyan.com/board/4
	中文名  英文名  类别  国家  上映时间  上映地点   用户评分
	要求入库  --- 数据库
3. 今天的笔记整理。
	分析思路写出来
```











