### Requests

~~~markdown
1. 是一个第三方的请求库
requests有什么问题？
		1. requests比较慢（致命）
框架：
		1. 使用起来特别方便，功能单一
		2. 使用起来比较麻烦，功能强大
1. 数据库的代码重复编写
2. 请求和响应有一定的冗余
3. requests不能对爬取的队列进行去重或调度
4. 效率低
~~~

### Scrapy

~~~markdown
1. 是一个专业的第三方爬虫框架（协程级的异步框架）
		19几几年的一个框架
		pip install scrapy
~~~

- Scrapy的安装

~~~markdown
1. 装一个异步框架库Twisted
2. pip install pywin32 
3. pip install scrapy
~~~

### Scrapy的框架





![scrapy框架图](E:\Python186共享文件夹\第三阶段\笔记\pic\scrapy框架图.png)



![Scrapy详细框架图](E:\Python186共享文件夹\第三阶段\笔记\pic\Scrapy详细框架图.png)





~~~markdown
1. 引擎：负责各个组件的数据的交互，以及规定整个框架的运行流程
2. scheduler（调度器）：对请求的队列进行调度
3. Downloader（下载器）：请求和响应。
4. Spider（爬虫）：规定requests的属性以及url
5. Item Pipeline（管道）：入库和持久化 
~~~

- scrapy的工作流程

~~~markdown
1. 从spider获取起始的url，交给了引擎，引擎把url（Requests）转发给了scheduler
2. scheduler身为调度器，主要做的是对Reuqests对象进行调度。把Requests对象调度给Downloader（经过引擎）。如果scheduler接收到了一个来自于Downloader的请求，那么说明该请求发送不成功，所以加入请求失败重试队列。
3. Downloader收到引擎传来的Requests对象后，把Requests对象进行发送。发送然后等待响应，接收到响应以后，如果响应状态码为200，经过引擎把响应传给Spiders，如果响应状态码不是200，经过引擎，传给Scheduler。
4. Spiders接收到了响应后，对响应进行解析。
		url：重新将解析出的url封装成Requests对象， 并且传给scheduler
		数据：将数据封装成Items对象，并且将Items对象传给Item Pipeline
5. Item Pipeline接收到Items对象后，将Items对象中的数据进行入库
~~~

- 创建一个scrapy项目

~~~markdown
1. scrapy startproject 项目名
2. cd 项目目录
3. scrapy genspider 爬虫名 allowed_domains和start_urls
~~~

- scrapy的开发流程

~~~markdown
1. 确认需求：获得哪些数据，封装Items
2. 编写Spiders
		1. 初始url
		2. 解析数据的解析规则
		3. 解析url的解析规则----回调函数（callback）
3. Pipelines：
		编写入库规则
4. 下午在讲
~~~

- settings

![settings](E:\Python186共享文件夹\第三阶段\笔记\pic\settings.png)

- 作业

~~~markdown
1. scrapy爬取百度图片和人人网和失信人和猫眼电影和笔趣阁和51job
2. bilibili（一百个）
~~~

