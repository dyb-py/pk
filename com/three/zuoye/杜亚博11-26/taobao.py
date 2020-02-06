import requests
from lxml import etree
import json
import MySQLdb
import time
conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='book',
        charset='utf8'
    )

num=0
c=0
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'cookie':'alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; v=0; _tb_token_=3e151ae06154b; cna=MQuKFlhdmHQCAd9oAzqpLQ0g; uc3=nk2=synEbg%2FtG0fpK7c%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UUGmv79Ym1CerA%3D%3D&vt3=F8dByuquys8DZ%2BkwPmw%3D; csg=047c7a11; lgc=%5Cu5C0F%5Cu675C%5Cu5148%5Cu68EE007; t=f69efc701dfc6b17959ec14031d66aa9; dnk=%5Cu5C0F%5Cu675C%5Cu5148%5Cu68EE007; skt=81c66457ed14901a; cookie2=1c205451587b66a28fd3f624db9c53a9; existShop=MTU3NzI2MzgxNQ%3D%3D; uc4=id4=0%40U2OR9yQM%2BLssH1%2BvSh2HgAufBnl4&nk4=0%40sVZkw8IiPjtLMEXugehwZ3Rgvr7QuQ%3D%3D; tracknick=%5Cu5C0F%5Cu675C%5Cu5148%5Cu68EE007; _cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; enc=08JWmKXuTh3SSXS1dDShGH%2BPX6ImzFUhNYz52UCUSSUZtzSdVJ80ySBLHX%2F2dpOJPjIIXFz89wqK6V7z9pUXag%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=1_1; thw=cn; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTbmhI3owFmsA%3D%3D&tag=8&lng=zh_CN; x5sec=7b227365617263686170703b32223a223464336166643738326538643239343135356164613133666136396634633331434966446a664146454c69756d50727576712b7368414561444449354e4445784e6a51354e5463374e673d3d227d; JSESSIONID=433ABB8401771CEFCB3340DF098E225E; l=cBOJT0ScQO5wiGCWBOfwGuIRXgQt6UAjcsPzw4ZQxIB1TisK9pq-QHwUdHqJW3QQE9fE3HtyV9gbWRe95iaKg-rGdW7dYVC1.; isg=BLm5dcDbw6tl958_Vq7cBbRhyCVTbobUD8LPW9v0vOnAYsX0MxSaSGB05CYxWkWw',
    'referer':'https://s.taobao.com/list?spm=a217f.8051907.249291-static.1.68213308PoxHUn&q=%E8%BF%9E%E8%A1%A3%E8%A3%99&style=grid&seller_type=taobao&cps=yes&cat=51108009&bcoffset=0&s=0'}
s = requests.session()
while 1:
    time.sleep(3)
    url='https://s.taobao.com/list?data-key=s&data-value=60&ajax=true&_ksTS=1577280157701_4205&callback=jsonp4206&q=%E5%A5%B3%E8%A3%85&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1&bcoffset=0&s='+str(num)
    num+=60
    res = s.get(url,headers=headers).text
    print(res[12:-2])
    try:
        r=json.loads(res[12:-2])
        cars=r['mods']['itemlist']['data']['auctions']
        for i in cars:
            c+=1
            print(i['raw_title'])
            print(i['view_price'])
            print(i['item_loc'])
            print(c)
            try:
                cur = conn.cursor()
                sql='insert into car(name,local,price) values (%s,%s,%s)'
                cur.execute(sql,(i['raw_title'],i['item_loc'],i['view_price']))
                conn.commit()
                cur.close()
            except:
                pass
    except:
        pass

cur.close()


