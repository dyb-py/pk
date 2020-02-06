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
















