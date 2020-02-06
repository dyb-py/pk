from urllib import request,parse
import json
import MySQLdb
head={
    "Host": "sp0.baidu.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=95943715_hao_pg&wd=%E8%80%81%E8%B5%96&oq=%25E8%2580%2581%25E8%25B5%2596&rsv_pq=ec5e631d0003d8eb&rsv_t=b295wWZB5DEWWt%2FICZvMsf2TZJVPmof2YpTR0MpCszb28dLtEQmdjyBEidZohtPIr%2FBmMrB3&rqlang=cn&rsv_enter=0&prefixsug=%25E8%2580%2581%25E8%25B5%2596&rsp=0&rsv_sug9=es_0_1&rsv_sug=9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8"
    }
conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='book',
        charset='utf8'
    )



name=['郭','王','李','张','赵','刘','陈','杨','吴','黄','朱','孙','胡','吕','高','宋','徐','程','林','郑','范','何','韩','曹','马','许','田','冯','杜','周','曾','汪','苏','董','方','蔡','梁','石','谢','贾','薛','彭','崔','唐','潘','邓','任','史','钱','侯','魏','罗','叶','沈','孟','姚','傅','丁','章','萧','蒋','卢','陆','袁','江','晁','谭','邵','欧阳','孔','俞','尹','廖','阎','洪','夏','雷','葛','文','柳','陶','毛','丘','龚','康','蒲','邢','郝','庞','安','裴','折','施','游','金','邹','汤','虞','严','钟']
c=0
n=0
while c<len(name):
    data={
     'iname':name[c]
    }
    c+=1
    data=bytes(parse.urlencode(data),encoding='utf-8')
    url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&areaName=&ie=utf-8&oe=utf-8&format=json&t=1577192471810'
    req = request.Request(url,headers=head)
    res = json.loads(request.urlopen(req,data=data).read().decode())

    for i in res['data'][0]['result']:
        print(n)
        n+=1
        print(i['iname'])
        print(i['cardNum'])
        print(i['areaName'])
        print(i['caseCode'])
        print(i['performance'])
        # try:
        #     cur = conn.cursor()
        #     sql = "insert into shixin(iname,cardNum,areaName,caseCode,performance)values(%s,%s,%s,%s,%s) "
        #     cur.execute(sql, (i['iname'],i['cardNum'],i['areaName'],i['caseCode'],i['performance']))
        #     conn.commit()
        #     cur.close()
        # except:
        #     pass
conn.close()
