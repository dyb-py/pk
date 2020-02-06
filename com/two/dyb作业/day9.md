## 一.关联关系

### 1.概念

在实际工作中。会有很多的数据。表之间不是孤立的，是存在关联关系的。关联关系的搭建是通过 **外键** 完成的

### 2.使用外键

```mysql
foreign key(列名) references 对方表名(对方主键名)
```

```mysql
-- 建立一个 部门表
create table t_department(
	id int auto_increment primary key,
	name varchar(20)
);
-- 建立一个员工表
create table t_employee(
	id int auto_increment primary key,
	name varchar(20),
	dept_id int,
	FOREIGN key(dept_id) REFERENCES t_department(id) -- 添加外键
);
```

1.外键列的类型要和对方主键列的类型保持一致

2.外键列中的值必须是对方主键中的值的子集

3.插入数据的时候要先插入主表

4.删除数据的时候要先删除从表（有外键的一方为从表）

### 3.表和表之间的关系

3.1. 一对多

```
上面的例子就是一对多
```

3.2 一对一

```mysql
-- create table person(
-- 	id int auto_increment primary key,
-- 	name varchar(20),
--  age tinyint
-- );

CREATE table idcard(
	id int auto_increment primary key,
	data1 int,
	person_id int,
	FOREIGN key(person_id) REFERENCES person(id), -- 设置外键
	unique(person_id) -- 设置为唯一
);
```

3.3 多对多

```mysql
-- 学生表
create table student(
 id int auto_increment primary key,
	name varchar(20),
	age int
);
-- 课程表
create table course(
 id int auto_increment primary key,
	title varchar(20),
	hours int
);
 -- 关系表
create table relation(
	student_id int,
	course_id int,
	FOREIGN key(student_id) REFERENCES student(id),
	FOREIGN key(course_id) REFERENCES course(id),
	PRIMARY key(student_id,course_id)
);

```

## 二.事务

### 1.概念：

在一个复杂的业务处理中，会有很复杂的多次操作，这些操作全部都成功了才意味着业务的完成。如果其中的某一步出错，那么整个业务就失败了。

- 需要保证的是一个业务中诸多数据操作一旦有任何一处的出错可以立刻全盘回退，使数据库不会出现非法数据。

```mysql
-- create table account(
-- 	id int auto_increment primary key,
-- 	OWNER varchar(20),
-- 	balance int
-- );
-- 
begin;  -- 开启一个事务
start transation； -- 也是开启事务（不用了）
update account set balance=balance-400 where owner = "zhangsan";
-- 出错的 
UPDATE account set balance=balance2+400 where owner = "lisi";
commit；  -- 提交事务 是由mysql控制的自动回滚

rollback；  -- 由程序员控制的回滚（手动的），不管是否出错，都回滚
```

### 2.事务的特性（ACID）



- atomicity原子性:一个事务是不可分割的工作单位，事务中的操作要么都做，要么都不做。
- consistency一致性：事务的干涉下，数据库总是从一个一致性的状态转换到另一个一致性的状态，数据的逻辑是完整和正确的。
- isolation隔离性：一个事务中的数据，对其他的事务是隔离的【隔离级别】
- durability：持久性：事务一旦提交，处理结束后，事务中的数据就持久化的到数据库中。

### 3.事务的并发问题

- 脏读：事务A读取到了事务B中的数据，但是事务B回滚了或更新了数据，事务A独到的就是脏数据。

- 不可重复读：事务A多次读取同一数据的过程中，事务B更新了此数据并提交了事务，则事务A多次读取到不同的数据。

- 幻影读：事务A多次读取统一张表的数据的过程中，事务B更新了表中的数据（增加或删除）,则事务A发现了莫名其妙的额外的数据。

  - 基于事务隔离级别小于repeatable-read

    ​	数据行数不一致

  - 基于事务隔离级别小于serializable

    ​	一个事务通过一次或多次查询的结构，确定可以添加一个不重复的数据。但是实际上却发现表中已有数据重复（另一个事务已经添加完了。）

- 更新丢失：后面再说。

总结：

脏读和不可重复读的区别：

- 脏读是B事务更新但未提交事务
- 不可重复读是指B事务更新并提交了事务，A读到的不一致

幻影读和脏读和不可重复读的区别

- 幻影读是对数据行的增加或删除
- 脏读和不可重读是对数据内容的修改

### 4.事务隔离级别

| 事务隔离级别                 | 脏读   | 不可重复度 | 幻影读  |
| ---------------------- | ---- | ----- | ---- |
| 读未提交（read-uncommitted） | 是    | 是     | 是    |
| 读提交（read-committed）    | 否    | 是     | 是    |
| 可重复读（repeatable-read）  | 否    | 否     | 是    |
| 串行化（serializable）      | 否    | 否     | 否    |

隔离级别由低到高，安全性逐渐加强，并发性逐渐降低

mysql中默认的隔离级别是repeatable-read

#### 4.1如何查看事务隔离级别

```mysql
select @@tx_isolation;
```

#### 4.2如何设置隔离级别

```mysql
-- 读未提交
set session transaction isolation level read uncommitted;
-- 读提交
set session transaction isolation level read committed;
-- 可重复读
set session transaction isolation level repeatable read;
-- 串行化
set session transaction isolation level serializable;
```

### 5.锁

更新丢失：当两个或多个事务选择同一行数据，然后基于最初选定的值更新该行时，由于每个事务都不知道其它事务的存在，就会发生更新丢失的问题。

在mysql中，增删改语句会自动的对所操作的数据行加锁。如果其他事务也要增删改相同的数据行，会被阻塞。

拥有锁的事务，会在事务结束后，释放锁。

- 悲观锁： select .. from 表名 .. for update;   【行级锁，排它锁】
- 乐观锁 :  在数据列中新增一列 version（初始值0）记录数据更新的版本，不是真正的锁。

```mysql
account   id name balance version(0)
select balance from account where id=1 and version=0;
update account set balance=2002+10,version=0+1 where id=1 and version=0;  -- 事务a做的事

select balance from account where id=1 and version=0;
update account set balance=2002+10,version=0+1 where id=1 and version=0;  -- 事务b做的事，未更新到数据行
```