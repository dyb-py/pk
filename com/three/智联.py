import MySQLdb
import requests
import json
import time
url='https://fe-api.zhaopin.com/c/i/sou?'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Content-Type': 'application/json',
}
serech=['python','c++','web','爬虫','php','AI','java']
city=['北京','太原','杭州','南京','青岛','郑州']
conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='book',
        charset='utf8'
    )
for i in serech:
    for j in city:
        st=0
        data = {
            "start": st,
            "pageSize": '90',
            "cityId": j,
            "kw": i,
            "kt": '3',
            'at': "fe14d83f35994c818a196bfe5edcc2dd",
            'rt': "1fd79cae12564c71bae1b1ad07e2cb76",
            '_v': "0.80261598",
           'userCode': '1058590788',
            'workExperience': "-1",
            'education': "-1",
            'companyType': "-1",
            'employmentType': "-1",
            'jobWelfareTag': "-1"
        }
        while 1:
            try :
                print(j,i,'_____________________________________________')
                print(data)
                st+=90
                res=requests.get(url,headers=headers,params=data).text
                print(res)
                data['start']=st
                d=json.loads(res)
                # print(d)
                a=d['data']['results']
                for di in a :
                    print(di['company']['name'])
                    print(di['jobName'])
                    print(di['salary'])
                    cur = conn.cursor()
                    sql = 'insert into job(company,jobname,salary) values (%s,%s,%s) '
                    cur.execute(sql,(di['company']['name'],di['jobName'],di['salary']))
                    conn.commit()
                    cur.close()
                time.sleep(2)
                if len(a)<90:
                    break
            except:
                pass
conn.close()


