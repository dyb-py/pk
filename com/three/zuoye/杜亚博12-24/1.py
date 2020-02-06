import gzip
from urllib import request

import MySQLdb
from lxml import etree
import time
def Data(res):
    data=res.read()
    try:
        #解压缩
        d = gzip.decompress(data).decode()
    except:
        #正常格式
        d = data.decode()
    return d
conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='book',
        charset='utf8'
    )

def Ele(url):
    res = request.urlopen(url)
    ele = etree.HTML(Data(res))
    return ele
url = "http://www.xbiquge.la/xiaoshuodaquan/"
ele = Ele(url)
book_names = ele.xpath("//*[@id='main']/div/ul/li/a/text()")
book_urls = ele.xpath("//*[@id='main']/div/ul/li/a/@href")
for book_url in book_urls:
    index1=book_urls.index(book_url)
    book_name=book_names[index1]
    ele = Ele(book_url)
    chapter_names=ele.xpath("//div[@id='list']/dl/dd/a/text()")
    print(chapter_names)
    chapter_urls=ele.xpath("//div[@id='list']/dl/dd/a/@href")
    for chapter_url in chapter_urls:
        # time.sleep(0.7)
        index = chapter_urls.index(chapter_url)
        chapter_name = chapter_names[index]
        ele = Ele("http://www.xbiquge.la"+chapter_url)
        try:
            conts = ele.xpath("//div[@id='content']/text()")
            s = ""
            for cont in conts:
                s += cont.strip()
            cur = conn.cursor()
            sql = "insert into book(name,chapter,con)values(%s,%s,%s) "
            cur.execute(sql, (book_name,chapter_name,s))
            conn.commit()
            cur.close()
            print(chapter_name)
        except:
            pass
conn.close()
        # with open(book_name + ".txt", "a", encoding="utf-8") as w:
        #     print("保存" + chapter_name)
        #     w.write(chapter_name + "\n" + s + "\n")