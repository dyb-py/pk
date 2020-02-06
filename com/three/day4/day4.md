### 断点续传

```markdown
1. 为什么要用到断点续传？
		爬虫程序出错或者其他原因导致爬虫中断的情况，需要从上次中断的位置继续往下抓取。
2. 笔趣阁：
		1. 需要知道当前书籍的url
		2. 需要知道当前章节的url
 存断点：
 		覆盖的形式存储
 		当启动爬虫的时候，首先要看有没有断点存在。如果有断点的话，就从断点处爬取，如果没有，就从自定义的位置爬取。
```

```python
import requests
from lxml import etree
import MySQLdb
conn = MySQLdb.connect(
    db="spider",
    user="root",
    passwd="123456",
    host="localhost",
    port=3306,
    charset='utf8'
)
cursor = conn.cursor()
# 书的url
def get_book_url():
    global book_name
    new_book_url,cha_url= get_duandian()  # 从数据库中获取断点
    url = "http://www.xbiquge.la/xiaoshuodaquan/"
    res = requests.get(url).content.decode()
    ele = etree.HTML(res)
    book_name = ele.xpath("//*[@id='main']/div/ul/li/a/text()")[0]
    book_urls = ele.xpath("//*[@id='main']/div/ul/li/a/@href")
    for book_url in book_urls:
        if new_book_url:  # 书的断点存在则爬取
            get_cha_url(new_book_url,cha_url)
        else:
            get_cha_url(book_url,cha_url)
# 章节url
def get_cha_url(book_url,new_cha_url):
    # new_cha_url = get_duandian()[-1] # 获取章节url
    res = requests.get(book_url).content.decode()
    ele = etree.HTML(res)
    cha_urls = ele.xpath("//div[@id='list']//dd/a/@href")
    if new_cha_url:  # 如果断点存在
        index = cha_urls.index(new_cha_url)  # 获取的当前书的章节index
        for cha_url in cha_urls[index+1:]:  # 爬下一章
                get_cont(cha_url) # 章节url传给get_cont 进行存储
                duandian(book_url,cha_url)  # 存新的断点
    else:
        for cha_url in cha_urls:
            get_cont(cha_url)
            duandian(book_url, cha_url)  # 存断点 --- 数据库里没有断点的情况
# 保存cont
def get_cont(cha_url):
    res = requests.get("http://www.xbiquge.la"+cha_url).content.decode()
    ele = etree.HTML(res)
    cha_name = ele.xpath("//h1/text()")[0]
    conts = ele.xpath("//div[@id='content']/text()")  # 获取章节内容
    s = ""
    for cont in conts:
        s += cont.strip()+"\n"
    with open(book_name+".txt","a",encoding="utf-8") as w:
        w.write(cha_name+"\n"+s)
# 打断点
def duandian(book_url,cha_url):
    sql = "update biqugeduandian set book_url=%s,cha_url=%s"
    cursor.execute(sql,(book_url,cha_url,))
    conn.commit()
# 获取断点
def get_duandian():
    sql = "select * from biqugeduandian"
    cursor.execute(sql)
    return cursor.fetchone() # return获取的断点
if __name__ == '__main__':
    get_book_url()
```

### 人人网

```markdown
1. 登录： cookie跳过登录步骤
2. 通过一个用户进行发散，抓取全站
		社交类网站抓取思路
3. 人人网访问100个人的页面，会出现验证码，需要通过验证码验证之后才能继续访问。
4. 验证码的解决思路：
	1. pillow库做自动识别
	2. 图像识别（人智）
	3. 下周一说
```

### 作业

```markdown
1. 整理一周的知识图谱
2. 世纪佳缘，百合网  --- 一般需要登录
		数据量：2万条
   为什么要抓取：
   		1. 数据量多
   		2. 数据值钱
```

