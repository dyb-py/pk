

# import json
# url = "https://baike.baidu.com/api/wikiui/getlemmaconfig?r=0.3921626663618556"
# res = request.urlopen(url)
# data = json.loads(res.read().decode())  # json数据解析成python可以解析的数据类型
# print(data['announcement']['data']['content'])
# from urllib import request
# import re
# url = "http://www.xbiquge.la/xiaoshuodaquan/"
# res = request.urlopen(url).read().decode()  # 发送请求
# rule = '">(.*?)</a>'
# print(re.findall(rule,res))


# 压缩流 
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



