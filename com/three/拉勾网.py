import json

import MySQLdb
import requests
import time
u='https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py'
u1='https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py'
url='https://www.lagou.com/jobs/positionAjax.json?city={0}&needAddtionalResult=false'
headers={
'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}
conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='book',
        charset='utf8'
    )
serech=['会计']
city=['北京','上海','广州','深圳','太原','杭州','南京','青岛','郑州']
num=0
data = {
    'first': 'false',
    'pn': str(num),
    'kd': 'c++'
    }
session = requests.session()
session.get(url=u,headers=headers)
for i in serech:
    data['kd']=i
    for j in city:
        print(i,j,'-----------------------------------')
        num = 0
        while 1:
            data['pn']=str(num)
            res=session.post(url.format(j),headers=headers,data=data)
            num+=1
            print(session.cookies)
            if '频繁'in res.text:
                session.cookies.clear()
                time.sleep(5)
                session.get(url=u,headers=headers)
                continue
            try:
                r=json.loads(res.text)
                for a in r['content']['positionResult']['result']:
                    print(a['companyFullName'])
                    print(a['positionName'])
                    print(a['salary'])
                    cur = conn.cursor()
                    sql = 'insert into job(company,jobname,salary) values (%s,%s,%s) '
                    cur.execute(sql, (a['companyFullName'],a['positionName'], a['salary']))
                    conn.commit()
                    cur.close()
                if len(r['content']['positionResult']['result'])<15:
                    break
            except:
                pass