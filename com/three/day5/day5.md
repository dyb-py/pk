## 验证码破解

```markdown
同一个账号，访问了100个左右用户的页面，就会出现验证码
1. 换个账号
2. 硬杠 -- 破解验证码
	1. 可以使用pillow库（成功率不高）
			噪点多：影响图片识别的准确率
	2. 使用图像识别方式
			没有这个技术
	3. 第三方打码平台
			看人家开发文档即可
```

```python
import requests
from lxml import etree
from chaojiying import get_code
url = "http://www.renren.com/228113725/profile"
cookies = {
    "t":"6c6ac64833374a0f316580451261744f7"
}
for i in range(110):
    res = requests.get(url,cookies=cookies).text
    ele = etree.HTML(res)
    name = ele.xpath("//title/text()")
    print(name[0])
    if name[0]=="人人网 - 验证码":
        image_url = ele.xpath("//div[@class='optional']/img/@src")[0]  # 获取图片url
        im = requests.get(image_url,cookies=cookies).content  # 拿到图片的二进制流
        with open("1.jpg","wb") as w:
            w.write(im)
        code = get_code(im).get("pic_str")
        data = {
            'id': '880792860',
            'icode': code,
            'submit': '继续浏览',
            'requestToken': '-1330999392',
            '_rtk': '7c6b8dfa',
        }
        requests.post("http://www.renren.com/validateuser.do",data=data,cookies=cookies)
```

### 人人网思路

```markdown
1. 广搜   可以获取到一定量的数据
2. 用户发散
	通过一个人的页面，发散到其他人的页面
			控制去重
3. 如何区分已爬过的和未爬过的url
	数据库：url  设置一个状态码
		已爬过的设置为1
		未爬过的设置为0
	每一次取url只需要从未爬过的取
	取出来设置状态为1
```

```python
import requests
from lxml import etree
from chaojiying import get_code
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
url = "http://www.renren.com/228113725/profile"
cookies = {
    "t":"d9b00f38123103075a85551d3e7f7bd92"
}
# 发送获取到的url
def send_url(url):
    res = requests.get("http://www.renren.com/"+url+"/profile",cookies=cookies).text
    ele = etree.HTML(res)
    try:
        name = ele.xpath("//title/text()")[0]
        print(name)
        if name == "人人网 - 验证码":
            check_code(ele)  # 破解验证码
        save_data(name)
        urls = ele.xpath("//div[@id='footprint-box']/ul/li/a/@namecard")
        for url in urls:
            try:
                save_url(url)
            except:
                pass
    except:
        pass
# 检测获取到验证码
def check_code(ele):
    image_url = ele.xpath("//div[@class='optional']/img/@src")[0]  # 获取图片
    im = requests.get(image_url, cookies=cookies).content  # 拿到图片的二进制流
    with open("1.jpg", "wb") as w:
        w.write(im)
    code = get_code(im).get("pic_str")
    data = {
        'id': '880792860',
        'icode': code,
        'submit': '继续浏览',
        'requestToken': '-1330999392',
        '_rtk': '7c6b8dfa',
    }
    requests.post("http://www.renren.com/validateuser.do", data=data, cookies=cookies)
# 保存数据
def save_data(name):
    sql = "insert into renren_data values (%s)"
    cursor.execute(sql,[name])
# 保存抓取下来的url
def save_url(url):
    sql = "insert into renren_url values(%s,%s)"
    cursor.execute(sql,(url,"0"))
    conn.commit()
# 从数据库中取值
def get_url():
    sql = "select url from renren_url where flag=%s"  # 从数据库中取出一个状态为0的url
    cursor.execute(sql,['0'])
    url = cursor.fetchone()[0]
    sql = "update renren_url set flag=%s where url=%s"  # 设置取出来的url状态为1
    cursor.execute(sql,['1',url])
    send_url(url)
    conn.commit()
if __name__ == '__main__':
    while True: # 循环获取url
        get_url()
```

### ip代理池

```markdown
存放可用ip的容器
1. 应该有什么方法
		取ip
		存ip
		删除ip
		检测ip（定时，定量）
2. 应该有什么属性
		阈值
		数据库的连接对象
和爬虫逻辑分开
```

### 为什么要用ip代理池

```markdown
1. 无论是免费网站还是收费网站，ip的可用性都不是100%
		需要定时定量检测ip的可用性
2. 维护方便
		每个人都有自己的习惯--- 学习思路（思想）
```

```python
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
```

### 作业

```markdown
1. 人人网： 基本信息数据5000条
2. 封装自己的ip代理池
3. 选做（携程国际港澳台机票）爬下来就行【管培生必做】
4. 查长期作业： 10w条  假期之后查 （数据量：不能重复）
```

