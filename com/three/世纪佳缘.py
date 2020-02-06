import requests
import json
url='https://search.jiayuan.com/v2/search_v2.php'
import re
headers={
    'cookie':'guider_quick_search=on; accessID=20191227171821260717; SESSION_HASH=d6e75a79db49c9671d0ef58246ec88782a5c5d19; user_access=1; PHPSESSID=b32e3da24c9711721528803b5db866b1; pop_avatar=1; stadate1=231916735; myloc=11%7C1102; myage=22; PROFILE=232916735%3A%25E6%2588%2591%25E5%258F%25AB%25E5%25BC%25A0%25E5%2587%25AF%25203%25E5%258E%2598%25E7%25B1%25B3%3Am%3Aimages1.jyimg.com%2Fw4%2Fglobal%2Fi%3A0%3A%3A1%3Azwzp_m.jpg%3A1%3A1%3A50%3A10%3A3; mysex=m; myuid=231916735; myincome=60; main_search:232916735=%7C%7C%7C00; RAW_HASH=fsnPOO%2A6lZFB2PnD3zzflDd87JlpiYOYisKJhrtWSUWj6RwKPKOwzpWVxg9CJHeZAuQvdZcIDVQ3PPEcKa4%2ADJcgm7fZOgRohByist63xIAtSYg.; COMMON_HASH=fee0b6650e0caf84a3c8218001a424eb; pop_time=1577448191091; is_searchv2=1; sk=%E8%80%81%E5%B8%88; skhistory_f=a%3A1%3A%7Bi%3A1577448194%3Bs%3A6%3A%22%E8%80%81%E5%B8%88%22%3B%7D'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
num=1
data={
    'sex':'f',
    'key':'老师',
    'listStyle':'bigPhoto',
    'f':'select',
    'pri_uid':'232916735',
    'jsversion':'v5',
    'p':str(num),
    'sn':'default',
    'sv':'1'
}
rule='##jiayser##(.*?)##jiayser##'
while 1:
    res = requests.get(url,headers=headers,params=data).text
    print(res)
    num+=1
    data['p']=str(num)
    r=json.loads(re.findall(rule,res)[0])
    for i in r['userInfo']:
        print(i['nickname'])
        print(i['age'])
        print(i['sex'])
        print(i['matchCondition'])
        print(i['height'])
        print(i['marriage'])
        print(i['work_location'])
        print(i['education'])






