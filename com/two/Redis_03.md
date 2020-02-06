# Python-Redis

### 一、安装模块

在虚拟环境中安装以下几个模块：

- `pip install redis ` #安装redis模块
- `pip install redis-py-cluster` #支持python连接redis集群
- `pip install django-redis` #支持django
- 补充：一旦pip 出现 问题，使用pypi社区 最新 pip tar包；下载tar包完毕之后，进行解压，cd到解压目录，执行 `python setup.py install`即可



### 二、连接Redis

#### 1、连接

```python
from redis import 

red = Redis(host='192.168.134.124',port=8000)    # 连接redis数据库
```

```python
red.set("name","houqn")
red.set("age",18)

age = red.get("age")
print(age)

red.lpush("hobbys","football","basketball")
hobby = red.lrange("hobbys",0,-1)
print(hobby)
```

#### 2、Json序列化存储

```
序列化过程：获取Model数据 -> 序列化为json字符串 -> set存储到redis数据库
```

```python
import json
from redis import Redis
from datetime import datetime

red = Redis(host='192.168.134.124',port=8000)    # 连接redis数据库

def mydefault(u):
    if isinstance(u,User):
        return {"name":u.name,'age':u.age,'salary':u.salary,'birthday':u.birthday.strftime('%Y-%m-%d')}

users = list(User.objects.all())                 # 查询mysql数据库中的user->QuerySet，并转为list
user_dump = json.dumps(users,default=mydefault)  # 将model数据 转为 json字符串

print(user_dump)
red.set('userlist',user_dump)      # 将json字符串以key-value的形式存储到redis中
```

#### 3、反序列化

```
反序列化过程：获取redis数据库中的数据get -> json字符串 -> 提取字符串中的数据（反序列化）  -> Model对象
```

```python
def parsedefault(dic):   # u为list中的一个个dict
    # dic['birthday'] = datetime.strptime(dic['birthday'],'%Y-%m-%d')
    # dic['salary'] = Decimal(dic['salary'])
    return User(name=dic['name'],age=dic['age'],salary=dic['salary'],birthday=dic['birthday'])

res = red.get("userlist")  # 返回bytes 需转为str   b"xxx".decode("utf-8") -> str
results = json.loads(res.decode("utf-8"),object_hook=parsedefault)
print(results)
```



### 三、Python-Redis集群

```python
from rediscluster import RedisCluster

cluster_nodes = [
    {'host': '192.168.134.124', 'port': 7001},
    {'host': '192.168.134.124', 'port': 7002},
    {'host': '192.168.134.124', 'port': 7003},
    {'host': '192.168.134.124', 'port': 7004},
    {'host': '192.168.134.124', 'port': 7005},
    {'host': '192.168.134.124', 'port': 7006},
]

cluster = RedisCluster(startup_nodes=cluster_nodes)
cluster.set('name','houqn')  # key 0-16383 
```



### 四、Django-Redis缓存 

#### 1、缓存的概念   

在实际Web开发中，经常需要在客户端和服务器端进行数据传输：

- 客户端发送请求，服务器端接收请求，返回数据

- 而在返回数据之前，我们要对数据库进行查询操作，找到正确的请求内容
- 如果要查找的数据量比较大，每次请求的耗时将会是一个非常可怕的事情。
- 这个时候，我们就需要对某些无需实时更新的内容进行缓存处理，把要返回的内容存放在缓存中，收到数据请求后直接把缓存中的数据返回，如果缓存不存在，则查询数据库，并且把内容添加进缓存中，以便下次请求使用。

简单来说：**缓存就是把一些查询频繁且改动较少的数据，放入一个内存区域临时存储，进而在一定程度上改善查询的性能。**



#### 2、缓存流程

初次查询，依然找到磁盘数据库，然后会将查询结果返回并纳入缓存；

之后的每次相同的查询都可以直接从缓存取数据，则可以达到 “较少与磁盘数据库通信次数” 的目的。

如果缓存失效，则再次回到数据库查询，并存入缓存。重复上述过程

`数据存储在Mysql中，查询到数据后，返回给客户端，同时将数据存储入redis数据库中（redis就是内存数据库）`





#### 3、Redis缓存配置 

##### 3.1 安装django-redis

`pip install django-redis`

##### 3.2 设置缓存

在Django项目的settings.py中添加如下设置：

```python
CACHES = {
      "default": {
         "BACKEND": "django_redis.cache.RedisCache", #Redis缓存入口，其中使用DefaultClient操作缓存
         "LOCATION": "redis://192.168.134.124:8000/3", #ip:port/db_index
         "OPTIONS": {
           "CLIENT_CLASS": "django_redis.client.DefaultClient" #操作缓存的对象
         }
      }
}
```



#### 4、view缓存 

实际要缓存的应该是查询到的数据，但是数据最终会通过模板文件html来显示

view缓存是将整个的模板文件加入到缓存中

```python
@cache_page(timeout=10,key_prefix="cacheRedis")    # timeout 缓存时效(秒)
def index(request):
    users = User.objects.all()
    return render(request,'redis_app/index.html',{"users":users})
```

加在会渲染模板的视图函数上，会将整个模板的渲染结果存入缓存



#### 5、template缓存

在模板中使用缓存，可以充分考虑缓存的颗粒度，细分颗粒度，可以保存只缓存部分HTML片段，而不是整个模板文件。

```python
<!DOCTYPE html>
{% load cache %}            # 加载cache
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  
    {% cache 100 cache_1 %}    # 要缓存的区域--开始   缓存时间100s

        {% for u in users %}
             {{ u.name }}
        {% endfor %}

    {% endcache %}               # 要缓存的区域--结束

    </body>
</html>
```



#### 6、缓存删除

当数据库的数据发生改动时，需要删除缓存

```python
from django.core.cache import cache
---------------------------------------------------------------------
keys = cache.keys("*abc*")#获取包含abc的所有key

for key in keys: #遍历key
	cache.delete(key) #删除某个key
-----------------------------------------------------------------------
cache.delete_many(keys) #删除多个key
---------------------------------------------------------------  
cache.delete_pattern("*abc*") #删除包含abc的所有key
---------------------------------------------------------------  
cache.clear() #清空当前db的所有key
```



#### 7、Session存储

~~~python
session：服务器生成 
		request.session['login'] = 'ok'
    	服务器端保存 django项目 session 表 session_key data expires
~~~



将session存入缓存，可以提高session数据的交互效率

```python
#django.contrib.sessions.backends.cached_db -- 缓存和数据库中并存
SESSION_ENGINE='django.contrib.sessions.backends.cache' #存于缓存
```

