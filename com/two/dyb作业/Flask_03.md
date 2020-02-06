# Flask_03

### 一、蓝图

#### 1、简介

一个Web项目，会有很多个模块，如用户管理、部门管理、账号管理等模块 ，如果把所有的这些模块都放在一个app.py文件之中，那么最后app.py文件必然臃肿不堪，并且极难维护 。因此flask中便有了blueprint的概念。

`在Django中使用app来对项目进行模块化管理，解耦合，利于项目管理和维护`。



#### 2、如何搭建项目结构

![structure1](.\Flask-pic\structure1.png) 

![structure2](.\Flask-pic\structure2.png) 



❶ 在project的根目录下创建包app，容纳各个项目模块(admin/employee)+static+templates

❷ 每个模块定义自己的蓝图，将项目的不同模块分在不同的package中(admin/employee)

❸ 在app包的init文件中初始化Flask环境 : 如Flask对象和SQLAlchemy对象和Session对象,蓝图注册，app.config.from_project(Config)

❹ app目录成为template和static的root_path，所以将static和templates目录放在app目录下

❺ models.py依然作为项目的模型文件，也放在app目录下

❻ config.py作为整个project的配置文件，存放配置信息：mysql连接参数，session配置参数等

❼ run.py作为启动文件，负责：`app.run()` 



```python
#-- app.py --#
from app import app

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

```python
#-- config.py --#
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

```python
#-- app - init.py --#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
```



#### 3、蓝图的使用

##### 3.1 view中声明

在每个模块中，定义自己的蓝图

```python
from flask import Blueprint, render_template
#                      蓝图名   模块名   前缀
admin_blue = Blueprint("admin",__name__,url_prefix='/admin')   # 声明蓝图
	

@admin_blue.route("/login/")      # 使用蓝图对象配置路由  不再使用app.route
def login():
    return render_template("admin/login.html")


@admin_blue.route("/login_logic/",methods=['post'])
def login_logic():
    return ""

注：之后url_for()软编码路径，需要 admin.login_logic
```

##### 3.2  注册蓝图

在应用程序的初始化文件中，加入以下代码：

```python
# -- app/__init__.py --#
...
...
from app.admin.views import admin_blue    # 引入各个模块中的蓝图
from app.emp.views import emp_blue
app.register_blueprint(admin_blue)    # 注册蓝图
app.register_blueprint(emp_blue)
```



### 二、状态保持

#### 1、Cookie

##### 1.1 简介

Http协议是一种无状态的协议，什么叫无状态，就是本次的客户端请求不会保留上一次客户端请求的状态，简单点说就是这样会要求我们每次在浏览器中点开一个网站的链接都会输一次账户和密码。cookie就是用来解决这个问题的。



##### 1.2 Cookie的使用

- 在服务器生成cookie，随着响应到达浏览器随之存储在浏览器的小段数据
- 保持数据，使得数据在一段时间之内，可以反复使用**(记住我)**
- cookie会随着后续的每一个请求，再次回到服务器
- 向服务器发送请求时，会自动携带来自该服务器的所有cookie

```python
@app.route("/cook/")
def testcookie(): #写
    response = make_response(render_template("xxx.html")) # 获得response
    # response = make_response("Hello World~~") # 获得response
    # 设置cookie,如果不设置max_age,则为会话cookie
    response.set_cookie("name","lilei",max_age=60*10) #设置一个10min的cookie
    return response

@app.route("/cook2/")
def testcookie2(): #读
    print(request.cookies.get("name")) #获取cookie
    return "aaa"

@app.route("/cook3/")
def testcookie3():#删
    response = make_response("hello") #获得response
    # response.delete_cookie('name') #删除cookie
    response.set_cookie("name",max_age=0) #删除cookie
    return response
```



#### 2、Session 

Session 对象存储特定用户会话所需的属性及配置信息。这样，当用户在应用程序的 Web 页之间跳转时，存储在 Session 对象中的变量将不会丢失，而是在整个用户会话中一直存在下去。 



##### 2.1 客户端session

flask默认的session处理是将session存在cookie中：“客户端session”。

```python
import os
os.urandom(20) # 获得一个随机的key
```

```python
from flask import session
app.secret_key=b'\x19M\xf1\xb2<&\xe2\x16l\x81\xa7G\xe2\xf2"\x82\xe2 d,' # 设置加密cookie的密钥
...

@app.route('/setsession/')
def setsession():
    session['name']='lilei' # 数据会加密后存在客户端的cookie中
    
    return 'Hello World!'

@app.route('/getsession/')
def getsession():
    rst = session['name'] # 数据会加密后存在客户端的cookie中
    # rst = session.get('name') 
    
    return 'Hello World!'

@app.route('/delesession/')
def hello_world():
    session.pop('name')
    # session.clear() 清空所有session
    
    return 'Hello World!'
```

##### 2.2 服务器session

（1）准备工作 

安装flask扩展 `pip install flask-session` 帮助实现server-session（mysql、redis等）

（2）**session-mysql**

- **mysql配置**

```
from flask_session import Session
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:222222@localhost/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True #避免警告信息
db = SQLAlchemy(app) #构建SQLAlchemy对象
```

- **session配置**

```python
app.config["SESSION_TYPE"]="sqlalchemy" #session存储类型
app.config["SESSION_SQLALCHEMY"]=db #session存储时，可以使用的SQLAlchemy对象
app.config["SESSION_SQLALCHEMY_TABLE"]='sessions125' #存储session数据的数据表
# app.config["SESSION_PERMANENT"]=True # 不设置时，默认为True为一个月 

# 如果会话一直没有活动，30分钟sesison失效，仅适用于SESSION_PERMANENT=True时
# app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(60*30)

app.config["SESSION_USE_SIGNER"]=False #是否需要加密cookie
app.config["SESSION_KEY_PREFIX"]="xxx:" #sessionID的前缀（sessionid会存入数据库中会追加一个prefix）


# 在 init.py文件中构建Session
Session(app) #构建Session，则之后，在项目中可以使用session了

def hello_world(name):
    session['name']="lilei" #数据存入数据库
    return 'Hello World!'

def hello_world2(name):
    session['name'] #从session取数据
    return 'Hello World!'
```

注意，在使用session前，需要做一次 `db.create_all()` 保证sessions表被创建(ops:也可以自己手动建表)

```python
from app import db
db.create_all()
```



（3）**session-redis**

```python
app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_PERMANENT'] = False  # 关闭浏览器session就失效。

# 如果会话一直没有活动，30分钟sesison失效

# 在redis的解决方案中SESSION_PERMANENT=False和PERMANENT_SESSION_LIFETIME可以共存

app.config["PERMANENT_SESSION_LIFETIME"]=60*30
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'lilei:'  # 保存到session中的值的前缀

# 用于连接redis的配置  （ops: pip install redis）

app.config['SESSION_REDIS'] = redis.Redis(host='192.168.180.131', port='7000',db=1)  

Session(app) #构建Session

def hello_world(name):
    session['name']="lilei" #数据存入redis
    return 'Hello World!'
```



### 三、静态资源

flask静态资源根目录是 Flask初始化的目录下的static目录：

```python
<img src="/static/hello/app.png"/>

# /static/hello/app.png

<img src="{{ url_for('static',filename='hello/app.png')}}"/>

# 如下view时flask内置的veiw：用于反向解析到静态资源的路径

@app.route("/static/<filename>")
def static(filename):
    ....
```



### 四、响应Json 

```python
import json
@emp.route("/all",methods=['get'])
def query_all():
    users = User.query.all()
    def xx(a):
        if isinstance(a,User):
            return {"id":a.id,"age":a.age}
    return  json.dumps(users,default=xx)  # content-type = "text/html"
    或者
    #response = make_response(json.dumps(users,default=xx))
    #response.headers['content-type'] = 'application/json;charset=utf-8'
    #return response
    
```



```python
$.ajax({
    type:"get/post",
    url:".....",
    data:"xxx=xxx&xxx=xxx",
    #dataType:"json",  #如果响应头中有 content-type="application/json"，则此参数可省略
    success:function(a){...} #a==xhr.responseText 或 解析后javascript对象
})
```
```python
from flask import jsonify  #（了解）
@emp.route("/all",methods=['get'])
def query_all():
    # {"id":1,"name":"zhj"} ,自动设置了响应头：content-type=application/json
    return jsonify(id=1,name="lilei") 
    #return jsonify({"id":1,"name":"lilei"})
```
