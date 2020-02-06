# Flask-Model 

### 一、简介

#### 1、ORM

ORM 全称 `Object Relational Mapping`，对象关系映射。简单的说，ORM 将数据库中的表与面向对象语言中的类建立了一种对应关系。这样，我们要操作数据库，数据库中的表或者表中的一条记录就可以直接通过操作类或者类实例来完成。 



#### 2、SQLAlchemy

SQLAlchemy是一个基于Python实现的ORM框架。该框架建立在 DB API之上，使用对象关系映射进行数据库操作，简言之便是：将类和对象转换成SQL，然后使用数据API执行SQL并获取执行结果。



#### 3、Flask-SQLAlchemy  

Flask-SQLAlchemy 是一个为 Flask 应用增加 SQLAlchemy 支持的扩展。 它致力于简化在 Flask 中 SQLAlchemy 的使用，提供了有用的默认值和额外的助手来更简单地完成常见任务。 



### 二、安装和配置

#### 1、安装

- `pip install flask-sqlalchemy`  ，安装`flask-sqlalchemy`时会自动安装`sqlalchemy`。
- `pip install mysqlclient` ，本节我们使用mysql数据库，因此需要安装mysql数据库驱动。



#### 2、配置

```python
from flask_sqlalchemy import SQLAlchemy

# mysql配置                            数据库类型 用户名 密码   ip        数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost/flask_db"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True #避免警告信息
db = SQLAlchemy(app)    
```



### 三、使用Flask-SQLAlchemy

#### 1、定义Model类

```python
# 新建models.py文件
from app import db     # 从app.py模块引入db对象

class User(db.Model):                              # 基于db.Model构建User类，与数据库建立映射
    __tablename__="t_user"                       # 自定义表名，默认名为类名小写"user"    
    id = db.Column(db.Integer,primary_key=True)    # 必须有主键存在
    name = db.Column(db.String(20),nullable=True)  
    age = db.Column(db.SmallInteger)
    gender = db.Column(db.Boolean)
```

#### 2、创建表

为了创建初始数据库，只需要从交互式 Python shell （python console面板）中导入 db 对象并且调用` SQLAlchemy.create_all() `方法来创建表和数据库: 

```python
>>> from app import db
>>> from models import User
>>> db.create_all()     # 创建表
>>> db.drop_all()      # 删除所有表
```

**注意：**也可以自己去建表，只要表名 和 表中的列和Model中的属性，可以一一对应即可



#### 3、字段类型

```python
class Test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column("name2",db.String(20)) #自定义列名
    age = db.Column("age2",db.SmallInteger) #自定义列名
    count = db.Column(db.BigInteger)
    salary = db.Column(db.Float)
    price = db.Column(db.Numeric(5,2))  # decimal
    note = db.Column(db.Text) # 存储大量文本
    note_uni = db.Column(db.Unicode(20))
    note_uni2 = db.Column(db.UnicodeText)
    gender= db.Column(db.Boolean)
    birth = db.Column(db.DateTime)
```

```python
CREATE TABLE `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name2` varchar(20) DEFAULT NULL,
  `age2` smallint(6) DEFAULT NULL,
  `count` bigint(20) DEFAULT NULL,
  `salary` float DEFAULT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  `note` text,
  `note_uni` varchar(20) DEFAULT NULL,
  `note_uni2` text,
  `gender` tinyint(1) DEFAULT NULL,
  `birth` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```



#### 4、字段参数

```python
db.Column(...,primary_key=True)
db.Column(...,unique=True)
db.Column(...,nullable=False)
db.Column(...,index=True)
db.Column(...,default=18) # 不作用在数据库，在保存数据时，默认值18
db.Column(...,server_default="12.52") # 作用在数据库  ，server_default的值必须是字符串格式
db.Column(...,server_default="lilei") # 作用在数据库
db.Column(db.DateTime,server_default="2018-12-12")
db.Column(db.TIMESTAMP, server_default=text('now()')) # 只有时间戳可以用now设置默认值
```



#### 5、表参数

```python
#联合主键：只要为多个列设置primary_key=True即可
class Test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    id2 = db.Column(db.Integer,primary_key=True)
    ...
    
class Test(db.Model):
    __tablename__ = "自定义表名"
    id = db.Column(db.Integer)
    id2 = db.Column(db.Integer)
    id3 = db.Column(db.Integer)
    id4 = db.Column(db.Integer)
    __table_args__ = (
        UniqueConstraint("id3", "id4"), # 联合唯一
        PrimaryKeyConstraint('id', 'id2', name='pks9'), # 联合主键
        Index("inds9","id3","id4") # 联合索引
    )
```



### 四、数据库CURD

创建（Create）、更新（Update）、读取（Retrieve）和删除（Delete）操作。

#### 1、简单查询

##### 1.1 Model.query属性

Flask-SQLAlchemy 在 Model 类中提供了 query 属性，当访问该属性时，会得到一个查询对象BaseQuery。

```python
User.query          # BaseQuery,打印BaseQuery可以输出对应的sql语句
User.query.all()    # list of User 直接获取所有Model的列表
```

##### 1.2 主键查询

```python
# get()函数仅仅用于通过主键进行条件查询

User.query.get(1) # select ... where id=1  如果没有数据返回None
User.query.get(2)
```



#### 2、条件查询

##### 2.1 filter_by

基本语法:

`User.query.filter_by(属性名1='xxx'，属性名2='xxx')`     返回值为BaseQuery

注意：`filter_by()`仅用于等值查询。

```python
query = User.query.filter_by(name='Tom')        
query = User.query.filter_by(name="tom",id=1) 

```



##### 2.2 filter

基本语法：

`User.query.filter(类名.属性名1=='xxx'，类名.属性名2=='xxx')`     返回值为BaseQuery

示例：

```python
from sqlalchemy import or_, and_

User.query.filter(User.id == 1)       # 返回BaseQuery
User.query.filter(User.name == "Tom") 
User.query.filter(User.id == 1,User.name == "Tom") # 且  
User.query.filter(and_(User.id == 1,User.name == "Tom")) # 且

User.query.filter(or_(User.id > 1,User.name != "Tom")) # 或
User.query.filter(User.id >=1,User.name.like("%j%")) # 模糊查询
User.query.filter(User.id.in_((1,2,3)),User.name.like("%j%")) # in
User.query.filter(~User.id.in_((1,2,3)),~User.name.like("%j%")) # 非
User.query.filter(User.id.between(1,4),User.name.like("%j%")) # between 1 and 4 ==[1,4]
User.query.filter(User.name != None) # is not null
User.query.filter(User.name != None).count() # BaseQuery.count() 计数
```



##### 2.3  BaseQuery获取数据

BaseQuery提供了all()、first()、one()等方法，进步一获取具体数据

| 方法          | 描述                                           | 示例                                                         |
| ------------- | :--------------------------------------------- | ------------------------------------------------------------ |
| all()         | 获取查询到的query中的所有数据，Model的列表     | User.query.all()                            User.query.filter(xxx).all() User.uqery.filter_by(xxx).all() |
| first()       | 获取查询到的query中的第一个Model，没有返回None | User.query.first()                          User.query.filter(xxx).first() User.uqery.filter_by(xxx).first() |
| one()         | 返回一个Model，如果有多个Model或没有则报错     | User.query.filter(User.id==1).one() User.query.filter_by(id=1).one() |
| one_or_none() | 返回一个Model或None，如果有多个Model报错       | User.query.filter(xxx).one_or_none() User.query.filter_by(xxx).one_or_one() |
| count()       | 返回查询到的query中的Model数量                 | User.query.count()                            User.query.filter(xxx).count() User.query.filter_by(xxx).count() |

```
query[0]  # 获取查询到的结果中的第1条数据 
qeury[0:] # BaseQuery支持切片，返回list
qeury[:3] 

query.all()
query.all()[0]
query.all()[0:]
query.all()[:3]
```



#### 3、映射查询

##### 3.1 db.session使用  

映射查询在SQLAlchemy中，可以通过session对象的query方法完成。query方法非常灵活，你可以根据需要使用不同的查询方式查找数据。

基本语法：

- `db.session.query(Model)`    **查询Model中的所有列**，返回BaseQuery  等价于` Model.query`

  ```python
  # query与query2等价   
  query = db.session.query(User)
  query2 = User.query
  print(type(query))      # 返回BaseQuery
  print(type(query2))     # 返回BaseQuery
  print(query)
  print(query2)   
  db.session.query(User).filter(User.id == 1).all()
  ```

  因此，也可以使用db.session.query(User)去调用all()、filter()、first()、one()等方法。

  

- `db.session.query(Model.property1,Model.property2..)`  **查询Model中的指定列**（**部分列**）

  ```python
  db.session.query(User.id,User.name).filter(User.id == 1).all()  # 查询id为1的用户的id和name
  ```

总结：对于Flask SQLAlchemy操作，即可以使用Model.query，也可以使用db.session.query。



#### 4、排序

```python
from sqlalchemy import desc, asc
# 按年龄排序，查询用户的信息   默认升序
db.session.query(User).order_by(User.age).all()    
# 按年龄排序，查询用户的姓名和年龄
db.session.query(User.name,User.age).order_by(User.age).all()
# 按年龄排序，年龄相同则按id排序
db.session.query(User).order_by(User.age,User.id).all()

# desc函数 降序排列
db.session.query(User).order_by(desc(User.age),asc(User.id)).all()   
```



#### 5、聚合函数

```python
from sqlalchemy import func
db.session.query(
    func.sum(User.id),
    func.min(User.name),
    func.avg(User.age),
    func.max(User.id),
    func.count(User.id)
) #返回BaseQuery
```



#### 6、分组

```python
# 以年龄分组，查询id之和
db.session.query(func.sum(User.id)).group_by(User.age).all()
db.session.query(func.sum(User.id)).group_by(User.age).having(func.min(User.id)<3)
# having条件限制
db.session.query(func.sum(User.id)).group_by(User.age).having(func.min(User.id)<3).all()
```



#### 7、增删改

```python
更新：
user = User.query.get(1)
user.age=11
# 事务控制
# db.session.rollback()
db.session.commit()  

删除：
user = User.query[1]
db.session.delete(user)
# 事务控制
# db.session.rollback()
db.session.commit()

增加：
user = User(name="lilei",age=22)
user2 = User(name="lilei2",age=23)
db.session.add(user)
# db.session.add_all([user,user2])#添加多个
db.session.commit()#提交
# db.session.rollback()#回滚
```



#### 8、分页查询

```python
pag = db.session.query(User).paginate(page=1,per_page=2)
print(pag.query)
print(pag.query.all())

print(pag.iter_pages()) #页序号
print(pag.pages)  # 共有多少页
print(pag.items)  # 当前页的数据
print(pag.total)  # 共有多少行
print(pag.per_page) # 每页几行
print(pag.has_next) # 是否有下一页
print(pag.has_prev) # 是否有上一页
print(pag.next_num) # 下一页页号
print(pag.prev_num) # 上一页页号

# 将pag传到模板文件中 
```



**补充：原生sql支持**  

```python
# 原生sql 

statement = text("select id,name from user where id>:id").params(id=1)
print(type(statement))
query = db.session.query(User.id,User.name).from_statement(statement)
print(query.all())

statement2 = text("select max(id) as mid,max(age) as mage from user where id> :id").params(id=1)
users = db.session.query('mid','mage').from_statement(statement2).all()
print(users)

 result = db.session.execute("select * from userlist where id>:id",{"id":2})
 print(result.fetchone())
 print(result.fetchone())
 result.fetchone()
 result.fetchmany(2)
 result.fetchall()
```



### 五、关联关系

#### 1、一对多关系

##### 1.1 Model类声明

```python
# Model类
class Department(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    # 主表中的 relationship用于搭建关联关系 
    employees = db.relationship('Employee',backref='dept',lazy='dynamic')

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    # 在从表中，定义外键，并指定主键的位置（数据库表中的字段）
    dept_id = db.Column(db.Integer,db.ForeignKey('department.id'))  # 表名.列名
```

##### 1.2 增加数据

- 同时增加双方

  ```python
  # 单独声明dept和emp
  dept = Department(id=1,title='教学部')
  emp = Employee(id=1,name="Tom")
  # 向dept的emppolyees中追加emp
  dept.employees.append(emp)
  # 将dept添加到数据库会话连接中
  db.session.add(dept)
  db.session.commit()
  ```

- 增加一方

  ```python
  # 从数据库中获取主表中的一条数据
  dept = Department.query.get(1)
  # 声明从表对象
  emp = Employee(id=2,name="Jack")
  # 向主表中的employees中追加从表对象
  dept.employees.append(emp)
  db.session.commit()
  ```

  ```python
  dept = Department.query.get(1)
  emp = Employee(id=3,name="Linda")
  emp.dept = dept       # 通过backref搭建关系
  db.session.commit()
  ```



##### 1.2 删除数据

```python
dept = Department.query.get(1)
db.session.delete(dept)          # 删除主表方，从表的外键将置为空
db.session.commit()
```



##### 1.3 级联行为

在主表中，声明关联关系时，可以设置cascade

 `orders = db.relationship("Employee",...，cascade="save-update，delete")`

`cacade='all/save-update/delete'  `   save-update为默认

- **save-update :** 在增加和修改主时，级联增加修改从
- **delete :** 在删除主时，级联删除从 (慎用)
- **all :** 所有级联行为



##### 1.4 主从查询

- 通过主表，查询从表数据（通过一查询多）

  ```python
  depts = Department.query
  depts.all()  # 不会查询employess
  # 查询关系一方时，对于关系对方会延迟查询（lazy-load）
  
  emp = depts.all()[0].employees  # 主表中的关系属性 得到AppenderBaseQuery对象
  print(emp.all())
  ```

- 通过从表，查询主表数据（通过多查询一）

  ```python
  emp = Employee.query.all() # 不会查询Dempartment
  print(emp[0].dept)         # 通过backref反查主表方
  ```



##### 1.5 表连接

- 表连接，查询但保留一方数据

  ```python
  Employee.query.join(Department)
  Department.query.join(Employee)
  Employee.query.join(Department).filter(Department.id==2)
  ```

- 表连接，查询并保留双方数据

  ```python
  # 内连接
  # 单独查一方数据
  Employee.query.join(Department).all()
  Employee.query.join(Department).filter(Department.id > 2).all()
  # 内连接 查询双方数据
  db.session.query(Department,Employee).join(Employee)
  # 外连接
  db.session.query(Department,Employee).outerjoin(Employee)
  db.session.query(Employee,Department).outerjoin(Department)
  # 多表连接
  db.session.query(Employee,Department,Area).join(Department).join(Area)
  
  ```



##### 1.6 lazy选项

- 'select' (默认值) 就是说 SQLAlchemy 会使用一个标准的 select 语句必要时一次性加载所有数据。
- 'joined' 告诉 SQLAlchemy 使用 JOIN 语句作为父级在同一查询中来加载关系。

- 'subquery' 类似 'joined' ，但是 SQLAlchemy 会使用子查询。

- 'dynamic' 在有多条数据的时候是特别有用的。不是直接加载这些数据，SQLAlchemy 会返回一个查询对象， 在加载数据前您可以过滤（提取）它们。


实例：

```python
dept = Department.query
emps = dept[0].employees
select : Department.query  时只查询Department ; employees是list of Employee     
joined：Department.query时通过join连接查询双方 (查询时，负载过重)
dynamic：Department.query时只查询Department ; empolyee是BaseQuery (建议使用的懒加载模式)    
```

注意：lazy选项只适用于一对多中主表方，和多对多



#### 2、多对多关系

##### 2.1 创建Model类

```python
tags = db.Table(
    "t_student_course", #表名
     db.Column("student_id",db.Integer,db.ForeignKey("student.id"),primary_key=True),
     db.Column("course_id", db.Integer,db.ForeignKey("course.id"),primary_key=True)
)


class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    courses = db.relationship("Course",secondary=tags,backref='stus',lazy="dynamic")

    # student加载course是懒加载，course加载student时也是懒加载。懒加载只能给一对多的主表和多对多的双方
    # courses = db.relationship("Course", secondary=tags,        
    #                           backref=db.backref("stus",lazy="dynamic"), lazy="dynamic")

class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    expire = db.Column(db.SmallInteger)
```

##### 2.2 增加数据

- 增加双方

```python
# 通过学生添加课程
student = Student(id=1,name="Tom")
course = Course(id=1,title='Mysql',expire=2)
student.courses.append(course)
db.session.add(student)
db.session.commit()
```

```python
# 通过课程添加学生
student = Student(id=2,name="Jack")
course = Course(id=2,title='Linux',expire=2)
course.stus.append(student)
db.session.add(course)
db.session.commit()
```

- 增加一方

```python
# 给学生1添加课程2
student = Student.query.get(1)
course = Course.query.get(2)
student.courses.append(course)
db.session.commit()
```

```python
# 给课程1添加学生2
student = Student.query.get(2)
course = Course.query.get(1)
course.stus.append(student)
db.session.commit()
```



##### 2.3 查询数据

- 查询一方（通过一方查另一方）

```python
# 通过学生查课程
students = Student.query.all()
cs = students[0].courses.all()
print(cs)

# 通过课程查学生
courses = Course.query.all()
st = courses[0].stus
print(st)
```

- 联合查询

```python
# 保留一方数据
db.session.query(Student).join(Student.courses).all()
db.session.query(Course).join(Course.stus).all()
# 查询双方所有数据
db.session.query(Student,Course).join(Student.courses) 
# 查询学生id=1的学生信息和对应的课程信息
db.session.query(Student,Course).join(Student.courses).filter(Student.id == 1)
# 查询课程id=1的课程信息和对应的学生信息
db.session.query(Course,Student).join(Course.stus).filter(Course.id==1)
坑: Course 连接 Student表时，不能查询具体字段，只能查询整个对象
```



##### 2.4 删除数据

```python
c = Course.query.get(2)
db.session.delete(c)
db.session.commit()
```



#### 3、一对一关系

##### 3.1 定义Model类

```python
class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    passport = db.relationship('Passport',uselist=False,backref='person')# uselist默认为True 1:*

class Passport(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    note = db.Column(db.Model)
    person_id = db.Column(db.Integer,db.ForeignKey('person.id'))
```



##### 3.2 增加数据

- 增加双方

```python
person = Person(name="Tom")
passport = Passport(note="中国")
person.passport = passport
db.session.add(person)
db.session.commit()

#通过passport来添加person
person = Person(name="Tom")
passport = Passport(note="中国")
passport.person = person
db.session.add(passport)
db.session.commit()
```

- 增加一方

```python
person = Person.query.get(2)
passport = Passport(note="美国")
person.passport = passport
db.session.commit()

#通过passport添加person
port = Passport.query.get(4)
per = Person(id=4,name='polly')
port.person = per
db.session.commit()
```

##### 3.3 删除

```python
per = Person.query.get(1)
db.session.delete(per)
db.session.commit()  #从表外键置空，如果要将从表数据一起删除，需要设置cascade
```

##### 3.4 查询

```python
#通过一方查另一方
person = Person.query.get(1)
passport = person.passport #获取对方（没有懒加载）

#联合查询
person = Person.query.join(Passport) # 表连接
passport = person[0].passport  # 获取对方
db.session.query(Person,Passport).join(Passport).filter(Person.id == 2) # 表连接，留双方数据
```

 