#  模型_01

### 一、模型简介 

#### 1、模型概述

- **模型（Models）：**用来构建和操作你的web应用中的数据，模型是你的数据的唯一的、权威的信息源。它包含你所储存数据的必要字段和行为。通常，每个模型对应数据库中唯一的一张表。 

- **模板(templates)**：模板层提供了设计友好的语法来展示信息给用户。使用模板方法可以动态地生成HTML。模板包含所需HTML 输出的静态部分，以及一些特殊的语法，描述如何将动态内容插入。 

- **视图（views）**：用于封装负责处理用户请求及返回响应的逻辑。视图可以看作是前端与数据库的中间人，它会将前端想要的数据从数据库中读出来给前端。也会将用户要想保存的数据写到数据库。 



#### 2、ORM 

##### 2.1 ORM概念

ORM是对象关系映射(Object Relational Mapping)的缩写，由于程序设计者更多采用面向对象的思想，而数据库则以关系作为其基础，ORM的作用使得我们可以采用面向对象的思路来设计数据库，使数据库设计更加简单。 



##### 2.2 ORM的优势

Django的ORM操作本质上会根据类与对象 对接数据库引擎，翻译成对应的sql语句；所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换Django的数据库引擎配置即可。



### 二、Model层开发过程

#### 1、安装数据库驱动   

```
pip install mysqlclient
```

#### 2、数据库配置

在项目的 settings.py 文件中找到 DATABASES 配置项，将其信息修改为： 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',     # 数据库引擎
        'NAME': 'test',                           # 数据库名
        'USER': 'root',						    # 用户名
        'PASSWORD': '123456',					# 密码
        'HOST':'localhost',						# 主机ip
        'PORT':3306,						    # 端口号
    }
}  
```

#### 3、创建App，安装App

- Django规定，如果要使用模型，必须要创建一个app：

```
python manage.py startapp testapp
```

- 安装App  在settings.py文件中

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testapp',                       # 创建的app名
]
```

- 修改时区等（暂时跳过）

```python
LANGUAGE_CODE = 'zh-hans'      # 让后台页面支持中文           
TIME_ZONE = 'Asia/Shanghai'    # 将时区改为东八区
```

![1545792451008](.\Django-Day03.assets\1545792451008.png) 	

#### 4、定义Model类

在App目录下的Models.py文件中，添加Model类：

```python
from django.db import models

class User(models.Model):                           # 一个Model类将对应数据库中的一个表  -- 基类
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    birthday = models.DateTimeField()
```

#### 5、生成移植文件记录

```python
python manage.py makemigrations            # 生成迁移记录
```

补充：`python manage.py sqlmigrate modelapp 0001` 查看对应的sql语句

#### 6、执行移植操作

```python
python manage.py migrate                   # 执行迁移操作--应用到数据库
```

#### 7、测试Model

```python
-- views.py -- 
def testdb(request):
    userlist = User.objects.all()
    str = ''
    for user in userlist:
        str += (user.name+',')
    return HttpResponse('查询结果：'+str)
```



### 三、模型字段

#### 1、常用字段类型

| 字段类型          | 说明                                                         |
| ----------------- | ------------------------------------------------------------ |
| AutoField         | 一般不用直接使用，Model中默认的主键类型。<br />Django默认给每个Model一个主键字段(如果没有自己定义的话) |
| SmallIntegerField | 2字节  smallint                                              |
| IntegerField      | 4字节  int                                                   |
| BigIntegerField   | 8字节   bigint                                               |
| FloatField        | double                                                       |
| DecimalField      | DecimalField(max_digits=5,decimal_places=2)  decimal。  <br />必填：max_digits=5 #共有几位数<br />必填：decimal_places=2#其中小数位占几位 |
| CharField         | CharField(max_length=20) max_length是必填属性 == varchar(20) |
| TextField         | longtext                                                     |
| BooleanField      | 接收“True/False”  tinyint                                    |
| NullBooleanField  | 接收“True/False/None”  tinyint                               |
| DateTimeField     | datetime                                                     |
| DateField         | 可选：auto_now=true 可做修改时间记录<br />可选：auto_now_add=True 可做首次添加时间<br />注意：以上两属性之一指定后，该字段不允许被编辑 |
| TimeField         | time                                                         |
| ForeignKey        | ForeignKey(to=关系对方的类或类名或‘self’，on_delete=级联选项) |
| OneToOneFiled     | OneToOneFiled(to=关系对方的类或类名或‘self’，on_delete=级联选项) |
| ManyToManyFiled   | ManyToManyFiled(to=关系对方的类或类名或‘self’)               |

#### 2、字段参数

- null   默认False,不能为空

  ```python
  name = models.CharField(max_length=20,null=True) #可为空
  ```

- default  定义默认值

  ```python
  name = models.CharField(max_length=20,default="lilei")
  age = models.IntegerField(default=18)
  birthday = models.DateTimeField(default="2018-12-12")
  ```

  默认值不会作用在数据库上，而是django自己的约定，通过Model.save()时，会使用默认值

- primary_key

  ```python
  id = models.AutoFiled(primary_key=True) #默认追加，不用自己定义
  id = models.CharField(primary_key=True,max_length=32)#如果需要字符串类型的ID可以自己定义
  ```

- unique  列是否唯一

  ```python
  name = models.CharField(max_length=20,unique=True)
  ```

- db_column    自定义列名，默认和field同名 

  ```python
  name = models.CharField(max_length=20,db_column="name9")
  ```

- db_index   是否在列上建立索引

  ```python
  name = models.CharField(max_length=20,db_index=True)
  ```

- blank  默认Flase，用于前端页面的form验证（了解）

  ```
  note = models.CharField(max_length=20,blank=True)
  ```

#### 3、元数据Meta

模型的元数据，指的是“除了字段外的所有内容”，例如排序方式、数据库表名、人类可读的单数或者复数名等等。 

- db_table = 'xxx' 设置表名（修改django默认生成的表名）
- unique_together = (('列名1','列名2'),(...))  设置联合唯一约束
- ordering = ['列名1']  或 ['列名1','列名2'] 

```python
class MyModel(models.Model):
   salary = models.DecimalField(...)
   .....
   age = models.xxx
   name = models.xxx
   class Meta:  
        unique_together = (("salary", "salary2"),("age","age2","age3"))
        db_table="my_user"
        ordering=['-age','name'] #根据age降序排列，如果age相同，再按照name升序排列
```



### 四、Model-API增删改 

#### 1、创建对象（添加数据） 

在Terminal中执行`python manage.py shell`进入python解释器：

```python
from testapp.models import User

user = User(name='lilei',age=18,salary=20000,birthdayday='1985-7-12 10:10:08') #创建对象
user.save()  # 向数据库插入一条数据

# 或者
# 创建对象并保存数据，一步完成
user= User.objects.create(name='lilei',age=18,salary=20000,birthdayday='1985-7-12 10:10:08') 

```

#### 2、删除数据

```python
user = User.objects.get(pk=3) / (id=3)
user.delete()   
# User.objects.get(pk=3).delete()
# 只删除id=3的数据 函数链 等价 user = User.objects.get(pk=3) user.delete() 

User.objects.all().delete()     # 删除所有数据
```

#### 3、修改数据

```python
user = User.objects.get(age=18)
user.name="new_name"
user.save()  # 注意：修改后要save()
```



### 五、查询操作

#### 1、QuerySet  

每个Model类都有一个默认的manager实例，名为objects。

对数据库中对象的检索， 是通过 model Manager 来构造一个 QuerySet 对象来实现。

 Model Manager QuerySet

- QuerySet 对象是一个model 类对应的实例集合，是一个可遍历的结构  。
- manger 对象是可理解为对QuerySet进行管理的一个类，可以通过manager的一些方法获取到QuerySet集合

```python
User.objects # 返回的是manager实例对象。由 Manager() 创建，用来进行查询

User.objects.all() # 返回的是一个QuerySet信息，它是通过manager的all()方法来返回的
```

#### 2、查询方法 

如下所有查询方法都是**QuerySet**实现的，只不过每个Model中都会有一个Manager,Manager接受到如下方法的调用时，会去调用**QuerySet**的方法，最终实现数据查询。

所以**QuerySet**这个类是查询动作的核心支撑。

Manager的任务是管理**QuerySet**，即，在需要的时候去调用QuerySet的对应方法。  

##### 2.1 基本查询方法

- all()  -- 返回值是QuerySet对象，包含了查询到的所有的数据行对应的Model对象

```python
User.objects.all() #返回QuerySet,其中是所有User的数据
# <QuerySet [<User: id:1, name:Tom, ,age:18, salary:1234.210000, birthday:1990-07-12 21:04:39+00:00>]>
```

- get()  -- 返回一个model对象

  注：返回查到的数据，没有数据或数据多于1条 报错

```python
# id为1的数据
User.objects.get(id=1)              #返回查到的数据，没有数据或数据多于1条 报错

#name='lilei' 且 age=18的数据
User.objects.get(name="lilei",age=18) #返回查到的数据，没有数据或数据多于1条 报错
```

- filter() -- 返回QuerySet对象 

  注：不管有没有对应数据，返回值均为QuerySet

```python
User.objects.filter(id=1)                # 返回一个QuerySet,其中是满足条件的数据

# 可以有多条数据，如果没有数据，就返回一个空白的QuerySet
User.objects.filter(name='lilei',age=18)   
```

- count()

```python
User.objects.count()       #数据数量
User.objects.all().count() #数据数量 和上面等价
User.objects.filter(age=18).count()  # 查询年龄为18的数据行数
```

- exclude() -QuerySet (了解)

```python
User.objects.exclude(pk=1) #和filter相反，取不满足条件的数据，返回QuerySet
User.objects.exclude(gender=True)# True/False 或者  1/0 和bool的filed比较
```

- first()  - 对象 （了解）

```python
User.objects.first() #获取QuerySet中的第一个元素，返回一个对象或None
```

- last() - 对象 （了解）

```python
User.objects.last() #获取QuerySet中的最后一个元素，返回一个对象或None
User.objects.filter(pk=1,name="lilei").last()
```

- exists() - Boolean （了解）

```python
User.objects.exists() #User对应的表中是否有数据，判断数据表是否为空。返回True/False
```

**补充：将QuerySet对象转为list**

```
list(User.objects.all())
```

##### 补充: 代码 可写在 项目中 tests.py文件中

~~~python
# 需要手动配置
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day03.settings")
django.setup()
# 导入models.py 即可
# 右键run即可
from modelapp.models import Employee,User

users = User.objects.all()
print(users)

~~~



##### 2.2 排序 order_by('列名')

```python
User.objects.order_by("pk") #根据id升序，返回QuerySet
User.objects.all().order_by("age")
User.objects.filter(age=18).order_by("-name")  # 
User.objects.all().order_by("age","-name") #根据age升序，age相同的根据name倒序
```



##### 2.3 限制操作

取结果集中的某一部分数据

```python
User.objects.filter(pk=1,name="lilei")[2] #返回QuerySet中第3个对象

uname="lilei" #可以使用变量在查询中
User.objects.filter(pk=1,name=uname)[2] #返回QuerySet中第3个对象

User.objects.exclude(pk=1,name="lilei")[1:3] #返回包含第[2,4)个对象(前闭后开)的新的QuerySet (子集)
User.objects.exclude(pk=1,name="lilei")[:3] # 等价于[0:3]
User.objects.exclude(pk=1,name="lilei")[2:] # 返回第3个到最后一个对象的新的QuerySet
```

select * from xxx where id >3

##### 2.4 条件查询

在众多查询方法中适合做条件查询的有：get(pk=1)、filter(name="xx")、exclude(pk=1)

get(pk=1,name="lilei") 如此只是等值查询，远不能满足查询需求。

对于比较运算：

并不支持【> < >= <=】这些符号的操作，替换为关键字lt、gt、lte、gte     

```python
User.objects.filter(pk__lt=10) #id小于10
User.objects.filter(pk__gt=100,age__lte=18) #id大于100且age小于等于18
#日期比较也可以
User.objects.exclude(birthday__gte="2018-5-22 12:12:12") #yyyy-mm-dd HH:MM:SS格式
User.objects.filter(birthday__gt=datetime.now())

dd = "2018-5-22 12:12:12"#使用变量
User.objects.exclude(birthday__gte=dd，name="xxx") #使用变量
```



##### 2.5 模糊查询

- contains、icontains            包含、包含（对大小写不敏感--忽略）    “%xx%”  
- startswith、istartswith       以..开始                                                       "xx%"
- endswith、iendswith          以..结尾                                                       "%xx"     

```python
User.objects.filter(name__contains="s") #name中包含"s"
User.objects.filter(name__icontains="s") #name中包含"s"或"S" 忽略大小写  ignore

User.objects.filter(name__startswith="s")
User.objects.filter(name__istartswith="s")# name是以"s"或"S"开始 忽略大小写

User.objects.filter(name__endswith="s")
User.objects.filter(name__iendswith="s")# name是以"s"或"S"结尾 忽略大小写
```



##### 2.6 范围查询

- in    在某个集合中    id__in=(1,2,4)     
- range 在某个范围中 id__range=(2,5) 

```python
User.objects.filter(name__in=("lilei","zz")) # where name in("lilei","zz")
User.objects.filter(age__in=(18,19,22))

User.objects.filter(age__range=(18,20)) # where age between 18 and 20  [18,20]
User.objects.filter(birthday__range=('2018-05-10','2018-06-14'))
```



##### 2.7 空值查询 

```python
User.objects.filter(age__isnull=True)   # 判断年龄是否为空
```



##### 2.8 日期查询（了解）

- year

- month  1-12

- day

- hour

- minute

- second

- week    一年的第几周  1-52 or 53

- week_day  周几 周日=1  周六=7

  ```python
  User.objects.filter(birthday__year="2018")
  User.objects.filter(birthday__month="1") # 生日是1月 可选值1-12
  User.objects.filter(birthday__week_day__gt=1) # 生日日期大于周日
  ```



##### 2.9 映射查询

`select * from t_user;`  查询全部列  

`select id,name from t_user;`查询部分列--映射查询

- values()  返回QuerySet对象，包含的元素都是dict
- only()      率先查询某些列

```python
User.objects.values() #  返回QuerySet对象，包含的元素都是dict   User.objects.values()

#查询部分列(返回QuerySet,其中每个元素都是一个dict)
User.objects.all().values("pk") #等价写法：select id from t_user;

User.objects.filter(age__lt=20).values("name")  # select name from t_user where age<20

#select id,age from t_user where name like "%m%"
User.objects.filter(name__contains="m").values("pk","age")
```

```python
#返回<QuerySet [<User>, <User>] >
users = User.objects.only("pk","name") #会率先查询id和name，其他列暂时不查
                                       #即，QuerySet内的User中暂时只有id和name有值
users[0].age #用到其他列数据时，才会查询它
#此处涉及到延缓查询的特性：lazy-load
```



##### 2.10 聚合函数 - aggregate

- Max( )
- Min( )
- Avg( )
- Sum( )
- Count( ) 

```python
from django.db.models import Count, Max,Avg,Min,Sum
#返回 {'pk__max': 4, 'name__min': '2134'}
User.objects.aggregate(Max("pk"),Min('salary')) #select max(id),min(salary) from t_user;

#可以定义别名，影响返回值结构 -- 返回 {'mm': 4, 'name__min': '2134'}
User.objects.aggregate(max = Max("pk"),min = Min('salary'))#select max(id) as mm,min(salary) from t_user;
```



##### 2.11 分组查询 - annotate

语法：	

```
Models.objects.values('age').annotate(Max("salary")) 
# 分组查询时，是将values中的列作为分组条件的列
```

示例：

```python
User.objects.values('age').annotate(Count('age'));
# select age,Count(age) from userlist group by age;
```

```python
#每种年龄中的用户的最大id和用户的最小生日
#select age,max(id),min(birthday) from t_user group by age
User.objects.values("age").annotate(Max('pk'),Min('birthday'))

#大于18的每种年龄中的用户的最大id和用户的最小生日
#加where : select age,max(id),min(birthday) from t_user where age > 18 group by age
User.objects.values("age").filter(age__gt=18).annotate(Max('pk'),Min('birthday'))

#加别名
User.objects.values("age").filter(age__gt=18).annotate(Min('birthday'),mm=Max('pk'))

#加having : select age,max(id),min(salary) from t_user having max(id)>3
User.objects.values("age").annotate(Min('salary') ,p = Max('id')).filter(p__gt=3)

#加排序
User.objects.values("age").filter(age__gt=18).annotate(Min('birthday'),mm=Max('pk')).order_by('mm')
```



##### 2.12 F()和Q()函数

User.objects.filter(id__gt=1) #id大于1

问题：查询id大于age的用户？  尝试：User.objects.filter(id__gt=age)--错误

​                                                                  User.objects.filter(id__gt="age")--错误

- **当查询条件中需要另外的列时，可以使用F**


User.objects.filter(id__gt=F('age'))--正确

```python
from django.db.models import F
User.objects.filter(id__lt=F('age')) #id小于age
User.objects.filter(id__lt=F('age')+1) #id小于age+1
User.objects.filter(id__lt=F('age')*10/2) #id小于age*10/2
User.objects.filter(id__lt=F('age')+F('salary')) #id小于age+salary
User.objects.filter(id__lt=2,name__contains="a") #id小于2 而且 name包含“a”
```



- **当需要 “或 （|） 非（~）” 逻辑时，可以使用Q**


```python
from django.db.models import Q
User.objects.filter(Q(id__gt=3)|Q(id__lt=2)) #id大于3 或 id小于2
User.objects.filter(Q(id__gt=3)|~Q(name__contains="e")) #id大于3 或 name不含有“e”
User.objects.filter(Q(id__lt=3)|Q(age__gt=F("id")*10)) #id小于3 或 age大于id*10

User.objects.filter(Q(id__gt=3)|Q(name__contains="e")，age__lt=2) #id大于3 或 name包含"e" 且 age小于2

User.objects.filter(Q(id__gt=3)|Q(name__contains="lilei")，~Q(age__lt=2) #id大于3 或 name包含"ee" 且 age不小于2
```



### 六、Raw-SQL  

如果以上的支持不能满足需求，Django也支持直接执行原生SQL语句。   

```python
users = User.objects.raw("select id,name from userlist where id=1")
users = User.objects.raw("select id,name from userlist where age=%s and name=%s",[18,'lilei'])
for user in users:
    print(user)
    
# 注意不要在外部拼接sql字符串
sql_str = "select id,name from userlist where age=%d and name='%s'"%(18,'lilei')
User.objects.raw(sql_str) # 会有sql注入风险

	sql_str = "select id,name from userlist where age=%d and name='%s'"%(18,"' or '1'='1")
```



