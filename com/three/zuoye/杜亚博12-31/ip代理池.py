import requests
from lxml import etree
import MySQLdb

class IpPool():
    def __init__(self,limit):
        self.limit=limit
        self.conn=MySQLdb.connect(
            db="book",
            user="root",
            passwd="123456",
            host="localhost",
            port=3306,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
    def save(self,ip):
        sql='insert into ippool value (%s)'
        self.cursor.execute(sql,(ip,))
        self.conn.commit()

    def get(self):
        sql='select * from ippool'
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]


    def check(self,ip):
        url='http://httpbin.org/ip'
        try:
            res=requests.get(url,proxies=ip,timeout=3).text
            print(res)
            if '117.136.0.134'in str(res):
                return False
        except:
            return False
        return True

    def check_all(self):
        sql='select * from ippool'
        self.cursor.execute(sql)
        ips=self.cursor.fetchall()
        for ip in ips:
            if not self.check(ip[0]):
                self.delete(ip[0])

    def count(self):
        sql='select count(ip) from ippool'
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def delete(self,ip):
        sql = "delete from ippool where ip=%s"
        self.cursor.execute(sql, [ip])
        self.conn.commit()


    def crawl(self):
        self.check_all()
        while self.count()<self.limit:
            num=1
            for i in range(100):
                url = "http://qinghuadaili.com/free/"+str(num)
                ele = etree.HTML(requests.get(url).text)
                type = ele.xpath("//tbody/tr/td[4]/text()")
                ips = ele.xpath("//tbody/tr/td[1]/text()")
                port = ele.xpath("//tbody/tr/td[2]/text()")
                for i in range(len(type)):
                    ip_dict={}
                    ip_dict[type[i].lower()]=ips[i]+":"+port[i]
                    print(ip_dict)
                    if self.check(ip_dict):
                        self.save(ip_dict)
                        print('有能使用的ip了！！！！！！！！！！！！！！！！！！！')
        print('ip满了噢！！！！')
if __name__ =='__main__':
    ip_pool = IpPool(20)
    ip_pool.crawl()