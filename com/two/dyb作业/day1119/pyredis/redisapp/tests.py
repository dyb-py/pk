
# 环境搭建 os django 关联当前django项目

# 普通py文件使用
# from redis import Redis
#
# # 建立连接 创建redis对象
# redis = Redis(host='192.168.174.128',port=7000)
# print(redis)
# mysql操作 获取cursor对象 进行 execute()
# redis.set('name','liuzong123456')
# redis.lpush('list1',10,20,30,40)
# 读取
# print(redis.get('name').decode('utf-8')) # b 二进制字符串
# print(type(redis.lrange('list1',0,-1)))


'''
django项目 ORM机制 model mysql数据
Model类 表 model对象 orm机制 映射到 数据库 生成表保存
model对象 保存在redis数据库 
'''


'''
以下 进行数据手动添加
'''
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyredis.settings")
django.setup()
from datetime import datetime
from redisapp.models import User
from redis import Redis
import json
# 添加
# User.objects.create(name='sunge',age=18,salary=1000,birthday=datetime.now())
# User.objects.create(name='liuzong',age=19,salary=2000,birthday=datetime.now())
# User.objects.create(name='jianhui',age=20,salary=3000,birthday=datetime.now())
# User.objects.create(name='zhangjingtai',age=21,salary=4000,birthday=datetime.now())
# User.objects.create(name='zhangxingxing',age=22,salary=5000,birthday=datetime.now())
# User.objects.create(name='songqi',age=23,salary=6000,birthday=datetime.now())
# User.objects.create(name='刘锟',age=23,salary=6000,birthday=datetime.now())

# 验证是否添加成功
# 查询
users = User.objects.all()
# print(users[6].name)

# 把当前 users queryset 保存在 redis数据库中
# 连接数据库
redis = Redis(host='192.168.174.128',port=7000)
#
'''
def mydefault(u):
     if isinstance(u,User):
         return {'id':u.id,'name':u.name,'age':u.age,'salary':str(u.salary),'birthday':u.birthday.strftime('%Y-%m-%d')}
# # json序列化工作
rst = json.dumps(list(users),default=mydefault)
# # print(rst,type(rst))
redis.set('users',rst)
'''

'''
以下要进行 反序列化
从redis数据库中 读取 json字符串
'''
# rst = redis.get('users')
# # print(rst.decode('utf-8')) # 字符串类型
#
# # 最终完成 model对象
# # json模块 dumps() model对象 - json串
# # json模块 loads()  json串- python对象
# def objhook(d):
#     print(d)
#     return User(**d)
# # User(name=dic['name'],age=dic['age'],salary=dic['salary'],birthday=dic['birthday'])
# rstobj = json.loads(rst.decode('utf-8'),object_hook=objhook)
# print(rstobj,type(rstobj))
# # model对象


'''
ajax
    后端接收到请求，返回响应，不是简单字符串，而是model对象 queryset对象
    json模块 dumps() json序列化 成json串 返回响应
    前端 进行接收 原生js json串 JSON.parse(json串) 成为 js原生对象
'''

# 查询工作
# print(users[1].age)