### mysql

一.简介

mysql是一个关系型数据库管理系统。

mysql的结构：

```python
库，表，行，列 组成的。
	每个库中有多个表，每个表中有多个行，每行有多个列
```

mysql将数据存放在不同的表中，而不是将所有的数据都放在一个大仓库里。

可以实现速度的提升和提高灵活度。

### 安装mysql

```markdown
1.下载安装包
	mysql 官网下载。
2.安装
	安装过程中需要注意：
		1.自定义安装位置
		2.配置环境变量
		3.输入密码
测试是否安装成功（查看版本号）：
	mysqladmin --version  
进入mysql：
	mysql -u用户名 -p密码
退出mysql：
	quit;
修改密码：
	mysqladmin -u用户名 -p旧密码 password 新密码
忘记了密码怎么办？
	1.关闭正在运行的MySQL服务
	2.进入mysql的bin目录下 （如果已配置环境变量，可以无视）
	3.输入命令：mysqld --skip-grant-tables 然后回车。这个命令的意思就是启动mysql服务的时候跳过权限表认证
	4.再打开一个DOS窗口，直接输入mysql进入数据库。
	5.连接权限数据库 ： use mysql;
	6.改密码：update user set password=password("新密码") where user="root";
	7.刷新权限命令： flush privileges;
	8.退出mysql
```

### 数据库管理

1.显示所有数据库

```mysql
show databases;
```

2.创建一个新的数据库

```mysql
create database 数据库名 charset=utf8;  # 万国码 解决中文乱码问题
```

3.删除数据库

```mysql
drop database 数据库名;
```

4.选择库、查看当前选中库

```mysql
use 数据库名;                  使用某个数据库
select database();            查看当前选中的数据库
```

5.查看数据库中的表

```mysql
show tables;
```

### 简单的建表操作

1.创建表

```mysql
create table 表名(列名 数据类型 约束 , 列名2)
create table stu(id int primary key auto_increment ,name varchar(20), sex varchar(3));
```

2.简单的数据类型

```mysql
1.int/integer 整数
2.varchar(n) 字符，n是字符的长度
3.datatime 日期
```

3.简单的约束

```mysql
1.auto_increment     自增   由mysql自动维护的，默认从1开始
2.primary key   主键   唯一的标识数据表中每天记录   不重复且非空
3.not null    非空
4.unique     唯一 但可以为空
```

4.查看表结构

```mysql
desc 表名
```

- 插入数据

  ```mysql
  insert into 表名(列名1，列名2,...) values(值1，值2,...)；
  ```

- 查看数据

  ```
  select * from 表名    
  ```

- 查看指定的部分列

  ```mysql
  select 列名1，列名2,...from 表名;
  ```

  ​









