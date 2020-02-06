import pymongo
import requests
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
# 创建一个连接对象方式1
conn = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# 选择使用哪个数据库
mydb = conn['spider']  # use 数据库
# 选择使用哪个集合
myset = mydb['hero']  # 选择使用哪个集合
res = requests.get(url).json()
list1 = []
for heros in res['hero']:
    list1.append({"name":heros['name']})
myset.insert(list1)  # 存储

datas = myset.find()  # 可迭代的游标对象
for data in datas:
    print(data)
