import gzip
from urllib import request

import MySQLdb
from lxml import etree
def Da(res):
    data=res.read()
    try:
        #解压缩
        d = gzip.decompress(data).decode()
    except:
        #正常格式
        d = data.decode()
    return d

class Date():
    def __init__(self,url):
        res=request.urlopen(url)
        self.data=Da(res)
    def Ele(self):
        self.ele=etree.HTML(self.data)
        return self.ele

url = "http://www.xbiquge.la/xiaoshuodaquan/"
d=Date(url)
ele=d.Ele()
book_names = ele.xpath("//*[@id='main']/div/ul/li/a/text()")
book_urls = ele.xpath("//*[@id='main']/div/ul/li/a/@href")
for book_url in book_urls:
    index1=book_urls.index(book_url)
    book_name=book_names[index1]
    d = Date(book_url)
    ele = d.Ele()
    chapter_names = ele.xpath("//div[@id='list']/dl/dd/a/text()")
    print(chapter_names)
    chapter_urls = ele.xpath("//div[@id='list']/dl/dd/a/@href")
    for chapter_url in chapter_urls:
        # time.sleep(0.7)
        index = chapter_urls.index(chapter_url)
        chapter_name = chapter_names[index]
        d = Date("http://www.xbiquge.la"+chapter_url)
        ele = d.Ele()
        try:
            conts = ele.xpath("//div[@id='content']/text()")
            s = ""
            for cont in conts:
                s += cont.strip()
            print(chapter_name)
            print(s)
            with open(book_name + ".txt", "a", encoding="utf-8") as w:
                print("保存" + chapter_name)
                w.write(chapter_name + "\n" + s + "\n")
        except:
            pass