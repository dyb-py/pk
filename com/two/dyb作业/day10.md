## 一.索引

### 1.索引作用

在查询数据表的时候，默认是从第一行数据一次查到最后一行。数据俩个多的时候，查询很耗时。如果作为查询条件的列有索引，就可以不必遍历每一条数据（查找的速度会很快）。

### 2.创建索引

​	表中的主键列和外键列和唯一列自动有索引

##### 	2.1 单列索引

```mysql
-- 1.建表的时候创建索引
create table t_user(id int auto_increment primary key,
                   name varchar(20),
                   age int,
                   index age_index(age)
                   );
-- 2.表外添加索引
-- create index 索引名   on 表名(索引列)
create index name_index on t_user(name);
```

##### 	2.2查看索引

```mysql
show index from 表名;
```

##### 	2.3删除索引

```mysql
drop index 索引名 on 表名;
drop index name_index on t_user;
```

##### 	2.4联合索引(复合索引)

```mysql
create index 索引名 on 表名(索引1,索引2,索引3...)
```

```mysql
select * from t_user where name="zhangsan" and age=18 and pid=1;
```

最左原则:

(name) (name,age) (name,age,pid)

联合索引如果是where...and...的话，联合查询的效率会更高

用and拼接的多个条件，先后顺序无所谓，但一定要遵循最左原则。

注意：or 不会使用联合索引，in not in ...

### 3.索引使用注意事项

```
1.索引对查询有增益，使查询速度更加快
2.索引不是越多越好。
	2.1 对于修改较多的表，不适合做过多索引
	2.2 对于查询较多的表，如果索引添加过多，会导致对存储空间的严重消耗。
	2.3.对于增删改来说，会有额外的索引维护时间消耗
```

## 二.SQL分类(了解)

```mysql
DQL：data query language数据查询语言： select，where,order by,group by,having
DDL: data definition language数据定义语言： create alter，drop
DML：数据操作语言 ： insert，update，delete
TPL：事务处理语言：commit rollback
DCL：数据控制语言：grant，revoke
```

grant all privilieges on \*.\* to "root" '@%‘ indentified by '密码' with grant option;

flush privileges;  # 刷新特权，使上述操作生效

## 三.python连接mysql

```python
1.mysql-connector-python    mysql官方提供的包，纯python构建的
2.PyMySQL  纯python构建的
3.mysqlclient    c构建的
4.cymysql   c构建的
5.mysqldb     # 不适用python3
```

### 1.安装

- pip install mysqlclient   联网一键安装
- 使用.whl文件安装

补充：pip install 包名    下载安装第三方包

​	   pip uninstall 包名  写在第三方包

​	   pip download 包名   下载第三方包

### 2.连接数据库

```python
import MySQLdb
conn = MySQLdb.connect(
    host="localhost",   #mysql所在的主机
    port=3306,   # 端口号
    user="root", # 连接的用户名
    password="123456", # 密码
    db="userdb", # 连接的数据库
    charset="utf8" # 连接使用的字符集
)
```

### 3.获取游标对象

```python
cursor = conn.cursor()
```

### 4.执行sql语句

```python
conn.begin()  # 开启事务（增删改操作需要做）
cursor = conn.cursor()  # 获取一个游标对象
# 执行一个查询sql语句, select语句返回的是查询到多少条数据
result = cursor.execute("select * from student")
print(result)

# 执行一个插入sql语句
names = "dachuiss"
age = 100
sql = "insert into student(name,age)values('{}','{}')".format(names,age)# 格式化sql语句
cursor.execute(sql)  # 执行sql语句
conn.commit()   # 提交

```

### 5.执行查询

```python
# cur = conn.cursor()
# result = cur.execute("select * from student where id < 4")
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchmany(3))
# print(cur.fetchall()[1][1])
注意：显示的结果就是在查询结果范围内。
```

### 6.游标类型选择

```mysql
cursor = conn.cursor(MySQLdb.cursors.DictCursor)
result = cursor.execute("select * from student where id < 4")
print(cursor.fetchall())
```

### 7.控制游标移动

```python
# 操控游标移动
# cursor = conn.cursor()
# result = cursor.execute("select * from student")
# print(cursor.fetchall())
# # 绝对定位，第一个参数的意思是从0开始（第一条数据）往后移动几位，mode=“”设置定位方式
# # cursor.scroll(0,mode="absolute")
# print(cursor.fetchall())

# 相对定位：从当前的游标位置往后移动
cursor = conn.cursor()
result = cursor.execute("select * from student")
print(cursor.fetchmany(3))
cursor.scroll(-2,mode="relative")
print(cursor.fetchone())
```

### 8.数据表中的数据对应python数据类型

```markdown
int -- int
float/double -- float
varchar/char -- str
datetime -- datetime.datetime(年月日时分秒)
```

### 9.资源回收

```python
cursor.close()  # 先关闭游标
conn.close()  # 在关闭连接对象
```

### 10.sql注入(了解)

所谓的sql注入，就是通过sql命令插入到web表单中提交，或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的sql命令。共计站点，达到入侵目的。

```python
# age="' or '1'='1"
# ' or '1'='1
# sql = "select * from student where name='%s' and age='%s'"%(name,age)
# cursor.execute(sql)
# print(cursor.fetchall())
```

### 11.防止sql注入

```python
# 防止sql注入
cursor = conn.cursor()
# name = 'wangdachui'
# age="' or '1'='1"
name="zhangsan"
age="18"
sql = "select * from student where name=%s and age=%s"
cursor.execute(sql,[name,age])
print(cursor.fetchall())
```

### 12.传递参数

```python
cursor.execute(sql,[name,age])  列表
cursor.execute(sql,(name,age))  元组
cursor.execute(sql,{"name":"zhangsan","age":"18"})
```



