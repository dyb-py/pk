import pymongo
# 创建一个连接对象方式1
# conn = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# 创建连接对象方式2
conn = pymongo.MongoClient(host="localhost",port=27017)

# 选择使用哪个数据库
mydb = conn['duanwei']  # use 数据库
# 选择使用哪个集合
myset = mydb['selina']  # 选择使用哪个集合
# 增
myset.insert([{"name":"瑟琳娜2号","age":"28","sex":"女孩子","like":"爬虫","_id":"4"},
            {"name":"马尔斯","age":"19","sex":"男","like":"被爬","_id":"2"},
            {"name":"卡西奥","age":"24","sex":"爷们","like":"写BUG","_id":"3"}
              ])
# 删
# 删集合
mydb.drop_collection("emily") # 删集合
# 删库
conn.drop_database("test")
# 删数据
myset.remove('2')  # 删除id为2的
# 改
myset.update({"name":"瑟琳娜2号"},{"哈哈":"变了吧"})  # 第一个参数是筛选的条件，第二个参数是修改的内容
myset.update({"name":"瑟琳娜2号"},{"$set":{"sex":"老爷们"}})  # 指定某个字段改变
#查
datas = myset.find()  # 可迭代的游标对象
for data in datas:
    print(data)
















