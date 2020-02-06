### 1.查询语句(sql)

结构化查询语言

## 一. 列查询

1.查询所有的列

```mysql
select * from 表名
```

2.查询指定列

```MYSQL
select 列名,列名,...from 表名
```

### 二.列操作

- 列运算： 列查询支持算术运算【+ - * /】，在运算中如果出现null ，结果还是null

  ```mysql
  select id+1,age*2 from userlist;
  ```

- 列拼接

  ```mysql
  SELECT CONCAT(age,"岁") from userlist;
  ```

- 列别名

  ```mysql
  select age as "年龄",birthday as "生日" from userlist;
  ```

  注意：as可省略（前期不要省）

- 列去重（了解）

  ```mysql
  select DISTINCT age from userlist;
  ```

### 三.where语句

#### 3.1 条件查询

如果需要获取满足一定条件的数据，可以使用where语句

基本语法:

```msyql
select ... from 表名 where 条件表达式
```

比较运算符：【=   !=    >   <   >=   <=    <>】

- 找出所有年龄不是18的人的全部信息

  ```mysql
  SELECT * from userlist WHERE age != 18;
  ```

逻辑运算符： 【and    or】

- 查询所有年龄大于18岁，且id大于2的人的所有信息

  ```mysql
  select * from userlist where age>18 and id>2;
  ```

- 查询id小于3 且年龄小于19 或名字是“zhangsan” 的用户的 id，name，age

  ```mysql
  select id,name,age from userlist where id < 3 and age<19 or name="zhang3";
  ```

范围区间：  between...and   in(xxx,xxx)/not in

- 查询年龄大于18岁，并且id在（1，3，4）其中之一的用户的id，name和age

  ```mysql
  select id,name,age from userlist where age>18 and id in(1,3,4);
  ```

- 查询年龄大于18岁，并且id在2-4之间的用户

  ```mysql
  select id,name,age from userlist where age > 18 and id between 2 and 4;
  ```

#### 3.2 空值的判断

格式：

```mysql
select ... from 表名 where 列名 is null 
```

- 查找name不为空，birthday为空的name

  ```mysql
  select name from userlist where name is not null and birthday is null;
  ```

  注意：检测是否为空不能使用=号来检测。

#### 3.3 模糊查询

- % 任意的多个字符
- _  一个字符

语法：

```mysql
select ... from 表 where 列名 like "%内容%"
like "%广哥%" 所有含有广哥的 信息
SELECT * from userlist where name like "%广哥%";

like "%广%哥%" 所有含有广和哥的 信息
SELECT * from userlist where name like "%广%哥%";

like "%广哥"  以广哥结尾
SELECT * from userlist where name like "%广哥";

like "广哥%"  以广哥开头
SELECT * from userlist where name like "广哥%";

like "广哥%_" 以广哥开头，并且广哥后面至少有一个字符
SELECT * from userlist where name like "广哥%_";

like "%__%"  至少两个字符  
	length(列名) >= 2
not like   和 like取反
```

### 四. 分页查询

limit 分页查询关键字

```mysql
从第一条数据开始，共查询3条数据
SELECT * from userlist LIMIT 0,3;

从第一条数据开始，共查询两条
SELECT * from userlist LIMIT 0,2;

从第3条数据开始，共查询3条
select * from userlist limit 2,4;
注意：如果数据量不够，则只显示已有的数据

每页显示3条数据，查询第3页
select * from userlist limit 6,3
公式： select 。。 from 表 limit (m-1)*n,n
n 是指的是每页显示多少条。m指多少页
```

### 五. order by 子句： 排序方式

```mysql
1. asc 升序排序（默认）
2. desc 降序排序
语法：
select 。。。 from 表名 order by 别名 asc/desc
```

- 所有人员的信息根据id来降序排序

  ```mysql
  SELECT * from userlist order by id desc;
  ```

- 根据age来升序排序，age相同的按照薪水升序排序

  ```mysql
  select * from userlist order by age asc,salary asc;
    在得到年龄排序的基础上再按照薪水排序
  ```

### 六.聚合函数：组函数

max() 最大值

min() 最小值

sum() 求和

avg()  平均值

count() 总共出现的次数

```mysql
查询最大的id和年龄的平均值
SELECT max(id),avg(age) from userlist;

查询共有多少条数据   注意不要使用max来查询，因为可能出现脏读
SELECT count(id) from userlist;

查询年龄的总和，和平均年龄
SELECT sum(age),avg(age) from userlist;

查询最大的年龄的名字
-- 这样的方式是不可以的，一条sql语句不能处理两条逻辑（可以查，但需要两条sql语句）
SELECT max(age),name from userlist; 

-- 这样的方式会报错，因为 = 后面必须跟的是确定的值  比如 = 10
   无论是什么比较运算符，后面跟的必然是一个确定的值
SELECT name from userlist where age=max(age);
```

### 七. group by : 分组统计

语法：

```mysql
select ... from 表名 (where ...)group by 列名;
```

```mysql
查询每个部门的最高工资，最低工资，最大年龄，部门id
SELECT max(salary),min(salary),max(age),dept_id from t_employee GROUP BY dept_id;
-- 分组查询的时候，查询的结果可以是组函数和分组条件的列

查询每个部门的平均工资，最低工资，工资总和，部门id
SELECT avg(salary),min(salary),sum(salary),dept_id from t_employee GROUP BY dept_id;

-- 查询年龄相同人的最高工资
SELECT max(salary) from t_employee group by age;

-- 查询每个部门的员工总数，部门id
select count(id),dept_id from t_employee group by dept_id;

聚合统计：将部门id和年龄都相同的分到一组（了解即可）
SELECT age,dept_id,name from t_employee GROUP BY dept_id,age;
注意： 分组查询，结果就是组中的一条数据
```

### having子句:分组限制

语法：

```mysql
select .. from 表名 group by 列名 having...；   有一个限制条件，对分组之后的数据的限制
```

例子

```mysql
-- 查询平均工资大于10000的部门的员工的平均年龄和最高工资
select avg(age),max(salary),dept_id from t_employee group by dept_id having avg(salary)>10000;

-- 查询最小年龄小于20的部门员工总数和部门id
select count(id),dept_id, from t_employee group by dept_id HAVING min(age) < 20;
```

注意：

```markdown
1. having的作用时刻在group之后执行的，对分组过程中的临时表做筛选，每个临时表筛选一次。
2. where也是做筛选，是对总表数据做筛选
如果有一个需求，where和having都能查的话，建议使用where，效率更高。
查询 部门id小于2的部门员工总数和部门id
select count(id),dept_id from t_employee where dept_id < 2 group by dept_id ;
3. 摆放顺序问题： where 在分组之前，having在分组之后
```

### 九.case子句

当...就...否则...

```mysql
语法：
select 
	列名1，列名2,...
 	case
 		when 布尔表达式 then 结果1
 		when 布尔表达式 then 结果2
 		...
 		else
 			默认结果
 	end
 from 表...
 
-- 例子
SELECT name,age,
CASE
	when age < 20 then "青少年"
	when age >=20 and age < 40 then "中年"
	else "老年"
end as "年龄段"
from t_employee ORDER BY age;

-- 例子2
SELECT 
CASE
	when age < 20 then "青少年"
	when age >=20 and age < 40 then "中年"
	else "老年"
end as "年龄段"
,name,age
from t_employee ORDER BY age;
```

### 十.子查询

将一个查询的结果作为另一个查询的一部分，称之为子查询

- 查询年龄最大的员工的姓名和工资

  ```mysql
  SELECT name,salary from t_employee where age=(select max(age) from t_employee);
  ```

- 查询工资大于平均工资的员工信息

  ```mysql
  SELECT * from t_employee where salary>(SELECT avg(salary) from t_employee);
  ```

- 查询工资小于平均工资的员工数量

  ```mysql
  SELECT count(id) from t_employee where salary < (select avg(salary) from t_employee);
  ```

- 查询平均工资大于10000的部门的员工信息

  ```mysql
  SELECT * from t_employee WHERE dept_id  in(select dept_id from t_employee group by dept_id HAVING avg(salary) > 10000);
  ```

  子查询执行效率很低

补充知识：

```mysql
1.length()  获取长度  select * from t_employee where length(name)>2;
2.lcase() 转为小写字符 SELECT lcase(name) from t_employee;
3.ucase() 转为大写字符 SELECT ucase(name) from t_employee;
4.trim() 去掉首尾空格 select trim(name) from t_employee;
5.now() 当前日期和时间 insert into userlist(name,birthday)values("xiaoming",now());
6.curdate() 当前日期 select curdate()
7.curtime() 当前时间  select curtime()
8.date_format()  日期格式化('%Y%m%d %H:%i:%S')
9.database() 当前数据库名称
10.user() 当前用户名
11.version() 当前服务器版本

```

