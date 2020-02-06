import json

import MySQLdb
import requests
url= 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='book',
        charset='utf8'
    )

p = 1
ann = 0
data={
'page': str(p),
'rows': '20',
'annNum': str(ann),
'annType':'',
'tmType':' ',
'coowner':' ',
'recUserName':' ',
'allowUserName':' ',
'byAllowUserName':' ',
'appId':' ',
'appIdZhiquan':' ',
'bfchangedAgengedName':' ',
'changeLastName':' ',
'transferUserName':' ',
'acceptUserName':' ',
'regName':' ',
'tmName':' ',
'intCls':' ',
'fileType':' ',
'totalYOrN':' true',
'appDateBegin':' ',
'appDateEnd':' ',
'agentName': ''
}
while True:
    ann+=1
    data['annNum']=str(ann)
    while True:
        res = requests.post(url,headers=headers,data=data)
        p+=1
        data['page']=str(p)
        r = json.loads(res.text)
        for i in r['rows']:
            try :
                print(i['tm_name'])
                print(i['reg_name'])
                print(i['reg_num'])
                print(i['ann_date'],'----------------------------')
                cur = conn.cursor()
                sql = 'insert into shangbiao(reg_num,tm_name,reg_name,ann_date)  values (%s,%s,%s,%s) '
                cur.execute(sql, (i['reg_num'],i['tm_name'],i['reg_name'],i['ann_date']))
                conn.commit()
                cur.close()
            except:
                pass
        if len(r['rows'])<20:
            print('下一期')
            p=1
            data['page']=str(p)
            break