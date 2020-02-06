## MongoDB

```markdown
MongoDB 是介于关系型和非关系型数据库之间的数据库。
		MongoDB支持的数据比较松散。可以是json，bson（二进制的json），可以存储一些比较复杂的数据。几乎可以实现关系型数据库的查询的大多数功能。
特点：	
	1. 高性能
		查询和写入皆基于内存
	2. 易部署
		使用安装包安装即可（.msi）
	3. 易使用
		在查询时和关系型数据库很像
```

### 安装MongoDB

```markdown
1. 安装包安装 --- 傻瓜式安装   .msi文件
2. 提供好的安装包
安装过程
1. 创建一个文件夹MonogoDB，在MonogoDB下面创建两个文件夹
		1. mongoDB 
			存放bin目录下面相关组件的
			把压缩包里的内容扔进去即可
		2. MongoData
			存放mongodb数据的文件夹
2. 进入bin目录下，在命令行里输入：
		mongod.exe --dbpath MongoData所在的目录
		注意：不要关掉此命令行
3. 再开一个命令行，在bin目录下输入：mongo  即可进入mongo环境
4. 在2，3步之前最好配置环境变量，就可以不需进入bin目录操作。
	mongodb的默认端口号：27017
```

### MongoDB的基本操作

```markdown
1. 数据库的操作
        db ： 当前指向的数据库
        show dbs:展示所有的数据库
        use 数据库名：改变数据库指向
            在use数据库的时候，如果没有该库，不会直接创建该库，直到往该库中添加数据才会创建
        db.dropDatabase()  删除当前指向的库
2. 集合操作
        创建一个集合：db.createCollection("集合名")  
        查看所有集合：show collections
        向集合中添加元素：db.集合名.insert（json串）
        查看集合中的元素：db.集合名.find()
        向集合中添加多个元素：db.集合名.insertMany([json1,json2,json3,...])
3. 查询操作
		1. db.集合名.find(【查询条件】)默认无条件查询 ：查询所有的json数据
					全集合查询
		2. findOne(【查询条件】) 查询第一个符合条件的json
	查询条件：
		1. 比较运算符
			等于：$eq :equle  
			小于：$lt :little than
			大于：$gt :granter than
			大于等于:$gte 
			小于等于：$lte
			不等于:$ne
		2. 逻辑运算符
			逻辑与：and
			逻辑或：or
			逻辑非：not
	db.集合名.find({筛选字段:{筛选规则:值}})
	例：查询年龄大于18的信息：
		db.emily.find({age:{$gt:18}})
	查询年龄在100（包含）-120（包含）之间的数据
		db.emily.find({age:{$gte:100,$lte:120}})
	查询年龄小于120岁且性别为girl的人
		db.emily.find({$and:[{age:{$lt:120},sex:{$eq:"girl"}]})
	查询名字不是duanwei1的人
		db.emily.find({name:{$not:{$eq:'duanwei1'}}})
	# 双重否定---查询名字不是不是duanwei1的人
		db.emily.find({name:{$not:{$not:{$eq:'duanwei1'}}})
```

### python连接mongodb

```markdown
pymongo 是一个第三方库
	是python连接mongo的一个库
	pip install pymongo
```

```python
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
```

```python
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
```













