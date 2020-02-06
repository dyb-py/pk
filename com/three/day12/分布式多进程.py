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