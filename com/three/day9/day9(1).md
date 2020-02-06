### 大规模采集数据会出现的问题

~~~markdown
1. 大规模:
		1. 数据量至少是千万级
		2. 爬取的网站量至少得上百
2. 问题：
		1. 封IP（换IP）
			1. 每当有一个ip被封，获取新的ip
			2. 持续的保持数据库中拥有100条ip，每次发请求，都换。
		2. 降低我的爬取速度。---如果爬取数据的数量，不是很多的话，影响不大。
		3. 把挂掉的请求，保存起来，有朝一日进行RETRY
~~~

### Scrapy的高阶使用

~~~markdown
1. get请求：有参/无参
	return scrapy.Request(url=url) #默认就是get请求
		有参：直接在url后面拼接，
2. post请求
	FormRequest(url,formdata=form表单)
3. headers
	1. 在scrapy.Request(headers=头)
	2. 在settings中修改全局的默认headers
		如果不配置头文件，默认UA为
		"User-Agent": "Scrapy/1.8.0 (+https://scrapy.org)"
		相当于告诉了对方，我是个爬虫，请给我数据。
	3. 两种配置headers的途径优先级：
			如果两种配置途径配置的headers字段不同，scrapy会全部添加到headers里面。
			如果两种配置途径配置的headers字段相同，第一种优先级更高。
4. cookies
	在使用cookies之前，一定要到settings里面进行如下配置：
		COOKIES_ENABLED = True
	在scrapy.Request(cookies=cookies)
5. proxy
	meta['proxy']='http://119.147.137.79:8008'
	配置meta的proxy属性
	配置一个meta，在scrapy.Request(meta=meta)
6. 响应的相关属性
	1. text，返回当前响应的解码后数据（自动解码）
	2. body，返回当前响应的响应体（原来响应是什么就显示什么）
	3. xpath，新版scrapy已经支持text()，获得到是一个列表，列表中的元素是一个个Selector对象，而获得Selector对象中的data值需要调用extract()方法
	4. meta属性可以获取cookies
	5. headers属性可以获取响应头
7. 额外功能
	1. 中间件
	2. scrapy给我们一些文件下载提供了专用的pipeline
	3. 日志
	4. 断点续传
~~~

### Scrapy的中间件

~~~markdown
1. 作用：解耦和
~~~

~~~markdown
1. Spider Middleware:爬虫中间件，位于爬虫和引擎之间
2. Downloader Middleware:下载器中间件，位于下载器和引擎之间
3. Scheduler Middleware：调度器中间件，位于调度器和引擎之间，内置的，水平不够千万别碰。
~~~

#### 爬虫中间件

![Spider_Middleware](E:\Python186共享文件夹\第三阶段\笔记\pic\Spider_Middleware.png)

#### 下载器中间件

![Downloader_Middleware](E:\Python186共享文件夹\第三阶段\笔记\pic\Downloader_Middleware.png)



#### 断点续传

~~~markdown
就是把调度器中的内存队列（未爬取的request），进行持久化
会把已爬取的url队列进行持久化。
~~~

#### 调度器

~~~markdown
磁盘队列和内存队列
1. 磁盘队列：
		优点：空间大、便宜、持久化
		缺点：慢
2. 内存队列：
		优点：快
		缺点：贵、空间小、不能持久化
3. 调度器：
		正常运行的时候，基于内存队列。
		如果要做断点。---需要把内存中的队列给持久化的磁盘队列中。s
~~~

