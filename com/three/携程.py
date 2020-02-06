import requests
url='https://flights.ctrip.com/international/search/oneway-bjs-tyo?depdate=2019-12-31&cabin=y_s&adult=1&child=0&infant=0&searchid=j106013813-1577713953395-1379087MC-0'
res = requests.get(url).text
print(res)