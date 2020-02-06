# Flask_01 

### 一、简介

Flask是一个Python语言编写的Web 微框架，让我们可以使用Python语言快速实现一个网站或Web服务 。

Flask是一个轻量级的框架，而Django是一个重量级的框架      

Flask的轻量级表现在它的核心实现简单，不会附带很多库和功能，但同时可以让开发人员自由地去扩展这些功能

而Django的重量级表现在本身附带了很多功能实现，比如Django中有自己的DTL，ORM

“微”并不代表整个应用只能塞在一个 Python 文件内， 当然塞在单一文件内也没有问题。 “微”也不代表 Flask 功能不强或有所欠缺。 微框架中的“微”字表示 Flask 的目标是保持核心简单而又可扩展，给开发人员足够的自由。

默认情况下，Flask 不包含数据库抽象层、表单验证，或是其它任何已有多种库可以胜任的功能。然而，Flask 支持用扩展来给应用添加这些功能。 

Flask 也许是“微小”的，但它已准备好在需求繁杂的生产环境中投入使用。



### 二、安装 

首先创建一个新的虚拟环境

在虚拟环境中`pip install flask` 即可！

Flask 依赖两个外部库：Werkzeug 和 Jinja2 。 Werkzeug 是一个 WSGI（在 Web 应用和多种服务器之间的标准 Python 接口) 工具集。Jinja负责渲染模板。 



### 三、快速上手

#### 1、第一个Flask程序

```python
from flask import Flask

app = Flask(__name__) # 初始化application实例，将成为核心对象，负责管理整个应用，处理所有请求。view， 
                      # urlConf等等都要注册于Flask对象。
    

@app.route('/')       # route()装饰器 告诉Flask 触发函数的url
def hello_world():
    #a=10/0               # 如果是调试模式开启，可以看到详细的错误信息
    return 'Hello World!' # 返回值即为响应内容，将显示在用户的浏览器上 -> Django-HttpResponse

if __name__ == '__main__':
    #app.run()  # 启动内置的WSGI服务器，启动后即可接受外界用户的访问了
    app.run(debug=True,host="localhost",port=9000)  
    #注意：开启了调试模式后，当程序出错时，可以在浏览器看到更详尽的信息
```

**坑：** `Pycharm2018版本，设置debug、host、port等参数无效解决方案`

- 点击Pycharm右上角运行按钮左边的项目名称  -- 下拉按钮 -- Edit Configurations  

![1535035617083](.\Flask-pic\Pycharm设置debug)



#### 2、运行

##### 2.1 使用Pycharm

选择菜单项`Run -> Run `即可：

![1532862770217](.\Flask-pic\1532862770217.png)



```python
FLASK_APP = app.py       # FLASK_APP环境变量被用来指定如何加载应用程序。 

FLASK_ENV = development  # Flask应用运行的环境是由FLASK_ENV环境变量设置的。如果没有设置它，默认                                 为production。其他认可的环境是development。 
                         # 如果env被设置为development，flask命令会开启调试模式，并且flask run会开启                             交互式调试器(debugger)和重载器(reloading)。
    
FLASK_DEBUG = 1          # 当FLASK_ENV为development时，调试模式被开启。如果你希望单独地控制调试模                               式，使用FLASK_DEBUG可以办到：设为1表示开启调试模式，0标识禁用它。
```

 

##### 2.2  在Terminal中运行（了解）

`(TestDemo) E:\Python Web\Python-Web-Lee\09 Flask\Flask-Codes\Demo01 >`

- `set FLASK_APP=app.py `

- `set FLASK_ENV=development`

- `python -m flask run --port=9999`

![1532864128100](.\Flask-pic\1532864128100.png)



### 四、路由URLConf

在Flask程序中，使用`route() `装饰器把一个函数绑定到对应的 URL 上 。

注：url中最前面的/必须写，末尾的可以不写。

#### 1、基本配置

```python
@app.route('/')            # localhost:5000/
def hello_world():         # 不需要加request参数
    return 'Hello World!'


@app.route('/index1/a/b/c')     # localhost:5000/index1/
def index1():
    return "URLConf-1"


@app.route('/index2/<name>')  # 命名路径  # localhost:5000/index2/Tom
def index2(name):
    return name
```



#### 2、转换器

对于命名路径,可以使用转换器，限定内容：

##### 2.1 Flask提供的默认转换器

```python
#: the default converter mapping for the map.   
DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}
```

示例：

```python
@app.route('/index3/<string:name>')      # string 可以不用定义，默认就是接收字符串
def index3(name):
    return name

@app.route('/index4/<int:age>')          # 只接受整数，age参数类型为int，不再是默认的string
def index4(age):
    return str(age)

@app.route('/index5/<path:name>')        # /d/a/b/c/d/ 可以访问，name="/a/b/c/d" 
def index5(name):
    return name

@app.route("/index6/<any('lilei','Tom'):name>")   # name="lilei"或"Tom"
def index6(name):
    return name

@app.route("/index7/<float:salary>")   # salary为float数
def index7(salary):
    return str(salary)

@app.route("/getUUID/")
def index88():
    return redirect("/index8/"+str(uuid.uuid4())+"/")

@app.route("/index8/<uuid:uid>/")         # /index8/b9630970-27af-4da9-929b-20daaf2af959可以访问
def index8(uid):
    return str(uid)
```



##### 2.2 自定义正则转换器

```python
# 1. 自定义转换器类
对比 DEFAULT_CONRVERTES
class RegexConverter(BaseConverter): # 自定义类，继承BaseConverter(所有转换器的父类)
    def __init__(self,map,*args):    # args=转换器的参数
        self.map = map
        self.regex = args[0]         # BaseConberter中的属性regex

# 2. 注册转换器          名称(键)      实现类(值)
app.url_map.converters['regex'] = RegexConverter 
#      DEFAULT_CONVERTERS 增加键值对

# 3. 使用转换器
				    # 类似 any()用法		
@app.route("/index9/<regex('\d{2}'):age>/")  # \d{2} 会参数给自定义类的args参数
def index9(age):
    return str(age)
```



### 五、跳转

#### 1、跳转到Template

```python
@app.route("/template/")
def template():
    return render_template("index.html")   # 转发到index.html （模板根目录是templates）
```



#### 2、跳转到view（重定向）

```python
@app.route("/index9/")
def index9():
    return "被重定向的页面"

@app.route("/index10/")
def index10():
    #       url_for(“view函数名”)
    url = url_for("index9")   # url_for相当于reverse反向解析, 
    print(url)
    return redirect(url)      # redirect(url) 重定向

# 在template中使用 <a href="{{ url_for('index9') }}">index9</a> 
```

注意： 针对路径软编码

在template中使用 `<a href="{{ url_for('index9') }}">index9</a>`



重定向传参：

```python
#命名路径传参
@app.route("/index10/")
def index10():
    url = url_for("index9",age=20)   # url_for相当于reverse反向解析, url_for(“view函数名”) 
    print(url)
    return redirect(url)
#命名路径接收参数
@app.route("/index9/<age>/")
def index9(age):
    print(age)
    return "被重定向的页面"
或者：
@app.route("/index10/")
def index10():    
    url = url_for('index99') + '?age=20'
    print(url)
    return redirect(url)
# request接收参数  更常用 web前端界面发送参数
@app.route("/index99/")
def index99():
    request.args.get("age")
    return "被重定向的页面"

```



### 六、request访问请求参数

#### 1、Get请求参数

```python
from flask import request                       # 全局request对象
request.args.get("id")                          # 获取id参数,没值报None
request.args["id"]                              # 获取id参数,没值报错
request.args.getlist("id")                      # 返回list
```



#### 2、Post请求参数

```python
from flask import request
request.form.get("id")             # 获取id参数,没值报None
request.form["id"]                 # 获取id参数,没值报错
request.form.getlist("id")         # 返回list 
```

**注意：View函数默认直接收Get请求，如果要发送post，需要设置：**

```python
@app.route("/index11/",methods=['get','post'])
def postParam():
    name = request.form.get('userName')
    password = request.form.get('password')
    print(name,password)
    return "post参数接收"
```

此时可以做一下兼容处理

~~~python
@app.route("/index11/",methods=['get','post'])
def postParam():
    if request.method == 'get':
        name = request.form.get('userName')
    	password = request.form.get('password')
    elif request.method == 'post':
    	name = request.form.get('userName')
    	password = request.form.get('password')
    print(name,password)
    return "post参数接收"
~~~

再回顾 重定向传参数 常用处理方式

* 方式一：

~~~python
# request接收参数
@app.route("/index99/")
def index99():
    request.args.get("age")
    return "被重定向的页面"

@app.route("/index10/")
def index10():
    url = url_for("index99",age=20)   # url_for相当于reverse反向解析, url_for(“view函数名”)
    print(url)
    return redirect(url)
~~~

* 方式二：

~~~python
# request接收参数
@app.route("/index99/")
def index99():
    request.args.get("age")
    return "被重定向的页面"

@app.route("/index10/")
def index10():
    url = url_for("index99") + '?age=18'
    print(url)
    return redirect(url)
~~~



### 七、模板渲染

#### 1、简介

模板其实是一个包含响应文本的文件，其中用占位符(模板变量 {{name}} )表示动态部分内容，告诉模板引擎其具体的值需要从使用的数据中获取，使用真实值替换变量，再返回最终得到的字符串，这个过程称为“渲染”。 Flask是使用 Jinja2 这个模板引擎来渲染模板 。

Jinja2：是 Python 下一个被广泛应用的模板引擎，是由Python实现的模板语言，他的设计思想来源于 Django 的模板引擎，并扩展了其语法和一系列强大的功能，jinja2是Flask内置的模板语言。 

模板语言：是一种被设计来自动生成文档的简单文本格式，在模板语言中，一般都会把一些变量传给模板，替换模板的特定位置上预先定义好的占位变量名。  

**使用**模板的好处：****

- 视图函数只负责业务逻辑和数据处理(业务逻辑方面)

- 而模板则取到视图函数的数据结果进行展示(视图展示方面) 
- 代码结构清晰，耦合度低 。    



#### 2、转发模板

```python
@app.route("/index12/")
def index12():
    return render_template('index.html')
```

注意：模板文件 存放位置 templates目录下

#### 3、模板变量

在view中向模板中传递数据，动态生成页面内容 (从view中传数据到模板文件中)

##### 3.1 view中传值

```python
@app.route("/index12/")
def index12():
    return render_template('index.html',name="lilei",age=18,birthday=datetime.datetime.now(),data={"hobby":['basketball','football'],"height":180,"weight":0})
```

##### 3.2 template中取值

```python
{{ name }} <br>
{{ age }} <br>
{{ data }} <br>
{{ data.height }}cm
{{ data.hobby[0] }} -- {{ data.hobby.0 }} <br>
```



#### 4、过滤器

##### 4.1 内置过滤器

```python
{{ name | upper }}
{{ name | length }}
{{ name | lower }}
{{ name | trim }}   <!-- 掐头去尾，去掉字符串开头和结尾的空格 -->    

{{ abc | default("abc不存在") }}               <!-- abc不存在时，显示default中的内容 --> 
{{ data.weight | default("weight为0",true) }}  <!-- data.weight为None、0、false、"" 时--> 
```



##### 4.2 自定义过滤器

```python
源自： DEFAULT_FILTERS
# 1. 自定义过滤器函数
def dateformat(value,format="%Y-%m-%d"):   # format默认值可选  
    return value.strftime(format)

# 2. 在filters中注册自定义过滤器
app.jinja_env.filters['dateformat'] = dateformat 

# 3. template中使用自定义过滤器
{{ birth | dateformat("%Y-%m-%d") }}
```



#### 5、测试器

`is 测试器` 进行各种判断

##### 5.1 是否定义

```python
测试器：defined=是否定义
{% if birthday is defined %} 
	birthday is there
{% endif %}
可以直接简化为：
{% if birthday %}
	birthday is there2
{% endif %}
```

##### 5.2 是否可以整除

```python
测试器：divisibleby=是否可以整除
{% if (data.list.0 + 1) is divisibleby(2) %}
	{{ data.list.0 }} % 2 == 0
{% endif %}
{% if not data.list.0 + 1 is divisibleby(2) %}
	{{ data.list.0 }}  not % 2
{% endif %}
```

##### 5.3 奇偶数

```python
测试器：even/odd=是否是偶数/奇数
{% if not data.list.0 + 1 is even %} {# odd 是奇数测试#}
	1+1 是偶数
{% endif %}
```

##### 5.4 大小写

```python
测试器：lower/upper=是否是小写/大写字符
{% if data.name is lower %} {# upper 是大写#}
	name is lower
{% endif %}
```



#### 6、运算

```python
{{ data.list.0 + 1 }}
{{ data.list.1 - 1 }}
{{ data.list[0] * 10 }}
{{ data.list[0] / 2 }}
{{ (data.list[0] + 1) % 2 }}

{{ data.list[0]>1}}
{{ data.list[0]==1}}
{{ data.list[0]<=1}}
{{ data.list[0]!=1}}

{{ data.list[0]==1 and 1==2 or 1==1}}
{{ data.list[0]==1 and 1==2 or not 1==1}}

{{ "hilo" ~ data.name ~ "!!" }} {# 字符串拼接 #}
```



#### 7、标签

##### 7.1 逻辑判断

逻辑判断中的0、None、“”、[]、没值  都做为False

```python
{% if data.list | length < 10 %}
	lt 10
{% endif %}

{% if age + 1 < 10 %}
	lt 10
{% endif %}

{% if age + 1 > 17 and name|trim=="lilei" and name is lower %}
	.....
{% endif %}

{% if data.name|trim == "lilei" %}
	hilo,lilei
{% endif %}

{% if data.name == "lilei" %}
	hilo,leilei2
{% elif not data.name|trim=="lilei" %}
	hilo,lilei3
{% else %}
	hilo,lilei4
{% endif %}
```



##### 7.2 循环

```python
{% for user in users %}
  <li>{{ user }}</li>
{% endfor %}

{% for user in users %}
    {% if loop.index is odd %}
    	<li><span style="color:red">{{ user }}</span></li>
    {% elif loop.index is even %}
    	<li><span style="color:green">{{ user }}</span></li>
    {% endif %}
{% endfor %}
注：index index0 revindex  revindex0

{% for key, value in my_dict.items() %}
    {{ key }}
    {{ value }}
{% endfor %}
```

```python
range()--模板的全局函数 range(4) == range(0,4) == range(0,4,1) 最后一个1表示步进  python中range

{% for number in range(10) %}
    <a href="xxxx?num={{number}}">{{number}}</a>
{% endfor %}
```



### 八、模板继承

#### 1、继承extends

- 在多个模板文件中，会有相同的部分，造成模板代码冗余
- 通过父模板的定义，抽取出所有的冗余部分。
- 利于管理和维护

```html
父模板 base.html
...
<body>
    <div style="background-color:lavender;margin-bottom: 100px">
        欢迎你，{{ user.name }}
    </div>
    {% block content%}
        
    {% endblock %}
    <div style="font-size: 12px;color:#999;margin:0 auto;text-align: center;padding:20px 0">
        Copyright © 2013-2018
        <strong><a href="#" target="_blank">百知</a></strong>&nbsp;
        <strong><a href="#" target="_blank">baizhi.com</a></strong> All Rights Reserved. 
    </div>
</body>
```

```html
sub.html

{% extends "base.html" %}

{% block content %}  {#-- 覆写父模板block --#}
    <div style="height: 100px;background-color: #999999">
        这是子类模板自己的内容
    </div>
{% endblock %}
```



#### 2、包含include

- 可以将一个大页面先做好布局，然后布局内的内容可以单独定义一个模板文件，然后再做包含
- 便于管理复杂的模板文件
- 效果和ajax中的load方法相似

```python
...
<body>
    <div style="float: left;height: 300px;width:200px">
        {% include "part1.html" %}
    </div>
    <div style="float: left;height: 300px;width:200px">
        {% include "part2.html" %}
    </div>
</body>
...
```

```html
part1.html:可以是一个完整的html，也可以是html片段
<div style="width: 100px;height: 300px;background-color: red">{{ birth }}</div>
```



### 九、全局错误页面

```python
@app.errorhandler(404) #404错误会自动转到此view，这样就单独定制了404页面
def not_found(e):
	return render_template("404.html")

@app.errorhandler(500) #500错误会自动转到此view，这样就单独定制了500页面(非调试模式下有效)
def not_found(e):
	return render_template("500.html")
```





作业：

 - 整理白天所有笔记，成思维导图。
 - 代码练习敲一遍
 - ems项目进行 相应内容改版  （模板相关部分改版）