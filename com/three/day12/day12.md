### 怎么精准定位爬虫中的反爬

~~~markdown
1. 使用代码发送的请求，返回的响应和我们使用浏览器发送的请求返回的相应不同。---我不像一个人。---使自己像一个人。
		使用浏览器发送一个请求，浏览器内核会帮我们做很多事
		比如：headers、cookies等等
		如果认为的想模拟浏览器内核的操作：手动加上headers和cookies
		中国商标网：直接检查浏览器内核（影响了效率），投入的技术成本太高太高。
2. 爬虫是一段自动化的从互联网上大批量爬取数据的一段程序。
		大批量采集：
			1. 验证码：超级鹰、图像识别（OCR）：能够解决所有反爬
				降噪：有噪点，图片比较乱。通过调整图片的色彩值，让小的噪点，消失甚至忽略不计。
				机器学习：采集100000张验证码作为训练集，手动的标注100000张数据，我的电脑（何欣），告诉何欣这玩意儿是个猫==告诉电脑这张图片对应的是什么验证码。
			2. 不可抗力因素或者中间被反爬：
				不可抗力：
					停电：断点
					断网：断点
				中间被反爬：断点
			3. 动态cookie：
				1. 爬着爬着，响应不对了；同时某个请求会返回一个set_cookie
				2. 需要重新获取一个cookie，再次发送请求的时候将新的cookie重新携带。
~~~

### 分布式爬虫

#### 分布式

- 多个终端做不同的事

![多个终端做不同的事](E:\Python186共享文件夹\第三阶段\笔记\pic\多个终端做不同的事.png)

- 多个终端做相同的事

![多个终端做相同的事](E:\Python186共享文件夹\第三阶段\笔记\pic\多个终端做相同的事.png)

~~~markdown
1. 多个终端做相同的事（不重复）
2. 进程间的通信(数据的传输)使用队列（Queue）
~~~

#### 多进程

~~~markdown
1. 进程池：
		池：值的是一种容器，可以保存一种特定的资源、对象
		1. IP代理池：存IP
		2. 常量池：存的是常量
		3. 串池：存放字符串
		4. 数据库连接池：连接对象随用随取
		5. 缓冲池：缓冲一些数据，供未来使用。
		6. 进程池：存放的是进程。
池有什么好处：
		方便、节省资源
		正常：
		消耗一定资源创建对象--->销毁对象--->再创建
		使用了池：
		消耗一定资源创建对象--->放入池中--->直接从池中获取
进程、线程、协程：基于操作系统
同步、异步、分布：调度
~~~

#### 分布式进程（以requests为例）

~~~python
 from multiprocessing import Pool,Manager
import requests
from lxml import etree
import time
import MySQLdb


conn = MySQLdb.connect(
            db="job51",
            user="root",
            passwd="123456",
            host="localhost",
            port=3306,
            charset='utf8'
        )
cursor = conn.cursor()

def get_list(url_q):
    pagenum = 1
    while True:
        url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,'+str(pagenum)+'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        pagenum += 1
        print('-----------')
        print(pagenum)

        res = requests.get(url=url, timeout=3)

        try:
            res = res.content.decode('gb2312')
            ele = etree.HTML(res)
            urls = ele.xpath('//*[@id="resultList"]//div/p/span/a/@href')
            for url in urls:
                if url.startswith('https://jobs.51job.com/') and url.endswith('s=01&t=0'):
                    url_q.put(url)
        except:
            pass

        if pagenum >= 20:
            break


def get_detail(url_q,data_q):
    while True:
        print('asldkfjslkdjfl')
        print(url_q.qsize())
        url = url_q.get()
        if url:
            print(url)
            res = requests.get(url=url, timeout=3)
            try:
                ele = etree.HTML(res.content.decode('gb2312'))
                # title = ele.xpath("//title/text()")[0]
                jobname = ele.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()")[0]
                salary = ele.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()")[0]
                exp = ele.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[2]")[0].strip()
                data_q.put((jobname,salary,exp,url))
            except:
                print('详情页解析出错')

def save_db(data_q):
    while True:
        data =data_q.get()

        if data:
            sql = 'INSERT INTO job51 VALUES (%s,%s,%s,%s)'
            try:
                cursor.execute(sql, (data[0], data[1], data[3], data[2]))
            except:
                continue
            conn.commit()
        else:
            continue


if __name__ == '__main__':
    # 创建一个url队列
    url_q = Manager().Queue()
    # 创建一个data队列
    data_q = Manager().Queue()
    pool = Pool(processes=3)
    # args指的是进程间的通信参数
    # 向进程池中添加一个进程
    pool.apply_async(func=get_list,args=(url_q,))
    pool.apply_async(func=get_detail,args=(url_q,data_q))
    pool.apply_async(func=save_db,args=(data_q,))
    pool.close()
    pool.join()
~~~

### scrapy分布式

![scrapy的分布式](E:\Python186共享文件夹\第三阶段\笔记\pic\scrapy的分布式.png)

~~~markdown
1. 发送请求---接受响应最耗时，所以应该在发请求接响应的地方做分布式
2. 管道：持久化、清洗并不耗时，所以不需要在Item Pipeline上做分布式
3. 爬虫：解析数据，基本不耗时，所以也不需要。
~~~

### Scrapy-redis

~~~markdown
是已经集成好了第三方的一个分布式架构
基于scrapy、redis
~~~

![scrapy-redis简单分析](E:\Python186共享文件夹\第三阶段\笔记\pic\scrapy-redis简单分析.png)

#### scrapy-redis的使用

~~~markdown
1. 安装redis
		默认redis的端口号为6379-
2. 需要在scrapy项目中进行简单的配置
		REDIS_HOST='192.168.0.1'
		REDIS_PORT=6379
		# 更换调度
		SCHEDULER='scrapy_redis.scheduler.Scheduler'
		# 手动配置redis的去重策略
		      				      DUPEFILTER_CLASS='scrapy_redis.dupefilter.RFPDupeFilter'
 3. 在spider中修改spider需要继承的父类（from scrapy_redis.spiders import RedisSpider）
 继承为RedisSpider
~~~

![redis存储](E:\Python186共享文件夹\第三阶段\笔记\pic\redis存储.png)

### 调度器

![scheduler](E:\Python186共享文件夹\第三阶段\笔记\pic\scheduler.png)

### 爬虫

![spiders](E:\Python186共享文件夹\第三阶段\笔记\pic\spiders.png)

- 作业

```markdown
1. 以小粉红的电脑为调度器，爬一爬51job的所有职业
		协同开发
2. 自己设计一个分布式爬虫框架
		交一张图
```

### 