## 一.表连接

1. #### 两张表或多张表联合查询，共同提取数据，最终得到结果。

join方式在两个或多个表查询数据

2. #### 使用

   2.1 连接方式

   - 内连接    inner join 
   - 外连接   
     - 左外连接 left outer join
     - 右外连接 right outer join
   - 自连接 连接的双方是同一张表

内连接：两张表连接或多张表连接

特点： 连接的条件不会显示空数据

语法：

```mysql
select .. from 表1 as 别名 inner join 表2 as 别名 on 别名1.列名 = 别名2.列名
-- on表示连接的条件
SELECT t1.*,t2.title from t_employee as t1 INNER JOIN t_department as t2 on t1.dept_id = t2.id;
内连接的inner可以省略，只写一个join即可
为了方便也是为了防止命名冲突，建议取一个别名。（别名可以不取）
```

内连接：如果是Ajoin了B

左外连接：将上述的inner join 改成 left join即可（outer可省略） ，这种方式叫左外连接。 左表显示全部数据，右表无对应的数据则显示为空。

右外连接：将上述的inner join 改成 right join即可（outer可省略） ，这种方式叫右外连接。 右表显示全部数据，左表无对应的数据则显示为空。

```mysql
-- 查看员工的对应的部门
-- SELECT t_employee.*,t_department.title from t_employee  inner JOIN t_department  on t_employee.dept_id = t_department.id;
-- SELECT t_employee.*,t_department.title from t_employee  left outer JOIN t_department  on t_employee.dept_id = t_department.id;
SELECT t_employee.*,t_department.title from t_employee  right outer JOIN t_department  on t_employee.dept_id = t_department.id;
```

总结：

```markdwon
1. 内连接 只有存在匹配对应的数据才会显示在最终结果中。
2. 外连接 左外连接的左表（主表） ，右外连接的右表（主表） 数据全部显示，如果从表没有对应数据，则显示为null（用null填充）
3. 左右表根据 join的左右关系确定。
```

自连接

```mysql
自己连接自己，多用于类别表中
查询所有的1级分类和他的子分类名称
select t1.title,t2.title from t_cate as t1 join t_cate as t2 on t1.id=t2.parent_id;
```

### 多表连接

员工，部门，地区...

- 查询所有员工的信息及所在部门的信息和部门所在地区的信息

  ```mysql
  SELECT emp.*,dept.*,loc.* 
  from t_employee emp
  left join t_department dept
  on emp.dept_id=dept.id
  left JOIN t_location loc
  on dept.location_id=loc.id
  ```

## 二.建表操作

### 1.数据类型

- 数字类型

|    类型名称     |                 大小                 |   用途    |
| :---------: | :--------------------------------: | :-----: |
|   tinyint   |                1字节                 | 极小的整数值  |
|  smallint   |                2字节                 |  小整数值   |
|  mediumint  |                3字节                 |  中整数值   |
| int/integer |    4字节  -2147483648——2147483647    |  大整数值   |
|   bigint    |                8字节                 |  极大整数值  |
|    float    |            4字节 小数点后最多6位            | 单精度浮点数值 |
|   double    |           8字节 小数点后最多15位            | 双精度浮点数值 |
|   decimal   | 无固定大小 decimal(m,n) m指的是多少位，n小数位多少位 |   小数值   |

- 字符类型

|    类型名称    |       大小       |             用途             |
| :--------: | :------------: | :------------------------: |
|    char    |    0-255字节     | 定长字符串 char(10) 表示固定占用10个字节 |
|  varchar   |   0-65535字节    |  变长字符串varchar(10) 表示最大长度   |
|  tinyblob  |    0-255字节     |      不超过255个字符的二进制字符串      |
|  tinytext  |    0-255字节     |           短文本字符串           |
|    blob    |   0-65535字节    |         二进制的长文本数据          |
|    text    |   0-65535字节    |            文本数据            |
| mediumtext |  0-16777215字节  |         中等长度文本字符串          |
|  longtext  | 0-4294967295字节 |          极大的文本字符串          |

日期和时间类型

|          类型名称           |         格式          |   用途DATE   |
| :---------------------: | :-----------------: | :--------: |
|          DATE           |     YYYY-MM-DD      |     日期     |
|          TIME           |      HH:MM:SS       |     时间     |
|        DATETIME         | YYYY-MM-DD HH:MM:SS |   混合日期时间   |
| TIMESTAMP：取值范围1970-2037 | YYYY-MM-DD HH:MM:SS | 混合日期时间，时间戳 |

### 2.表约束

对表中的列做出修饰。

primary key ： 主键 -- 唯一记录数据表中的一条记录   不能重复+非空

not null ： 非空

null ： 可空

unique： 唯一

### 3.列选项

auto_increment : 自增长。一般用在主键上，默认从1开始

default ：列的默认值,插入数据时候的列的缺省值。

```mysql
create table stu(
	id int auto_increment primary key,
	name varchar(20),
	sex varchar(10) default "女",
	age int default 16
);
```

### 4.表选项

engine   引擎选择 -- 一般就使用innodb

default charset  表中数据的编码格式

```markdown
1. 建库的时候最好选择字符集为utf8  建表的时候会继承库的字符集
2. 如果建库的时候没有选择字符集，则建表的时候必须设置字符集，否则会出现中文乱码。
3. my.ini配置文件里面有设置默认字符集的选项，可以设置为utf-8，数据库就会继承配置中的字符集。
```

auto_increment  自增长的列的起始值

```mysql
create table user(
	id int auto_increment primary key,
	name varchar(20)
)ENgine=INNODB default charset=utf8 auto_increment=2;


create table user(
	id int auto_increment,
	name varchar(20),
	id_card int,
	PRIMARY key(id), -- 表级约束
	UNIQUE(id_card)
)ENgine=INNODB default charset=utf8 auto_increment=2;
```

### 5.联合约束

```mysql
create table t_user2(
	id int auto_increment,
	name varchar(20),
	age tinyint,
	PRIMARY key(id,name),  -- id和name共同作为联合主键
	unique(name,age) -- name和age的组合不能重复
) engine=INNODB default charset=utf8;
```

## 三.操作表里的数据

### 1.插入数据

```mysql
基本格式：
insert into 表名(列名1，列名2,...) values(值1，值2，...);
```

注意：values前后括号里的值 数量要保持一致

- 主键是自动增长的，mysql会自动填充值，不建议为主键指定值

一次插入多条数据

```mysql
insert into t_user2(name) values("wangba"),("liujiu"),("niufen");
```

省略列名插入，一定要保证values中必须是完整的（包括主键）列对应的值

```mysql
insert into t_user2 values(11,"wangba",18);
```

### 2.更新数据

```mysql
语法：
update 表名 set 列名1=值，列名2=值,...
```

注意: 更新数据的时候务必要指定where条件，否则会影响所有行的值

- 更新id为1的用户姓名为文广

```mysql
update t_user set name="wenguang" where id=1;
```

- 更新所有人的性别为未知

```mysql
update t_user set sex="未知"；
```

### 3.删除数据

```mysql
语法：
delete from 表 where...
```

- 删除所有数据

```mysql
delete from t_user2;
```

- 删除年龄大于200岁的用户

```mysql
delete from t_user where age > 200;
```

