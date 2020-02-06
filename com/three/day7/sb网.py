import requests
import pymongo
conn = pymongo.MongoClient(host="localhost",port=27017)

# 选择使用哪个数据库
mydb = conn['sbw']  # use 数据库
# 选择使用哪个集合
myset = mydb['sb']  # 选择使用哪个集合
mydb.drop_collection("sb")
url = "http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
data = {
'page':'1',
'rows':'10',
'annNum':'1677',
'annType':'',
'tmType':'',
'coowner':'',
'recUserName':'',
'allowUserName':'',
'byAllowUserName':'',
'appId':'',
'appIdZhiquan':'',
'bfchangedAgengedName':'',
'changeLastName':'',
'transferUserName':'',
'acceptUserName':'',
'regName':'',
'tmName':'',
'intCls':'',
'fileType':'',
'totalYOrN':'true',
'appDateBegin':'',
'appDateEnd':'',
'agentName':'',
}

res = requests.post(url,data=data,headers=header).json()
for i in res['rows']:
    try:
        a=[]
        print(i['tm_name'])
        print(i['reg_name'])
        print(i['reg_num'])
        print(i['ann_date'], '----------------------------')
        a.append({'tm_name':i['tm_name'],'reg_name':i['reg_name'],'reg_num':i['reg_num'],'ann_date':i['ann_date']})
        print(a)
        myset.insert(a)
    except:
        pass
