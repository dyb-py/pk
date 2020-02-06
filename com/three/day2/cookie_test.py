from urllib import request

# url = "http://www.httpbin.org/cookies"
# headers = {
# 'Cookie':'BAIDUID=A56424D93AAEF8FA4BC9A42FB823A3D3:FG=1; BIDUPSID=A56424D93AAEF8FA4BC9A42FB823A3D3; PSTM=1571306136; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=80187_0_7_9_1_2_0_0_6_2_74_0_0_0_99_0_1577153193_0_1577153292%7C9%2326_7_1577065117%7C4; delPer=0; BD_HOME=0; H_PS_PSSID=1438_21123_30211_30284; BD_CK_SAM=1; PSINO=2; H_PS_645EC=c6c13NdgtEPBs25xHIjjlRy%2Br9ObXP15O3%2FG38SswgRzJmrrR8RTaYSpQnw; BDSVRTM=162'
# }
# req = request.Request(url)
# res = request.urlopen(req).read().decode()
# print(res)
from urllib import request
from http.cookiejar import CookieJar
cookiejar = CookieJar() # 保存的是response cookie
handler = request.HTTPCookieProcessor(cookiejar)  # cookie handler
print(cookiejar)
opener = request.build_opener(handler)
url = "http://www.renren.com/972685182"
res = opener.open(url).read().decode()
# print(res)
print(cookiejar)
# headers = {
#     "Cookie":"anonymid=k4jantmb6l5i7o; depovince=BJ; _r01_=1; JSESSIONID=abctwXeqlCIyQ5PRk518w; ick_login=18c9a04b-b52e-42c8-9967-e6701570849d; t=b1cf4728fbc1b8705c85b4efc1b69d462; societyguester=b1cf4728fbc1b8705c85b4efc1b69d462; id=972685182; xnsid=ca1b0649; jebecookies=4e5b6680-17c1-46b8-be99-57b22a170082|||||; ver=7.0; loginfrom=null; jebe_key=3aba2334-a23d-4d7a-a82f-e385f5ec289f%7Cc06fd7b330d1b34a3b663a70fd4e85c3%7C1577157199724%7C1%7C1577157086589; jebe_key=3aba2334-a23d-4d7a-a82f-e385f5ec289f%7Cc06fd7b330d1b34a3b663a70fd4e85c3%7C1577157199724%7C1%7C1577157086596; wp_fold=0"
# }
# req = request.Request(url,headers=headers)
# res = request.urlopen(req).read().decode()
# print(res)