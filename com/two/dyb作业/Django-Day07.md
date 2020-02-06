# Django扩展

### 一、验证码

#### 1、简介

在常规的Form表单使用中，验证码是常用的组件，用于更好的保障请求的合法性，防止无效访问，恶意访问，暴力破解等攻击

在服务器端，生成一个随机的code：“aecd1”  ，将code画到一张图片中，最终将图片写出给client。

**注意：依赖第三方包：pillow**

`pip install pillow`



#### 2、验证码使用过程

##### 2.1 导入第三方库

![1532598642901](Django-notes-pic\1532598642901.png) 

将文件拷贝到自己的项目app中，2个py文件，1个data文件夹，保证三个处于项目中的统一个目录中。



##### 2.2 生成验证码

```python
import random,string
from captcha.image import ImageCaptcha   #从image.py中导入ImageCaptchar类

def getcaptcha(request):   # 127.0.0.1:8000/getcaptcha   
    #为验证码设置字体 获取当前目录下的xxx目录下的segoesc.ttf文件
    image = ImageCaptcha(fonts=[os.path.abspath("xxx/segoesc.ttf")])
    #随机码
    #大小写英文字母+数字，随机抽取5位作为验证码 ['x','x','x','x','x'] -> "ABCDE"
    code = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,5) 
    #将验证码存入session，以备后续验证
	random_code =  "".join(code)
    request.session['code']=random_code 
    #将生成的随机字符拼接成字符串，作为验证码图片中的文本
    data = image.generate(random_code )
    #写出验证图片 给客户端
    return HttpResponse(data,"image/png")
```

##### 2.3  在html中使用验证码

```html
<input type="text" name="identifycode">
<img src="{% url 'identify_demo:getcaptcha' %}" id="image_code" width="80px" height="30px" align="center">   
<a href="javascript:void(0)" onclick="change()">换一张</a>

<script>
    function change() {
        var url = "{% url 'identify_demo:getcaptcha' %}?"+new Date().getTime()
        
        $('#image_code').attr('src',url)    //刷新验证码
    }
</script>
```

##### 2.4 验证是否正确

```python
def registlogic(request):
    code = request.session.get('code')
    if code.lower() == request.POST.get('identifycode').lower():
        return HttpResponse("成功")
    else:
        return HttpResponse("失败")
```



### 二、文件上传 

#### 1、简介

Django的模型类（django.db.models.Model）提供了两个字段FileField和ImageField用于上传文件和图片。而ImageField继承自FileField，`class ImageField(FileField):`

使用Django的ImageField需要提前安装**pillow**模块，**pip install pillow**即可。



#### 2、使用步骤

使用FileField或者ImageField字段的步骤： 

1. 在settings文件中，配置**MEDIA_ROOT**，作为你上传文件在服务器中的基本路径。 
2. 添加FileField或者ImageField字段到模型中，定义好upload_to参数，文件最终会放在MEDIA_ROOT目录的“upload_to”子目录中。 
3. 所有真正被保存在数据库中的，只是指向你上传文件路径的字符串而已。可以通过url属性，在Django的模板中方便的访问这些文件。例如，假设有一个ImageField字段，名叫mug_shot，那么在Django模板的HTML文件中，可以使用{{ user.mug_shot.url }}来获取该文件。
4. 可以通过name和size属性，获取文件的名称和大小信息。



#### 3、实例：为用户上传头像

##### 3.1 设置文件保存目录

```python
# settings.py中：

MEDIA_ROOT = os.path.join(BASE_DIR,"media")   # 项目目录下的media目录 需要在项目目录下创建media目录
```



##### 3.2 定义Model

```python
class User(models.Model):
    name = models.CharField(max_length=20)
    #文件将存于 MEDIA_ROOT目录下的pics目录下
    pic = models.ImageField(upload_to="pics")
    csspic = models.FileField(upload_to='pics') # 文件将存放在csspic目录下
```

**注意：定义好Model，记得生成移植文件并执行**



##### 3.3 定义form表单

```html
<form action="{% url 'uploadfile_demo:uplogic' %}" method="post"  enctype="multipart/form-data">  # 上传文件必须要设置type类型，改变默认键值对形式
    {% csrf_token %}
    用户名：<input type="text" name="name"><br>
    头像：<input type="file" name="source">
    <input type="submit" value="提交">
</form>
```



##### 3.4 定义view函数

```python
def uplogic(request):
    try:
        name = request.POST.get('name')
        file = request.FILES.get('source')  # 使用FILES属性才能获取到文件 
        file.name = generateUUID(file.name)    # 调用自定义的generateUUID生成唯一文件名，辨识每个文件的名字

        user = User.objects.create(name=name, pic=file)
        return HttpResponse("上传成功")
    except:
        return HttpResponse("上传失败")
```

```python
import uuid,os
def generateUUID(filename):    # 创建唯一的文件名 服务器端不会直接用本地上传名字，重命名名字。
    id = str(uuid.uuid4())
    extend = os.path.splitext(filename)[1] # 保证与原文件后缀一致
    return id+extend
```

**注意，此时数据库中存储的路径是相对于MEDIA_ROOT的路径**

**所以可以将MEDIA_ROOT设置为静态资源根目录，可便于后续的头像回显**



##### 3.5 回显图片

1. 设置静态资源根目录

   ```python
   MEDIA_ROOT = os.path.join(BASE_DIR,'media')
   
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), MEDIA_ROOT ]
   ```

2. view函数

   ```python
   def query(request):
       users = User.objects.all()
       return render(request,'uploadfile_demo/detail.html',{'users':users})
   ```

3. 模板中使用

   ```
   {% load static %}
   
   <img src="{% static user.headpic.url %}" width="50px">
   ```



**补充：**Python原生文件操作

```python
def test_upload2(r):
    import os,uuid
    b = r.FILES.get("source")  # 获取上传的文件
    unique_name = str(uuid.uuid4())  # 唯一文件名
    ext = os.path.splitext(b.name)[1]  # 文件后缀
    name = unique_name + ext  # 拼接文件名
    with open(file=os.path.join(os.path.abspath("media/just_test/"),name),mode="wb") as output:
        for chunk in b.chunks(): #如果超过2.5M则分块，分为64Kb的块依次读取
            				    #chunks是django.core.files.base.File中的方法
            output.write(chunk)
    return HttpResponse("ok")
```



### 三、分页显示

#### 1、简介

 Django自身提供了一些类来实现管理分页，数据被分在不同的页面中，并带有“上一页/下一页”标签。这个类叫做Pagination，其定义位于 django/core/paginator.py 中。

注意：数据表 需要有排序



####  2、Paginator分页器

##### 2.1 初始化方法

`pagtor = Paginator(User.objects.all(),per_page=3)`   # 构造分页器对象

```python
# 源码
class Paginator(object):

    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True):
        self.object_list = object_list
        self.per_page = int(per_page)
        self.orphans = int(orphans)
        self.allow_empty_first_page = allow_empty_first_page
        self._num_pages = self._count = None
```

##### 2.2 属性

- Paginator.count：所有页面对象总数，即统计object_list中item数目。 
- Pagnator.num_pages：页面总数。
- pagiator.page_range：页面范围，从1开始，例如[1,2,3,4]。

```python
pagtor = Paginator(User.objects.all(),per_page=3)   # 构造分页器对象
print(pagtor.count)                                 # 获取item总数
print(pagtor.num_pages)                             # 页面数
print(pagtor.page_range)                            # 页面范围
```



##### 2.3 page方法（重点）

Paginator.page(number)：根据参数number返回一个Page对象，表示第number页。

```python
page = Paginator(User.objects.all(),per_page=3).page(1)  # 获取第一页
```



#### 3、Page对象

```python
class Page(collections.Sequence):

    def __init__(self, object_list, number, paginator):
        self.object_list = object_list
        self.number = number                
        self.paginator = paginator    # 分页器对象
```

##### 3.1 方法

- `Page.has_next`()  如果有下一页，则返回`True`。
- `Page.has_previous`() 如果有上一页，返回 `True`。
- `Page.has_other_pages`() 如果有上一页或下一页，返回`True`。
- `Page.next_page_number`() 返回下一页的页码。如果下一页不存在，抛出`InvalidPage`异常。
- `Page.previous_page_number`() 返回上一页的页码。如果上一页不存在，抛出InvalidPage异常。
- `Page.start_index`() 返回当前页上的第一个对象，相对于分页列表的所有对象的序号，从1开始。比如，将五个对象的列表分为每页两个对象，第二页的`start_index()`会返回`3`。
- `Page.end_index`() 返回当前页上的最后一个对象，相对于分页列表的所有对象的序号，从1开始。 比如，将五个对象的列表分为每页两个对象，第二页的`end_index()` 会返回 `4`。



##### 3.2 属性

- `Page.object_list `当前页上所有对象的列表。
- `Page.number `当前页的序号，从1开始。
- `Page.paginator `相关的`Paginator`对象。



#### 4、实例

##### 4.1 简单分页

```python
# http://localhost:8000/page/index/?num=2
def index(request):
    number = request.GET.get('num')
    pagtor = Paginator(User.objects.all(),per_page=4)
    page = pagtor.page(number)  # 某一页的page对象
    return render(request,'page_demo/index.html',{'page':page})  
```

```python
{# 显示某一页所有数据#}

{% for user in page.object_list %}
  {{ user.id }} --  {{ user.name }} -- {{ user.password }} <br>
{% endfor %}
```

##### 4.2 输出序号

```python
{# 显示某一页所有数据#}

{% for user in page.object_list %}
  {{ user.id }} --  {{ user.name }} -- {{ user.password }} <br>
{% endfor %}

{# 输出所有页号 #}
{% for page_num in page.paginator.page_range %}
	<a href="/page/index/?num={{ page_num }}">{{ page_num }}</a>
{% endfor %}
```

##### 4.3 显示上一页/下一页

```python
{% for user in page.object_list %}
  {{ user.id }} --  {{ user.name }} -- {{ user.password }} <br>
{% endfor %}

{% if page.has_previous %}             {# 是否有上一页 #}
    <a href="/page/index/?num={{ page.previous_page_number }}">上一页</a>
{% endif %}

{% for num in page.paginator.page_range %}     {# 是否有下一页 #}
    <a href="/page/index/?num={{ num }}">{{ num }}</a>
{% endfor %}

{% if page.has_next %}
    <a href="/page/index/?num={{ page.next_page_number }}">下一页</a>
{% endif %}
```

##### 4.4 页码样式

```css
<style>
    .current{
        width:20px;
        height: 20px;
        border:1px solid #e1e2e3;
        background-color: yellow;
        cursor:pointer;
        display: inline-block;
        text-align: center;
        line-height: 20px;
    }
    .normal{
        border:0;
        width:20px;
        height: 20px;
        cursor:pointer;
        display: inline-block;
        text-align: center;
        line-height: 20px;
    }
    a{
        text-decoration:none;
    }
</style>
```

```python
#显示某一页面数据
{% for user in page.object_list %}
  {{ user.id }} --  {{ user.name }} -- {{ user.password }} <br>
{% endfor %}

#显示上一页
{% if page.has_previous %}
    <a href="/page/index/?num={{ page.previous_page_number }}">上一页</a>
{% endif %}

{% for num in page.paginator.page_range %}
    <a href="/page/index/?num={{ num }}">
        {% if num == page.number %}            {# 当前选中页的样式 #}
            <span class="current">{{ num }}</span>
        {% else %}
            <span class="normal">{{ num }}</span>
        {% endif %}
    </a>
{% endfor %}

 #显示下一页
{% if page.has_next %}
    <a href="/page/index/?num={{ page.next_page_number }}">下一页</a>
{% endif %}
```



### 四、中间件

#### 1、简介

中间件（Middleware）用于在http请求到达`视图函数之前` 和 `视图函数return之后`，django会根据自己的规则在合适的时机执行中间件中相应的方法。 

常用作view中冗余功能的抽取，如每个页面（或某些页面）在访问前**强制登录**。



#### 2、定义中间件

单独 创建py文件 即可

```python
class MyMiddleware(MiddlewareMixin):          # 自定义的中间件
    def __init__(self,get_response):#初始化
        super().__init__(get_response)
        print("init1")
	#view处理请求前执行
    def process_request(self,request):  #某一个view
        
        print("request:",request)
    #在process_request之后View之前执行
    def process_view(self,request, view_func, view_args, view_kwargs):
        print("view:",request,view_func,view_args,view_kwargs)
	#view执行之后，响应之前执行
    def process_response(self,request,response):
        print("response:",request,response)
        return response #必须返回response
    #如果View中抛出了异常
    def process_exception(self,request,ex):#View中出现异常时执行
        print("exception:",request,ex)
```

**中间件中常用的两个过程：**process_request , process_response



#### 3、激活中间件

每当有请求发生时，所有中间件都会执行自己的生命周期。

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ....
    'middleware115.middlewares.MyMiddleware',# 注册自定义中间件路径，尽量放在最后注册
]
```



#### 4、强制登录实例

```python
class MyMiddleAware2(MiddlewareMixin):
    #如果验证成功，则什么一个不用做，否则返回HttpResponse即可响应请求(中断)
    def process_request(self,request):#强制登录判断
        # 特殊情况：访问login，正常进行登录即可
        if "login" not in request.path:#路径中有login，正常登录即可
            print("登录验证")
            session = request.session #获取session
            if session.get("login"): #判断是否有登录的标记
                print("已登录")
            else:
                print("未登录")
                return render(request,"login.html") #未登录则，跳转登录页面
        else:
            print("正在登录") #如果路径中"login"则是登录动作本身
    def process_response(self,request,response):
        print("response:",request,response)
        return response #持续返回响应
```



### 五、CSRF

#### 1、简介

CSRF（Cross-site request forgery）跨站请求伪造，是一种常见的网络攻击手段。

#### 2、基本使用

Django为我们提供了防范CSRF攻击的机制。 

默认情况下，使用`django-admin startproject xxx`命令创建工程时，CSRF防御机制就已经开启了。如果没有开启，请在MIDDLEWARE设置中添加'django.middleware.csrf.CsrfViewMiddleware'

**对于GET请求，一般来说没有这个问题，CSRF通常是针对POST方法的！**

在含有POST表单的模板中，需要在其`<form>`表单元素内部添加`csrf_token`标签，如下所示：

```html
<form action="" method="post">
    {% csrf_token %}
    ....
</form>
```

#### 3、实现原理

1. 在发送请求时，通过CsrfViewMiddleware 在服务器端生成一个随机的token(令牌)，在render渲染模板时存放于form单的隐藏域和cookie中
2. 当再次form发送请求时，会携带隐藏域令牌和cookie中的令牌，此时CsrfViewMiddleware 会先于View执行，去判断两块令牌是否一致，验明正身。



### 六、Admin管理后台  

#### 1、简介

Admin站点是Django有别于其它Web框架最重要的一点

admin通过读取你的模型数据，快速构造出一个可以对实际数据进行管理的Web站点

常用于开发测试，简单管理等场合，适用于部门内部为工作方便的场合，但不建议在生产环境中使用。



#### 2、admin使用步骤

##### 2.1 安装django.contrib.admin

确保,在settins.py中的INSTALLED_APPS 中安装了admin，它会扫描每个app的admin.py，进而支持后台管理。

```python
INSTALLED_APPS = [
    'django.contrib.admin',            # 安装admin
    'django.contrib.auth',             # 下面四个为admin的依赖模块
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    ...
 ]
```



##### 2.2 注册Model

在App的admin.py中注册需要管理的Model类

```python
admin.site.register(User)
```



##### 2.3 创建管理员账户

```python
 python manage.py createsuperuser
```



##### 2.4 启动服务

```
python manage.py runserver
```



##### 2.5 访问后台管理页面

```
http://localhost:8000/admin
```

在URLconf中默认已经配置好admin的访问路径

```
urlpatterns = [
    path('admin/', admin.site.urls),
    ...
]
```



#### 3、定制admin

##### 3.1 User（Models）管理页面

![1531812346521](Django-notes-pic\admin界面.png)

修改后台列表显示User Object，改为更为直观的信息：

```python
class User(models.Model):
    name = models.CharField(max_length=30)
    imagepath = models.ImageField(upload_to='lilei')

    def __str__(self):          # 重写__str__方法
        return self.name
```

![1531812582045](Django-notes-pic\修改admin后台User显示.png)



##### 3.2  操作选项位置

- 定制前：

![1531813791353](Django-notes-pic\操作选项位置.png)

**补充：**注册admin的另一种方式 `装饰器`

```python
@admin.register(User)                # 等价于 admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    #定制操作选项位置
    actions_on_top = True
    actions_on_bottom = True
```



- 定制后：

![1531814252335](C:\Users\ADMINI~1\AppData\Local\Temp\1531814252335.png)





##### 3.3 定制列名

- 定制前：

![1531814668417](C:\Users\ADMINI~1\AppData\Local\Temp\1531814668417.png)



- 定制后：

![1531814709514](C:\Users\ADMINI~1\AppData\Local\Temp\1531814709514.png)



- 代码：

```python
class UserAdmin(admin.ModelAdmin):
	list_display = ['name','imagepath'] # 定制显示的列名
```

- **定制列名的别名（可以是中文）**

```python
class User(models.Model):
    name = models.CharField(max_length=30)
    imagepath = models.ImageField(upload_to='lilei')

    def other_name(self):
        return self.name
    other_name.short_description = '姓名'  # 改列名
    other_name.admin_order_field = 'name'  # 保证改列名后依然可以排序

    def other_path(self):
        return self.imagepath
    other_path.short_description = '图片路径'
    other_name.admin_order_field = 'imagepath'
```

```python
# -- admin.py -- #
class UserAdmin(admin.ModelAdmin):

    list_display = ['other_name','other_path'] # 定制显示的列名的别名 注意使用的是other_name
```

![1531815337945](Django-notes-pic\列名别名.png)



##### 3.4 定制Model名

- 定制前：

![1531815869870](Django-notes-pic\定制Model名)



- 定制后：

![1531815931757](Django-notes-pic\model名)

- 代码：

```python
class User(models.Model):
    ...

    class Meta:
        verbose_name = "用户"          # 修改Model名
        verbose_name_plural = "用户"   # 复数Model名 默认为users
```



##### 3.5 定制过滤查询栏

- 定制前：

![1531816162933](Django-notes-pic\定制查询栏前)



- 定制后：

![1531816244585](Django-notes-pic\查询栏)

- 代码：

```python
class UserAdmin(admin.ModelAdmin):

    list_display = ['other_name','other_path']  
    list_filter = ['name','imagepath']         # 定制过滤查询栏
```



##### 3.6 定制分页

- 定制前：

![1531816470130](Django-notes-pic\定制分页前)



- 定制后：

![1531816419699](Django-notes-pic\分页)



##### 3.7 定制搜索框

- 定制前：

![1531816603764](Django-notes-pic\定制搜索框前)



- 定制后：

![1531816673645](Django-notes-pic\搜索框)



- 代码：

```python
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name'] #可以以哪列作为条件搜索，会增加搜索框
```



##### 3.8 定制可操作的列

- 定制前：

![1531818430016](Django-notes-pic\定制可操作的列前)



- 定制后：

![1531818482886](Django-notes-pic\可操作的列)



- 代码：

```python
class UserAdmin(admin.ModelAdmin):
	fields = [('name', 'imagepath')] #增加和修改页显示的列，且name和imagepath列在一行显示
```



##### 3.9 定制分组显示 

- 定制前：

![1531817042108](Django-notes-pic\定制分组前)



- 定制后：

![1531817077831](Django-notes-pic\分组显示)



- 代码：

```python
class UserAdmin(admin.ModelAdmin):

	...

    fieldsets = (
        ('基本信息',{'fields':['name']}),
        ('头像',{'fields':['imagepath']})
    )
```



##### 3.10  关联显示

![1531819157050](C:\Users\ADMINI~1\AppData\Local\Temp\1531819157050.png)



```python
class Order(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
```

```python
class OrderInline(StackedInline):
    model = Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline
    ]
```



### 七、Form(了解)

> 可以快速定制前端的form表单，并提供参数接收，数据验证。功能看似很全面
>
> 但实则使用价值不大，因为有众多前端框架，可以更专业的定制前端逻辑，而django如此定制有些越俎代庖，而且会影响前端框架的建设，无法和前端人员或前端技术对接(如：easyUI,bootstrap等)
>
> 所以，此章节请自学，了解即可！

```python
class UserForm(forms.ModelForm):
    class Meta:
        model = User2
        #fields=["name","age","gender"]
        exclude=["salary2"]
```

```python
def aa(request):
	print("goto a template")
	render(request,"xx.html",{"form":UserForm()})
```

```python
xx.html
<form action = "xxx" method="post">
	{% csrf_token %}
    <table>
    	{{ form }}
        <tr>
        <td colspan="2" align="center"><input type="submit" value="Submit" /></td>
        </tr>
    </table>
</form>
```

```python
def test3(request):
    form = UserForm(request.POST)
    if form.is_valid():
        print("表单数据合法")
        #{'name': 'zzz', 'age': 18, 'gender': True, 'birth': datetime.date(2018, 11, 12),...}
        data = form.cleaned_data
        print(data)
    return render(...)
```

