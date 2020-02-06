#  请求与响应 

### 一、请求与响应

- #### 请求与响应过程


当用户请求一个页面时，Django 把请求的数据包装成一个 HttpRequest 对象，然后 Django 加载对应的view 函数，把这个 HttpRequest 对象作为第一个参数传给 view 函数。任何 view 函数都应该返回一个 HttpResponse 对象。 

![请求与响应](Django-notes-pic\请求与响应.jpg)

- 客户端发送一个请求，并携带参数到达服务器端     Browser -> Server 
- 服务器会接收请求，并通过request对象获取数据
- 服务器会进行逻辑处理（查询数据库，验证）
- 服务器返回响应回到客户端 Server -> Browser

 

### 二、HttpRequest请求对象

HttpRequest 对象表示来自客户端的一个单独的 HTTP 请求。HttpRequest 对象是 Django 自动创建的，且会传递给视图函数作为第一个参数。 

**HttpRequest常用的属性：**

- method -- 返回一个字符串，表示请求使用的HTTP方法 

  ```python
  if request.method == "POST":
  
  	...
  
  elif request.method == "GET":
  
  	...
  ```

- GET、POST -- 一个类似于字典的对象，包含GET、POST请求时传递的的所有参数

  ```python
  def formRequest(request):
      if request.method == 'GET':
          a = request.GET.get('uname')              # 通过GET的get方法得到uname对应的值 
          b = request.GET['upwd']                   # 通过字典形式获取
          return HttpResponse("表单传参" + a + b)
      else:
          a = request.POST.get('uname')
          b = request.POST.get('upwd')
          return HttpResponse("表单传参" + a + b)
  ```

- COOKIES -- 包含所有cookies的标准Python字典对象。Keys和values都是字符串。 


### 三、HttpResponse响应对象

#### 1、响应对象简介

Request 和 Response 对象起到了服务器与客户机之间的信息传递作用。Request 对象用于接收客户端浏览器提交的数据，而 Response 对象的功能则是将服务器端的数据发送到客户端浏览器。 

对于 HttpRequest 对象来说，是由 Django 自动创建, 但是，HttpResponse 对象就必须我们自己创建。每个 View 方法必须返回一个 HttpResponse 对象。 

#### 2、创建Response对象

##### 2.1 不调用模板，直接返回数据 

```python
from django.http import HttpResponse

def index(request):
	return HttpResponse('HelloWorld')
```



##### 2.2 调用模板

- **使用render()函数**

  ```python
  from django.http import HttpResponse，render
  
  def index(request):
  	return render(request, "index.html")     # 建议使用更简易的这种写法
  ```



### 四、view跳转

#### 1、跳转的情景

一个View接到请求，处理完业务逻辑后，最后都需要给出响应。而响应内容的生成一般不由View负责，Template是专业的响应内容生成者，则此时需要View和Template之间做衔接、跳转。

- 基本的跳转：从view跳转到template

```python
from django.http import HttpResponse，render

def index(request):
	return render(request, "index.html")     # 跳转到模板中，并将模板内容显示在客户端
```



- 更复杂的跳转：从view跳转到view，再跳转到template（用户注册完成后，自动跳转到登录页面）


```python
def regist_logic(request):
    try:
        name = request.POST.get("userName")
        password = request.POST.get("userPwd")
        user = User.objects.create(name=name, password=password)
        #return HttpResponseRedirect("/redirect/login/")       # 从一个页面，重定向到另一个页面
        return redirect("/redirect/login/")       # 从一个页面，重定向到另一个页面
    except:
        return HttpResponse("注册失败")
```
**跳转方式：**

- **转发**：基本的跳转，浏览器中的URL不变

  转发发生在一个请求内的跳转，用于View到Template间的跳转， **`render(request, "test.html")`**  即为在一个请求内由View转发跳转到Template

- **重定向**：从view跳转到view，浏览器中的URL发生改变

  重定向发生在不同请求之间，用于View之间的跳转 **`redirect("另外的View的请求路径：/a/b/c/")`**



#### 2、重定向与转发的区别

1. 转发用于View和Template，重定向用于View和View
2. 转发是一次请求内的跳转(地址栏不变)，重定向会自动触发第二次请求(地址栏会改变)



### 五、Cookie 

#### 1、Cookie简介

Cookie实际上是一种数据存储技术，由服务器生成，并保存在客户端(浏览器)的一种技术。  

HTTP协议是无状态的协议。一旦数据交换完毕，客户端与服务器端的连接就会关闭，再次交换数据需要建立新的连接。 

比如你登录邮箱，我们经常会在此时设置30天内记住我，或者自动登录选项。 



#### 2、Cookie的使用场合 

- 保存登录信息 
- 保存用户的搜索关键词 



#### 3、Cookie的使用过程

##### 3.1 存储cookie

存储cookie是由Response对象来完成，当通过Response对象设置好cookie后，再响应到客户端，cookie会随之存入到客户端。

由服务器生成，通过Response对象传递给客户端浏览器并保存

- 不使用模板

  ```python
  def index(request):
      res = HttpResponse("测试cookie")
      res.set_cookie("name","lilei") 
      return res;
  ```

- 使用模板

  ```python
  def index2(request):
      res = render(request,'cookie_demo/index.html')
      res.set_cookie("age",18)
      return res;
  ```

**设置过期时长：**默认是浏览器关闭后失效 --  一个会话周期

- max_age=0 会删除cookie，如：res.set_cookie("password",max_age=0)
- max_age=-1，或不设置max_age 都是会话级cookie
- max_age=100 存活100秒，100秒后失效

```python
 res.set_cookie("age",18，max_age=100)
```



##### 3.2 读取cookie

请求服务器时，当再次访问项目时，request会携带本项目的所有cookie到达服务器，通过request对象可以读取cookie中的数据。

```python
def index(request):
    #返回所有cookie
    print(request.COOKIES)             #{'name': 'lilei', 'age': 18}
    print(type(request.COOKIES))       #dict
    request.COOKIES['age']  
    request.COOKIES.get("age") 
```

![cookie过程](Django-notes-pic\cookie过程.png)



#### 4、cookie中文问题

```python
#存中文cookie值
name = "李雷".encode('utf-8').decode('latin-1')

#取中文cookie值
str = request.COOKIES.get("name").encode('latin-1').decode('utf-8')
print(str)
```

**测试实例：记住我**  



### 六、Session

#### 1、Session简介

Cookie是将少量信息存储于客户端（本地浏览器）的，而Session技术是一种将会话状态保存在服务器端的技术。

Session一般是指浏览器这个页面打开到关闭的这段时间 ，Session用作多个请求之间，共享数据。

常见情景：登录请求之后，之后的请求中都可以显示用户名。



#### 2、Session使用

##### 2.1 启用Seesion功能

- settings.py中如下设置，开启后，请求到达服务器时，就可以使用session了：

```python
INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
    ...
]
MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]
```

- 在使用session前，需要为**django.contrib.sessions**做移植生成数据表，用于存储session数据

```python
python manage.py migrate
```



##### 2.2 Session生命周期

Session默认存活两周，可以修改为一个会话周期，在settings.py中：

```python
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
```



##### 2.3 存储Session

```python
#注意，django默认的session存储位置为数据库的django_session表，需要通过python manage.py migrate生成
def xxx(req):
    req.session['username']="lilei"   # 储存在服务器端，所以使用request来存储。VS. cookie
    req.session['login']=1
    ...
```



##### 2.4 读取Session

```python
def xxx(req):
    print(req.session['username'])
    print(req.session.get('login'))
    ...
```

**注意session没有中文问题，没有长度限制，相比存在客户端的cookie更安全**



##### 2.5 手动清除Session

主动 退出登录

```python
req.session.flush() # 清除数据，置空cookie中的sessionid，清除数据表中的记录
req.session.clear() #清除数据 数据记录还在
del req.session['username'] #清除一个key的数据
```



##### 2.6 Session存储位置

- 数据库：**INSTALLED_APPS** 中的 **django.contrib.sessions** 会在执行移植文件时生成数据表（默认）
- 缓存：为Project设置缓存组件，则session可以存入缓存，提高执行效率(redis)
- 文件：存于服务器本地文件中（不建议）
- cookie：存取客户端的cookie中（不建议，适合小项目）


##### 2.7  Seesion实现原理

浏览器第一次请求session对象时，服务器会创建一个session并且生成一个sessionId，存储在数据库中，并将sessionid返回给浏览器，这个sessionId会被保存在浏览器的会话cookie中

在浏览器不关闭的情况下，之后的每次请求请求头都会携带这个sessionId到服务器。服务器接收到请求后就得到该请求的sessionID，服务器找到该id对应的session返还给请求者使用。 



##### 2.8 Cookie Session选择

- 需要在多个请求间多次共享使用的数据，保持状态，使用session，如在多个请求间持续保持一些数据
- 需要在一段时间后依然可以保持的小块数据，使用cookie，如“记住我”，保证一段时间后，可以自动登录
- 每个网站在一个浏览器中的cookie数据上限是4k，session没限制
- cookie存在浏览器本地，隐私性不好。安全性较低



**测试实例**：强制登录 

我的订单 进入时，进行判断，是否已经登录账户，如果没有，强登，否则直接进入 订单页面。



### 七、全局错误视图设置

http请求的状态码  200=成功  404=资源未找到  500=服务器错误(10/0)   400=bad request...(改变服务器ip地址)

可以为常见的错误定制错误页面

关闭调试模式，设置allow_hosts ['*']

在templates下新建：404.html   500.html  400.html,在出现对应错误时，会自动跳转错误页面



### 八、基于View的事务控制

对接 MYSQL中事务，处理 数据 增删改 情况

Django手动配置事务的方式主要有二种：

- 第一种是将每个请求都包裹在一个事务中。  

  - 需要在settings.py中的database配置中加入`'ATOMIC_REQUESTS': True`

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'jangodb',
          'USER':'root',
          'PASSWORD':'123456',
          'HOST':'localhost',
          'PORT':3306,
          'ATOMIC_REQUESTS':True
      }
  }
  ```

  - 当有请求过来时，Django会在调用视图方法前开启一个事务。如果请求正确处理并正确返回了结果，Django就会提交该事务。否则，Django会回滚该事务。 

```python
# 运行View前已经开启事务
def test(request):
    Person(name="tx_name22", age=18).save()
    Person(name="tx_name33", age=18).save()
    a=10/0 #出现异常，事务自动回滚
    return HttpResponse("abc")
```



**注意：**

**如下情况，事务依然提交**

基于View的事务控制，不能处理异常，否则事务行为被破坏

如果在view中try了异常，django就认为整个View没有异常，则事务正常提交

```python
def test(request):
    try:
        Person(name="tx_name22", age=18).save()
        Person(name="tx_name33", age=18).save()
        a=10/0
    except Exception:
        print("error")
        raise
        return render(request,"error1.html")
    return render(request,"success.html")
```

注册页面时，在注册提交后提示注册失败；重新注册会发现，之前注册提交的用户名提示已存在。事务并没有回滚。

- 第二种是自己在view中通过上下文管理器灵活控制事务。 

```python
def test(request):
    try:
        with transaction.atomic():#开始一个事务 环境,with结束时，如果没有异常，事务提交；否则回滚
            Person(name="tx_name22", age=18).save()
            Person(name="tx_name33", age=18).save()
            a=10/0
        	return render(request,"success.html")
    except:
        print("error") #此时的异常已经回滚
        return render(request,"error.html") #还可以为错误提供专用的视图页面
```



### 九、反向解析

#### 1、简介

在实际的Django项目中，经常需要获取某条URL，为生成的内容配置URL链接。 

比如提交表单时，跳转到某个url，点击a标签链接到某个url，此时在表单和a标签中一定不能硬编码URL 。

```html
<!-- 都使用了硬编码 -->
<form action="/account/loginlogic/" method="post"> </form>

<a href="/account/regist/">注册</a> 
```

```python
path('loginlogic/',views.login_logic),
path('regist/', views.regist_view),
```

一旦URLconf中的的路由配置发生修改，则需要在所有使用到该url的地方去作修改。显然这种做法是比较stupid。



#### 2、反向解析

此时我们需要一种安全、可靠、自适应的机制，当修改URLconf中的代码后，无需在项目源码中大范围搜索、替换失效的硬编码URL。

为了解决这个问题，Django提供了一种解决方案，只需在URL中提供一个name参数，并赋值一个你自定义的、好记的、直观的字符串。

通过这个name参数，可以反向解析URL、反向URL匹配、反向URL查询或者简单的URL反查。

```python
urlpatterns = [
    path('index/',views.index,name='index'),
]
```



#### 3、如何使用

在需要解析URL的地方，对于不同层级，Django提供了不同的工具用于URL反查：

- 在模板语言中：使用`url`模板标签。(也就是写前端网页时）

  ```html
  <a href="{% url 'index' %}">反向解析</a>
  ```

- 在Python代码中：使用`reverse()`函数。（也就是写视图函数等情况时）

```python
def index(request):
    url = reverse('index')   # 可用作重定向的url等
    print(url)   
    return render(request, 'index.html')

# redirect("index")  --  path('index/',views.index,name='index'),
```



#### 4、URL命名空间 

URL名称name使用的字符串可以包含任何你喜欢的字符，但是过度的放纵有可能带来重名的冲突，比如两个不同的app，在各自的urlconf中为某一条url取了相同的name，这就会带来麻烦。为了解决这个问题，又引出了下面的命名空间。 

URL命名空间可以保证反查到唯一的URL，即使不同的app使用相同的URL名称。 

实现命名空间的做法很简单，在urlconf文件中添加`app_name = 'xxx'` 即可。

```python
#-- urls.py -- #

app_name='reverse_app'       # 定义app_name

urlpatterns = [
    path('index/',views.index,name='index'),
]
```

使用时在name前加app_name:url_name即可：

```python
def index(request):
    url = reverse('reverse_app:index')   # 使用方式 app_name:url_name
    print(url)
    return render(request, 'index.html')
   # return redirect('reverse_app:index')
```

```html
<a href="{% url 'reverse_app:index' %}">反向解析</a>
```







**作业：**

技术点熟悉，练习

登录  注册  

注册后自动跳转登录页面，登录成功后自动跳转到home页面

登录后记住我 一周  -- cookie

强制登录  -- session



