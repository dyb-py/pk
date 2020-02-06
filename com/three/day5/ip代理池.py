import requests
from lxml import etree
import MySQLdb
class IP_Pool():
    # 属性
    def __init__(self,limit):
        self.limit = limit # 传的阈值
        self.conn = MySQLdb.connect(
            db="spider",
            user="root",
            passwd="123456",
            host="localhost",
            port=3306,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
    # 方法
    # 检测ip是否可用
    def check_ip(self,ip):
        try:
            res = requests.get("http://httpbin.org/ip",timeout=3,proxies=ip).text
            if "124.64.16.94" in res:
                return False
        except:
            return False
        return True
    # 定时定量检测ip是否可用
    def check_all(self):
        sql = "select * from ip_pool"
        self.cursor.execute(sql)
        ips = self.cursor.fetchall() # 获取全部ip
        for ip in ips:# 遍历出来
            if not self.check_ip(ip[0]):  # 是否通过检测，未通过则删除
                sql = "delete from ip_pool where ip=%s"
                self.cursor.execute(sql,[ip[0]])
                self.conn.commit()
    # 查看ip的数量
    def count_ip(self):
        sql = "select count(ip) from ip_pool"
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]
    def save_ip(self,ip):
        if self.check_ip(ip):
            sql = "insert into ip_pool values(%s)"
            self.cursor.execute(sql,[ip])
            self.conn.commit()
    # 爬取ip,并保存
    def crawl_ip(self):
        if self.count_ip() < self.limit:
            num = 1
            for i in range(100):
                url = "http://qinghuadaili.com/free/"+str(num)
                num += 1
                ele = etree.HTML(requests.get(url).text)
                type = ele.xpath("//tbody/tr/td[4]/text()")
                ips = ele.xpath("//tbody/tr/td[1]/text()")
                port = ele.xpath("//tbody/tr/td[2]/text()")
                for i in range(len(type)):
                    ip_dict = {}
                    # {type:ip:port}
                    ip_dict[type[i].lower()] = ips[i]+":"+port[i]
                    print(ip_dict)
                    self.save_ip(str(ip_dict))
        self.check_all()
    # 获取一条ip
    def get_ip(self):
        sql = "select * from ip_pool"
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

if __name__ == '__main__':
    ip_pool = IP_Pool(20)
    ip_pool.crawl_ip()