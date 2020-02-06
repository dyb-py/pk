# 模板进阶

### 一、模板概述

#### 1、在view中硬编码HTML

```python
from django.shortcuts import render,HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    html = "<h1>It is now %s.</h1>" % now
    return HttpResponse(html)
```

直接将HTML硬编码到视图（Python代码）里却并不是一个好主意。 

- 对页面设计进行的任何改变都必须对 Python 代码进行相应的修改。 前端页面设计的修改往往比底层 Python 代码的修改要频繁得多，因此如果可以在不进行 Python 代码修改的情况下变更页面设计，那将会方便得多。
- Python 代码编写和 HTML 设计是两项不同的工作，大多数专业的网站开发环境都将他们分配给不同的人员（甚至不同部门）来完成。 设计者和HTML/CSS的编码人员不应该被要求去编辑Python的代码来完成他们的工作。
- 程序员编写 Python代码和设计人员制作模板两项工作同时进行的效率是最高的，远胜于让一个人等待另一个人完成对某个既包含 Python又包含 HTML 的文件的编辑工作。

基于这些原因，将**页面的设计和Python的代码分离开会更干净简洁更容易维护**。 我们可以使用 Django的模板系统 (Template System)来实现这种模式 。

**模板是一个文本，用于分离文档的表现形式和内容**。 模板定义了占位符以及各种用于规范文档该如何显示的各部分基本逻辑（模板标签）。 模板通常用于产生HTML 。



#### 2、MTV模式

- **模型（Models）：**一个抽象层，用来构建和操作你的web应用中的数据，模型是你的数据的唯一的、权威的信息源。它包含你所储存数据的必要字段和行为。通常，每个模型对应数据库中唯一的一张表。 

- **模板（Templates）**：模板层提供了设计友好的语法来展示信息给用户。使用模板方法可以动态地生成HTML。模板包含所需HTML 输出的静态部分，以及一些特殊的语法，描述如何将动态内容插入。 

- **视图（ Views）**：用于封装负责处理用户请求及返回响应的逻辑。视图可以看作是前端与数据库的中间人，他会将前端想要的数据从数据库中读出来给前端。他也会将用户要想保存的数据写到数据库。 


```python
# models.py   模型 -- 提供数据
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=18)
```

```python
# views.py  视图 -- 逻辑处理
def login_logic(request):
    uname = request.POST.get('name')
    upassword = request.POST.get('password')
    try:
        user = User.objects.get(name=uname,password=upassword)
        res = render(request,"account/loginSuccess.html",{"user":user.name})
        return res
    except ObjectDoesNotExist:
        return HttpResponse("失败")
```

```html
<!-- loginSuccess.html 模板文件 显示内容-->   
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    登录成功，欢迎{{ user }}      <!-- 动态内容 -->
</body>
</html>
```



#### 3、**Django 模板查找机制** 

模板的搜索根目录：**Project下的templates目录 和 “已安装App”下的templates目录**

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]                 # project下的templates目录
        ,
        'APP_DIRS': True,                                             # App下的temlates目录
        ...
    },
]
```

**模板文件管理方式：**

- 每个App自己持有，且有自己的独立目录防止多个App中的模板命名冲突。

  - 具体操作：在app目录下创建templates目录，在templates目录下创建与app名相同的目录，再创建html文件。
  - 使用：`render(request,"app名/xxx.html")`

- 统一放在Projects根目录下的templates目录中，且有自己的独立目录防止多个App中的模板命名冲突 。

  - 具体操作：在项目目录下的templates目录，创建与app名相同的目录，再创建html文件。
  - 使用：`render(request,"app名/xxx.html")`



### 二、模板语言DTL

#### 1、模板语言概述

模板语言：Django内置有自己的模板语言(模板引擎)；第三方的模板语言比较流行的有jinja。

Django官方表示，如果没有不得不换的原因，推荐内置模板语言**Django Template Language(DTL**)

模板文件中，包含的动态渲染代码，使用的就是DTL

```html
<body>
    登录成功，欢迎{{ user }}      <!-- 动态内容 -->
</body>
```



#### 2、模板传值

模板的正确使用，是衔接View，接收View传递的数据，将数据渲染在html网页中。

值：View中通过Model层得到的数据。

传递：由View 传递给 Template。

目标：将数据渲染到一块静态内容(html)中 , 定制动态内容，作为请求的响应内容。

- 传值示例：`{key:value,key2:value2}`

```python
# views.py
def xx(request):
    user = User.objects.get(pk=1) #获得数据
    # 跳转index.html,并向其传值：{"user":user}，index.html就可以使用如此数据
	return render(request,"index.html",{"user":user})
```

```html
<-- index.html ->
<html>  
	...
    hello,{{user}} <!-- 使用View传递来的数据 -->
    ...
</html>
```

总结：通过view获取Model层的数据，并传递给模板文件，生成动态内容。



### 三、模板变量

从本节开始，讲解DTL的详细语法。变量--在模板中如何去获取View传递来的数据。`{key:value,key2:value2}`

#### 1、简单数据

```html
<!-- index.html -->
<body>
    现在时间是：{{time}}
</body>
```

```python
# views.py
def index(request):
    now = datetime.now()
    return render(request,"template_app/index.html",{"time":now})
```

#### 2、列表

```python
# views.py
def index(request):
	content = {'list':[2,4,6,8,22]}
    return render(request,"template_app/index.html",content)
```

```python
<!-- index.html -->

{{ list }}
{{ list.0 }}
{{ list.1 }}
```

#### 3、dict字典

```python
# views.py
def index(request):
    content = {'dic':{'name':'lilei','age':20}}
    return render(request,"template_app/index.html",content)
```

```python
<!-- index.html -->

{{ dic.name }}
{{ dic.age }}
```

#### 2、Model对象  

```python
# views.py
def index(request):
	content = {"user1": User(name='lilei',age=18)}
	# content = {"user2":User.objects.get(pk=1)}
	# content = {"user3":User.objects.filter(pk=1)}
	return render(request,"template_app/index.html",content)
```

```python
<!-- template index.html -->
{{user1.name}}             # user1的name属性
{{user1.age}}              # user1的age属性

{{ user2.order_set.all.0 }}       # id为1的用户的所有订单中的第一个订单
{{ user2.order_set.all.0.price }}  # 第一个订单的价格

{{ user3.0.name }}      # id=1的结果集中的第一个用户的名字
```



#### 5、无参方法（了解）

```
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()

    def func(self):
        return "测试函数"
```

```python
def index(request):
    content = {"user2":User.objects.get(pk=1)}
    return render(request,"template_app/index.html",content)
```

```python
<!-- index.html -->

{{ user2.func }}
```



### 四、模板标签

#### 1、if/else 标签

基本语法格式如下： 

```python
{% if condition %}  
     ... display ...
{% else %}
     ...
{% endif %}
```

或者： 

```python
{% if condition1 %}
   ... display 1
{% elif condiiton2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}
```

示例：

```python
# 比较运算

{% if list.1 > 3 %}
    {{ list.1 }}
{% endif %}
```

```python
# 逻辑运算

{% if 1 or 2 %} {# and or not 与或非 拼接多个条件 #}
    ...
{% elif id > 100 and not name %}
    ....
{% elif not id > 100 and not name %}
    ....
{% endif %}
```

```python
# in / not in  包含于/不包含于   用于字符串 和 序列 和 dict 和 QuerySet 

{% if  user.name not in "aazhjzzzaaa" and users.0 in users%}
    name in zhjasdf
{% endif %}
```



#### 2、for 标签

{% for %} 允许我们在一个序列上迭代。

与Python的 for 语句的情形类似，循环语法是 for X in Y ，Y是要迭代的序列而X是在每一个特定的循环中使用的变量名称。

```python
{% for foo in list %}
    {{ foo }},
{% endfor %}
```

- 给标签增加一个 reversed 使得该列表被反向迭代： 

```python
{% for foo in list reversed %}
    {{ foo }},
{% endfor %}
```

- empty空标签

```python
{% for foo in list  %}
    {{ foo }},
    {% empty %}
    <p> 如果遍历的数据为[],或不存在，执行empty，输出这个段落</p>
{% endfor %}
```

- 遍历list of list

```python
content = {'list':[[1,2,3],[4,5,6]]}

{% for f1,f2,f3 in list  %}
    {{ f1 }},{{ f2 }},{{ f3 }}
{% endfor %}
```

- 遍历索引

```python
{% for ... %}
	...
    {{ forloop.counter0 }}  遍历索引,从0开始
    {{ forloop.counter }}   遍历索引,从1开始
    {{ forloop.revcounter }}  倒序索引
    {{ forloop.revcounter0 }}  # 倒序索引，对应 counter0
    {{ forloop.first }}  #是否为第一次面试
    {{ forloop.last }}  # 是否为最后一次遍历
    ...
{% endfor %}

{% for ... %}
   ...
   {% if  forloop.first %}
		第一次遍历
   {% else %}
   ...
{% endfor %}
```



### 五、过滤器

获取值的过程中，可以对值进行处理，通过  **过滤器**  完成。

注意：| 左右两侧不允许有空格。坑

`{{ xx }} 正常取值`   

`{{ xx|过滤器 }}`

```python

{{name|length}}  {#获取长度#}
{{list|length}}  
{{dict|length}}
{{queryset|length}}
{{name|length_is:'4'}}   # 判断 长度是否为4  True/False

{{name|lower}}  {# 所有字符变小写 #} （了解）
{{name|upper}}  （了解）
    
{{name|default:'lilei'}} {# 没值、False、None、""、0 #}（了解）游客，不存在

{# 加减乘除 #}
{{ list115.1|add:'1' }} {# 加法 #}
{{ list115.1|add:'-1' }} {# 减法 #}
{{ list115.1|divisibleby:'2' }}<br/> {# % 求模运算 #}
{% widthratio 5 10 100 %}  {# a/b*c   5/10*100 百分比#}  
{% widthratio list115.1   1   list115.2 %}  {#  乘法运算 #}
{% widthratio list115.1   list115.2  1 %}  {#  除法运算 #}

{#技巧#}
{% widthratio a b c as result%}
{% if result == "50" %}
	....
{% endif %}
    
{{birth|date:'Y/m/d H:i:s'}}
```

```python
{% if  user.birth|date:'Y/m/d H:i:s'|length > 10%}
    <p>length gt 10</p>
{% endif %}
```



### 六、模板继承 

项目的多个页面中会有重复的部分，会导致在多个模板文件中会有重复的代码，文本。

此时，会造成代码冗余，不利于项目的管理

模板继承，可以很好的解决这种问题

语法：

```html
<!-- base.html 包含的是子模板中共有的内容 -->  

<html>
  <head>
    <title>Hello World!</title>
  </head>

  <body>
    <h1>Hello World!</h1>
    {% block mainbody %}
       
    {% endblock %}
  </body>
</html>
```

![1546053791592](Django-Day06.assets\1546053791592.png)

以上代码中，名为mainbody的block标签是可以被继承者们替换掉的部分。 

```html
<!-- sub1.html 子模板文件-->

{% extends "base.html" %}   

{% block mainbody %}
<p>继承了 base.html 文件</p>
{% endblock %}
```

![1546053869616](Django-Day06.assets\1546053869616.png)

子模板中只能定义父模板中 `block块`中的内容，其他内容都是继承自父模板

则实现了子模板中不用定义父模板中已经定义的内容，进而消除重复。

**注意：**在子模板中，只有block块内的内容，才是有效的内容，block块外的内容，不被解析，视为无效。



### 七、静态资源

#### 1、静态资源概述

除了HTML文件外，WEB应用一般需要提供一些其它的必要文件，比如图片文件、JavaScript脚本和CSS样式表等等，用来为用户呈现出一个完整的网页。

在Django中，我们将这些文件统称为“静态文件”，因为这些文件的内容基本是固定不变的，不需要动态生成。 



#### 2、使用静态资源

首先在你的app目录中创建一个`static`目录。Django将在那里查找静态文件，这与Django在/templates/中寻找对应的模板文件的方式是一致的。 

**目录结构如下：**

```
APP
	-- static
		-- (aaa.css，bbb.jpg，ccc.js)
```

```python
settings.py中

STATIC_URL = '/static/'   #ip:port/static/
```

访问：

```python
# Django在查找静态资源时，是查找 "已安装"的APP中的static目录
<link rel="stylesheet" href="/static/aaa.css"> # 访问aaa.css文件
<img src="/static/bbb.jpg" width="200px"/> # 访问bbb.jpg文件
<script src="/static/ccc.js"></script>  # 访问ccc.js文件
```



**注意：** 如果多个APP下有同名文件，会如何？

​        **静态资源的查找是短路查找，找到就停止。所以后安装的app中的静态资源，无法被访问**

**解决方案：每个APP的静态资源都有自己的独立目录即可**

**注意：在有了独立目录后，在访问静态资源是，路径上也要加上独立目录名** 

除默认的静态文件根目录外，

也可以，单独创建一个static目录，存放所有app的静态资源，增加几个静态文件的根目录：

```python
settings.py
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'),
                     "E:\\static"]
```

Django查找静态资源的目录：

（1）默认在每个app的static目录下去查找

（2）可以再额外添加一些静态资源的查找目录 在setting.py文件中 加STATICFILES_DIRS = []

访问时：  加static_url指定的访问前缀   /static/img/a.jpg



修改硬编码URL：

```
{% load static %}   HTML文件最上面

<img src="{% static "/img/a.jpg" %}"> 
```





总结：

 -  模板相关

    模板文件存放路径

    静态资源存放设置

    url中 命名空间 以及对应 url设置name

- 模板语言DTL

  - 模板传值？ 语法规范 render( ,{})
  - 模板变量  Python现有数据类型 MODEL对象 
  - 模板标签  if  for
  - 过滤器  
  - 模板继承  

作业：

​	白天代码 敲  整理白天笔记

​	模板继承 title实现各自自定义

​	表单中：输入框 提交按钮

​		点击提交按钮，后端通过接收到的不同数据，去 取不同的表中数据  用户表，员工表，部门表。

​	把表中所有数据 传给 html文件

​	html文件操作：把所有数据 展示在表格中 实现 边框 隔行变色



