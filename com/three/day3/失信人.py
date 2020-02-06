from urllib import request,parse
import json
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Referer": "https://www.baidu.com/s?ie=UTF-8&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA"
}
s = "赵钱孙李周吴郑吴"
for i in s:
    data = {
    'resource_id':'6899',
    'query':'失信被执行人名单',
    'cardNum':'1',
    'iname':i,
    'areaName':'北京',
    'ie':'utf-8',
    'oe':'utf-8',
    'format':'json',
    't':'1577238207995',
    'cb':'jQuery110206755767511303314_1577238165304',
    '_':'1577238165307',
    }
    data = parse.urlencode(data)
    url+=data

    req = request.Request(url,headers=headers)
    result = request.urlopen(req).read().decode()
    print(json.loads(result[46:-2]))