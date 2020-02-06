from urllib import request
import time
from lxml import etree
url = "http://www.httpbin.org/ip"
#"124.64.16.94, 124.64.16.94"  #本机的
res = request.urlopen(url).read()
print(res)
# ip的格式：{'type':'ip:端口号'}
for i in range(1,6):
    daili_url = "https://www.kuaidaili.com/free/inha/"+str(i)+"/"
    res1 = request.urlopen(daili_url).read().decode()
    ele = etree.HTML(res1)
    IP = ele.xpath('//td[@data-title="IP"]/text()')
    PORT = ele.xpath('//td[@data-title="PORT"]/text()')
    TYPE = ele.xpath('//td[@data-title="类型"]/text()')
    proxy = {}
    for j in range(len(IP)):
        proxy[TYPE[j]] = IP[j]+":"+PORT[j]
        handler = request.ProxyHandler(proxy) # 构建一个代理handler
        opener = request.build_opener(handler)
        res2 = opener.open(url).read()
        print(proxy,res2)
        if res2 != res:  # 检测和主机IP地址是否一致
            with open("ip.txt","a",encoding="utf-8") as w:
                w.write(str(proxy)+"\n")
    time.sleep(2)