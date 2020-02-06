# 模型_02

### 一、关联关系

#### 1、概述

关联关系指的是数据表之间的数据是相互依赖和影响关系，表之间有**从属关系**，比如，有一个用户表，用户又有订单表，则用户表与订单表之间就存在从属关系。



#### 2、关联关系的种类

- 一对一    一个人一本护照                   
- 一对多    一个部门可以有多个员工  
- 多对多    一个学生有多门课，一门课有多个学生    



#### 3、Model中的关联关系

##### 3.1 关系类型字段

- ForeignKey(to=关系对方的类或类名或‘self’，on_delete=级联选项)
- OneToOneField(to=关系对方的类或类名或‘self’，on_delete=级联选项)
- ManyToManyField(to=关系对方的类或类名或‘self’)



#### 4、关联关系Model搭建

##### 4.1 一对多Model

```python
1:*
class Category(models.Model):
    title = models.CharField(max_length=20)
    note = models.CharField(max_length=20)
    class Meta:
        db_table="t_category"

class Goods(models.Model):
    title = models.CharField(max_length=20,unique=True)
    price = models.FloatField()
    cate = models.ForeignKey(to=Category,on_delete=models.CASCADE) #关系属性 主表删除后，从表中使用主表中数据的也会跟随一起删除
    class Meta:
        db_table = "t_goods"
```

##### 4.2 一对一Model

```python
1:1
class Passport(models.Model):
    note = models.CharField(max_length=20)
    person = models.OneToOneField(to="Person",on_delete=models.CASCADE,null=True) #关系属性
    class Meta:
        db_table="t_passport"

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        db_table="t_person"
```

##### 4.3 多对多Model

```python
*:*
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        db_table="t_student"
        
class Course(models.Model):
    title = models.CharField(max_length=30)
    expire = models.SmallIntegerField()
    stu = models.ManyToManyField(to=Student) #关系属性
    class Meta:
        db_table="t_course"
```



#### 5、关联关系查询

##### 5.1 一对一查询 

```python
# 1.只查 单方数据 （与单表数据查询一致）
# 只查人的信息
ps = Person.objects.filter(name='Tom').values()
print(ps)
# 只查 护照的信息
p1 = Passport.objects.all().values()
print(p1)
ps = Person.objects.filter(passport='1').values()
print(ps)

# 2.通过一方查另一方数据 (先获取一方数据，再通过它查询另一方)
# 查询 名字为tom的护照信息
p1 = Person.objects.get(name='Tom')
print(p1.passport.note)
# 查询护照为美国的人的信息
ps = Passport.objects.get(note='美国')
print(ps.per_id, ps.per.name,ps.per.age)

# 3.通过一方 查另一方 (查询条件是对方)
# 查询名字为tom的护照信息
p1 = Passport.objects.filter(per__name='Tom').values()
print(p1)
# 查询护照为美国的人的信息
p1 = Person.objects.filter(passport__note='美国').values()
print(p1)
print(Person.objects.filter(passport__note='美国'))  # QuerySet集合对象

# 4.保留双方数据 ()
# 查询名字为Tom的人信息 和 护照的信息
p1 = Person.objects.filter(name='Tom').values('name','age','passport__note')
print(p1)
p1 = Passport.objects.filter(per__name='Tom').values('note','per__name','per__age','per_id')
print(p1)

```

##### 5.2 一对多查询

```python
# 1对多关系   Category(1)：没有关系属性   Goods(*)：其中有关系属性cate
# 一对多 查询  category主表 goods从表

# 1.只查询一方数据
# 只查 主表
c1 = Category.objects.filter(name='服装').values()
print(c1)
g1 = Goods.objects.filter(price=5000).values()
print(g1)

# 2.通过一方查询另一方 (先查询到一方数据,再通过它查询另一方)
# 查询服装类别为男装的 商品名称
c1 = Category.objects.get(name='服装')
print(c1.goods_set) # 查询也是一个集合
print(c1.goods_set.all()) # 查询也是一个集合
# 查询 商品沙发所属的类别
g1 = Goods.objects.get(title='沙发')
print(g1.cate.name, g1.cate.note)

# 3.通过一方查询另一方(查询条件是另一方)
# 查询 床 商品的 类别信息
c1 = Category.objects.filter(goods__title='床').values()
print(c1)
# 查询分类为 家居 类别的 商品信息
g1 = Goods.objects.filter(cate__name='家居').values()
print(g1)

# 4.保留双方数据
# 查询商品名称为 电视 的分类信息 和 商品信息
c1 = Category.objects.filter(goods__title='电视').values('name','note','goods__title','goods__price')
print(c1)
# 查询商品价格大于5000的商品的分类信息
c1 = Category.objects.filter(goods__price__gt=5000)
print(c1)
print(set(c1))

#注意在进行联合查询时，可能会由重复数据出现，解决：
list(set(Category.objects.filter(goods__price__gt=200)))
```



##### 5.3 多对多查询

```python
# 多对多关系   Course：有对方关系属性students   Student：没有对方关系属性 

# 1.只查询一方
# 查询学生 linda 学生信息
s1 = Student.objects.filter(name='Linda').values()
print(s1)
# 查询mysql课程信息
c1 = Course.objects.filter(title__icontains='MYSQL').values()
print(c1)

# 2.查询一方,通过它查询另一方
# 查询 学习mysql的学生信息
c1 = Course.objects.get(title='DJANGO')
print(c1.stu.all())
# 查询 学生 linda 课程信息
s1 = Student.objects.get(name='Linda')
print(s1.course_set.all())
print(s1.course_set.values())

# 3.通过一方 查询 另一方 (查询条件为对方)
# 查询 学生 linda 课程信息
c1 = Course.objects.filter(stu__name='Linda').values()
print(c1)
# 查询 学习mysql的学生信息
s1 = Student.objects.filter(course__title='PYTHON').values()
print(s1)


# 4.保留双方数据
# 查询学习django的学生信息 和 课程信息
s1 = Student.objects.filter(course__title='DJANGO').values('name','age','course__title','course__expire')
print(s1)
# 查询jack学习的课程信息 和 学生信息
c1 = Course.objects.filter(stu__name='Jack').values('title','expire','stu__age','stu__name')
print(c1)


#关联查询
Student.objects.filter(course__title__contains="h") #标题中含有"h"的课程中的学生
Course.objects.filter(stu__name="zzz") #姓名为zzz的学生参加的课程
Course.objects.filter(stu__age__gt=18) #年龄大于18的学生参加的课程
```



#### 6、增加数据

- 单独增加主表方(没有外键一方) 和单表增加无差异

```python
c = Category(title="男装",...)
c.save()
```

- 为已存在的主表方附加从表数据（常见的增加情形）

```python
# 方式一： 先取某一个类别，再通过该类别创建一个商品
c = Category.objects.get(pk=1)   # 获取类别一对象
c.goods_set.create(title = 'abc',price=139.99)   # 不需要再save

# 方式二：先取某个类别，单独创建商品并关联类别
c = Category.objects.get(pk=1)
g = Goods.objects.create(title='abc',price=213,cate=c) #为商品的关系属性赋值

# 注意：如果是1：1，则只能使用方式二
```

- 同时添加主从数据

```python
c = Category(title="类别1",note="xx")
g = Goods(title="zzz6",price=100)
g.save() #此时，外键的值为null
c.save()
c.goods_set.add(g) #会同步数据库,补充外键值

或

c = Category(title="类别1",note="xx")
c.save()
g = Goods(title="zzz6",price=100，cate9=c)
g.save() #此时，good是有外键值的
#注意如果是1:1只能用第二种

```

#### 7、删除数据

- 单独删除从表方，和删除单表无差异

```python
Goods.objects.get(pk=1).delete()
```

- 删除主表方，此时要看从表方的级联设置，会影响到从表方

  级联选项 : 在关联关系中删除主表时，对于从表可以有级联操作

  - CASCADE  级联删除
  - SET_NULL  外键置空(如果允许空的话)
  - PROTECT   不允许直接删除主表
  - SET_DEFAULT  需要为外键列设置默认值，默认值也应该是合法的外键值，可以在表中预留一个id
  - SET   将外键设置为某个值，值应该是合法的外键值，可以在表中预留一个id
  - DO_NOTHING   django什么也不做，由数据库决定是否合法

` *:*  不支持级联删除`      

```PYTHON
 #如果要删除主，所有从的外键置null  （重要）
 per = models.OneToOneField(to=Person,on_delete=models.SET_NULL,null=True)
 #如果要删除主，所有从一起删除
 per = models.OneToOneField(to=Person,on_delete=models.CASCADE,null=True)
 #如果要删除主，django什么也不做，有数据库决定是否合法
 per = models.OneToOneField(to=Person,on_delete=models.DO_NOTHING,null=True)
 #如果要删除主，所有从的外键置为6  （重要）
 cate = models.ForeignKey(to="Category",on_delete=models.SET(6))
 #如果要删除主，所有从的外键置为默认值5  （重要）
 cate = models.ForeignKey(to="Category",on_delete=models.SET_DEFALUT,default="5")
 #如果要删除主，如果有从数据存在，不允许删除
 cate = models.ForeignKey(to="Category",on_delete=models.PROTECT)
```

#### 8、修改数据

查询出数据，修改属性，然后save()即可

```python
cs = Category.objects.all()
c = cs[0]
c.title="new_title"
c.save()

# 坑：
Category.objects.all()[0].title="new_title"  #查询一次，并修改
Category.objects.all()[0].save() #查询一次，并保存

cate1=Category.objects.all()[0]
cate1.title="new_title"
cate1.save()
```

### 二、懒加载Lazy-load    

QuerySet在查询数据时，是延迟执行，直到真正使用了数据，才发起查询

```python
a = Person.objects.all() #未查询
b = Category.objects.all() #未查询
print(a) #查询了a
#如上代码只执行了一次查询

c = Category.objects.all() #未查询
print(c) #查询c
goods = c[0].goods_set.all() #未查询goods
print(goods) #查询了goods
```

- 测试方式

  找到mysql的安装目录下的my.ini文件，添加配置：

```mysql
# SERVER SECTION
[mysqld]
.....
log = "E:/mysql_log.log" #设置日志文件，记录sql语句执行
或
general-log=1
general_log_file=E:/mysql_log.log

#需要重启Mysql服务   net stop/start mysql   
```

