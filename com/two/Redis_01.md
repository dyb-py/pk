3# Redis数据库

### 一、NoSQL简介

NoSQL，泛指非关系型的数据库，有时也称作Not Only SQL的缩写，是对不同于传统的关系型数据库的的统称。    

- SQL (Structured Query Language) 数据库，指关系型数据库。主要代表：SQL Server，Oracle，MySQL，PostgreSQL。存储数据时，需要预先定义表，字段--关系表
- NoSQL（Not Only SQL）泛指非关系型数据库。主要代表：MongoDB，Redis，CouchDB。无表无关联



**SQL和NoSQL对比：**

- SQL通常以数据库表形式存储数据。举个栗子，存个学生借书数据： 

![img](Redis_01.assets/1744544-a9b6a180eb06a2ba.jpg) 

- 而NoSQL存储方式比较灵活，比如使用类JSON文件存储上表中熊大的借阅数据：

 ![img](Redis_01.assets/1744544-e7d6976369ed43e6.png) 



**关系型数据库瓶颈**

- 高并发读写需求

  针对网站类用户的并发性访问非常高，而一台数据库的最大连接数有限，且硬盘I/O有限，其不能满足很多人同时连接

- 海量数据的高效率读写

  网站每天产生的数据量是巨大的，对于关系型数据库来说，在一张包含海量数据的表中查询，效率是非常低的



### 二、Redis简介

#### 1、Redis是什么？

  速度非常快的Nosql数据库，基于key-value的内存存储，同时支持数据持久化到硬盘。



#### 2、Redis的特点

- 高性能
- 数据类型丰富 
- 基于内存存储，又支持持久化（将内存中的数据保存到硬盘中）       



### 三、Redis安装 

#### 1、解压

将redis的tar包发送到Linux中，并解压： `tar -zxvf redis-3.0.7.tar.gz `

#### 2、make指令

`cd`指令切换到解压目录中，然后执行指令:` make`

- 执行make的时候，如出现异常：
  - 异常一：

    `make[2]: cc: Command not found`

    异常原因：没有安装gcc

    解决方案：yum install gcc

  - 异常二：

    `zmalloc.h:51:31: error: jemalloc/jemalloc.h: No such file or directory`

    异常原因：一些编译依赖或原来编译遗留出现的问题

    解决方案：make distclean。清理一下，然后再make。

#### 3、make test

在make成功以后，执行指令：`make test`

- 在make test时出现异常：
  - 异常一：

    `couldn't execute "tclsh8.5": no such file or directory`

    异常原因：没有安装tcl

    解决方案：yum install -y tcl。

#### 4、make install

安装，执行指令：`make install`



#### 5、启动服务 

- 第一种：前台模式，默认配置启动(默认端口6379) 

  `直接执行指令：redis-server`

- 第二种：守护进程(后台)模式,指定配置文件启动 

  - 在redis解压根目录中找到配置文件模板(redis.conf)，复制到如下位置：

    ```
    cp redis.conf /usr/local/redis_conf/redis.conf
    ```

  - 通过vi命令修改

    ```
    daemonize yes   #守护进程模式启动 -- 后台

    port 7000       #端口  也可以不改

    pidfile ./redis.pid  #进程id存储位置

    logfile ./redis.log   #日志文件存储位置

    dir /usr/local/redis_conf/                 #工作目录 rdb、aof文件存储位置
    ```

  - 然后执行` redis-server redis.conf`

#### 6、连接Redis

执行指令：

- `redis-cli ` 连接端口为6379 Host为127.0.0.1的redis服务器

- `redis-cli -p 7000 -h 192.168.1.103` 连接端口为7000 Host为192.168.1.103的redis服务器



#### 7、关闭服务

redis-cli连接了redis服务器后，可以通过` shutdown `  指令关闭连接，并关闭服务

如果只想关闭连接（客户端），在redis命令中，按`Ctrl+c` 即可，此时服务不会被关闭

如果继续想要关闭服务，可在命令行中执行 `redis-cli -p 7000 shutdown`





### 四、Redis数据类型 

Redis支持五种数据类型：string（字符串），list（列表），set（集合）及zset(sorted set：有序集合)，hash（哈希）。 

#### 1、String字符串  

用于存单值，常用指令：

| 命令          | 说明                            | 示例                                 |
| ----------- | ----------------------------- | ---------------------------------- |
| set         | 设置一个key/value                 | set name houqn                     |
| get         | 根据key获得对应的value               | get name       (keys *  / keys n*) |
| mset        | 一次设置多个key value               | mset age 18 salary 3000            |
| mget        | 一次获得多个key的value               | mget name age                      |
| getset      | 获得原始key的值，同时设置新值              | getset age 20                      |
| del         | 删除key-value (可以同时多个)          | del name                           |
| strlen      | 获得对应key存储value的长度             | strlen name                        |
| append      | 为对应key的value追加内容              | appdend name 123                   |
| getrange    | 截取value的内容,对原始的值没有影响          | getrange name  0 2                 |
| setex       | 设置一个key存活的有效期（秒）              | setex name 10 tom (ttl key查看剩余时长)  |
| psetex      | 设置一个key存活的有效期（毫秒）             | psetex course10000 redis           |
| setnx       | 只有当这个key不存在时等效set操作 not exist | sexnx birth 2020-2-2               |
| msetnx      | 可以同时设置多个key，在key不存在时有效        | msetnx  course mysql duration 4    |
| decr        | 进行数值类型的-1操作                   | decr age                           |
| decrby      | 根据提供的数据进行减法操作                 | decrby age 3                       |
| incr        | 进行数值类型的+1操作                   | incr age                           |
| incrby      | 根据提供的数据进行加法操作                 | incrby age 3                       |
| incrbyfloat | 根据提供的数据加入浮点数                  | incrbyfloat age 3.5                |

注：查看所有键值对 keys *  keys *a

#### 2、List列表

存储多值，常用指令：

| 命令      | 说明                     | 示例                                     |
| ------- | ---------------------- | -------------------------------------- |
| lpush   | 将某个值加入到一个key列表头部       | lpush users tom                        |
| lpushx  | 同lpush,但是必须要保证这个key存在  | lpushx users jack                      |
| rpush   | 将某个值加入到一个key列表末尾       | rpush users linda                      |
| rpushx  | 同rpush,但是必须要保证这个key存在  | rpushx users james                     |
| lpop    | 返回和移除列表的第一个元素          | lpop users                             |
| rpop    | 返回和移除列表的最后一个元素         | rpop users                             |
| lrange  | 获取某一个下标区间内的元素          | lrange users 0 3   / lrange users 0 -1 |
| llen    | 获取列表元素个数               | llen users                             |
| lset    | 设置某一个位置的元素(替换已有的某个值)   | lset users 2 andy                      |
| lindex  | 获取某一个位置的元素             | lindex users 2                         |
| lrem    | 从列表头起，删除对应个数的指定元素      | lrem users 2 james                     |
| ltrim   | 保留列表中特定区间内的元素,将其它的元素删除 | ltrim users 1 3                        |
| linsert | 在某一个元素之前，之后插入新元素       | linsert users before/after jack lilei  |



#### 3、Set集合

set是无序集合，并且不允许有相同的元素

常用指令：

| 命令          | 说明                 | 示例                |
| ----------- | ------------------ | ----------------- |
| sadd        | 为集合添加元素            | sadd st tom       |
| smembers    | 显示集合中所有元素   无序     | smembers st       |
| scard       | 返回集合中元素的个数         | scard st          |
| spop        | 随机返回并移除一个元素        | spop st           |
| smove       | 从一个集合中向另一个集合移动元素   | smove st1 st2 tom |
| srem        | 从集合中删除一个元素         | srem st tom       |
| sismember   | 判断一个集合中是否含有这个元素    | sismember st tom  |
| srandmember | 随机返回元素，对原始数据没有影响   | srandmember st    |
| sdiff       | 减去两个集合中共有的元素   求差集 | sdiff st1 st2     |
| sinter      | 求交集                | sinter st1 st2    |
| sunion      | 求并集                | sunion st1 st2    |



#### 4、Zset有序集合 

常用指令：

| 命令            | 说明                      | 示例                             |
| ------------- | ----------------------- | ------------------------------ |
| zadd          | 添加一个有序集合元素，根据元素的score排序 | zadd salary 3000 tom 2000 jack |
| zcard         | 返回集合的元素个数               | zcard salary                   |
| zrange        | 返回一个范围内的元素              | zrange salary  1 2 withscores  |
| zrangebyscore | 按照分数查找一个范围内的元素          | zrangebyscore salary 1000 2000 |
| zrank         | 返回对应元素的排名               | zrank salary tom               |
| zrevrank      | 返回对应元素倒序排名              | zrevrank salary tom            |
| zscore        | 显示某一个元素的分数              | zscore salary tom              |
| zrem          | 移除某一个元素                 | zrem salary tom                |
| zincrby       | 给某个特定元素加分               | zincrby salary  100 tom        |



#### 5、Hash哈希 

常用指令：

| 命令           | 说明              | 示例                               |
| ------------ | --------------- | -------------------------------- |
| hset         | 设置一个key/value对  | hset user name tom               |
| hget         | 获得一个key对应的value | hget user name                   |
| hgetall      | 获得所有的key/value对 | hgetall user                     |
| hdel         | 删除某一个key/value对 | hdel user name                   |
| hexists      | 判断一个key是否存在     | hexists user name                |
| hkeys        | 获得所有的key        | hkeys user                       |
| hvals        | 获得所有的value      | hvals user                       |
| hmset        | 设置多个key/value   | hmset  user name tom gender true |
| hmget        | 获得多个key的value   | hmget user name age              |
| hsetnx       | 设置一个不存在的key的值   | hsetnx user salary 4000          |
| hincrby      | 为value进行加法运算    | hincrby user age 3               |
| hincrbyfloat | 为value加入浮点值     | hincrbyfloat user age 3.5        |



### 五、Redis持久化

#### 1、什么是持久化？

持久化的含义就是把内存中的数据保存到可永久存储的设备中（磁盘中），以便数据可以重用。   

- 存：读内存中Redis数据 -> 通过持某种久化的方式 -> 存储到磁盘的文件中      `内存->文件`
- 取：读磁盘文件中的数据 -> 内存中                                                                        `文件->内存`

众所周知，redis是内存数据库，它把数据存储在内存中，这样在加快读取速度的同时也对数据安全性产生了新的问题，即当redis所在服务器发生宕机后（或服务器进程退出 ），redis数据库里的所有数据将会全部丢失。

为了解决这个问题，redis提供了持久化功能：

- **RDB持久化**（snapshotting快照 - 原理是将Redis在内存中的数据库记录定时dump到磁盘上的RDB持久化） 
- **AOF持久化**（append only file - 原理是将Redis的操作日志以追加的方式写入文件）。  


通俗的讲就是将内存中的数据写入硬盘中，当redis重启后，可以从磁盘中恢复数据。    



#### 2、RDB持久化

##### 2.1 RDB开发步骤

编辑redis.conf文件：

```
save   900   1           #900秒内超过1个key被修改 
save   300   10          #300秒内超过10个key被修改
save   60    10000
dbfilename dump.rdb      #快照文件名
stop-writes-on-bgsave-error yes   #快照失败后是否继续写操作
rdbcompression yes                #是否压缩快照文件   
```



##### 2.2 RDB运行原理

- 在某些时刻（满足rdb持久化的时刻），Redis通过fork产生子进程，一个父进程的快照(副本)， 其中有和父进程当前时刻相同的数据
- 父进程继续处理client请求，子进程负责将快照(数据副本)写入临时文件(默认文件名为dump.rdb)
- 子进程写完后，用临时文件替换原来的快照文件，然后子进程退出。        

![img](Redis-pic\388326-20170726161552843-904424952.png) 

##### 2.3 RDB触发方式

- 根据配置  save 900 1 等，在满足条件时自动触发

- 手动执行  bgsave 指令触发 在后台保存

- 手动执行 save指令触发，但会造成持久化过程中的主进程阻塞。在主进程阻塞期间，服务器不能处理客户端的任何请求。 （不常用）

  如果数据量很大时可以考虑使用，因为不用创建子进程，也就没有子进程抢资源，所以save在生成快照时可以更快(夜深人静时手动触发)

- 当通过 shutdown 关闭redis时，会自动触发



##### 2.4 RDB注意事项

- 如果发生系统崩溃，则会丢失最近一次rdb之后的数据，所以如果项目不能接受这样的数据损失，则不建议使用rdb
- 如果数据量巨大，则创建子进程的时间长，导致redis卡顿，要谨慎设置save参数时间间隔大一些；或如果软件允许，可以每天在闲时手动同步
- 将生成的快照文件，留在原地，则可以在重启redis后，恢复数据状态
- 将生成的快照文件，复制到其它redis服务中，可以方便的将数据移植过去



#### 3、AOF持久化

Append-Only File（AOF）：与RDB的保存整个redis数据库状态不同，AOF是通过保存对redis服务端的写命令（如set、sadd、rpush）来记录数据库状态的，即保存你对redis数据库的写操作记录。  



##### 3.1 AOF运行机制

Redis将每一个写操作(执行成功)，写入aof文件，即记录所有的数据改动行为，Redis重启时只要从头到尾执行一次aof文件，即可恢复数据，也可以将aof文件复制到别的服务器，做数据移植。

**注意：**在重启时，要恢复数据，如果rdb文件和aof文件同时存在，以AOF为准。



##### 3.2 AOF配置

编辑redis.conf文件：

```
appendonly  yes           #启动AOF机制

# appendfsync always       #每次收到写命令就立即强制写入磁盘，保证完全的持久化，但产生极大的IO开销(不推荐使用)  

appendfsync everysec      #每秒钟强制写入磁盘一次，在性能和持久化方面做了很好的折中(推荐使用）

# appendfsync no            #完全依赖os，虽然基本不对redis性能产生影响，但操作系统的缓存区满时，会阻塞redis(不推荐使用)

appendfilename "appendonly.aof"    # 设置aof文件名     
```



##### 3.3 AOF细节

- AOF文件会不断增长(可能比快照文件大几倍)，在极端情况下，可能会对硬盘空间造成压力
- Redis重启时，需要重新执行一个可能非常大的AOF，时间会很长
- AOF同步时间间隔小，数据更安全，理论上至多丢失1秒的数据

**注意：**

- 如果当前数据量巨大，则子进程创建过程会很耗时

- 在替换aof文件时，如果旧aof很大，则删除它也是一个耗时的过程




#### 4、AOF重写

##### 4.1 重写设置

AOF采用文件追加的方式持久化数据，所以文件会越来越大，为了避免这种情况发生，增加了重写机制。

- 为了减小aof文件的体量，可以手动发送 bgrewriteaof 命令，则会创建子进程，通过移除aof文件中的冗余命令来重写aof文件，生成更小体量的aof，然后替换掉旧的、大体量的aof文件
- 也可以设置：`auto-aof-rewrite-percentage 100`

​                               `auto-aof-rewrite-min-size 64mb`

   在体量超过64mb，且比上次重写后的体量增加了100%时自动触发重写



##### 4.2 重写原理

Redis将AOF重写程序放到子进程（后台）里执行。这样处理的最大好处是： 

- 子进程进行AOF重写期间，主进程可以继续处理命令请求；
- **子进程带有主进程的数据副本**，使用子进程而不是线程，**保证数据的安全性**。



子进程进行AOF重写的问题：

- 子进程在进行AOF重写期间，服务器主进程还要继续处理命令请求，而新的命令可能对现有的数据进行修改，这会让当前数据库的数据和重写后的AOF文件中的数据不一致。

解决方案：

- 为了解决这种数据不一致的问题，Redis增加了一个AOF重写缓存，这个缓存在fork出子进程之后开始启用，Redis服务器主进程在执行完写命令之后，会同时将这个写命令追加到AOF文件和AOF重写缓冲区

即子进程在执行AOF重写时，主进程需要执行以下三个工作： 

- 执行client发来的命令请求；
- 将写命令追加到现有的AOF文件中；
- 将写命令追加到AOF重写缓存中。

#### 5、RDB与AOF对比

- RDB体量更小，AOF文件体量更大
- RDB的同步时间间隔大，AOF同步时间间隔小，所以AOF更能保证数据的安全 
- RDB有更快的恢复速度，可以用来做数据版本控制。RDB每次进行快照方式会重新记录整个数据集的所有信息。RDB在恢复数据时更快，可以最大化redis性能。
- 通过使用RDB和AOF，用户可以在重启或系统崩溃后保留数据，但随着负载量变大和数据安全越来越重要，可以使用redis的复制特性做更好的数据安全保障

RDB可以做数据备份，并且要求数据恢复快，对数据一致性要求不高时



### 六、Redis主从 

#### 1、 简介

在高负载和对数据要求高完整性时，数据的复制是不可或缺的。一个Redis主服务器，并为其关联多个从服务器，主服务器会将自己的数据状态不断的同步给从服务器，即，从服务器中会持有主服务器最新的数据副本，则首先为数据完整性提供了进一步的保证，而且所有读取操作都可均衡的负载到多个从服务器中，主服务器主要负责写操作。则主从多个服务器实现读写分离，提供更好的数据完整性，和更强的负载能力。 



#### 2、主从配置

开启两个redis服务器，一个做主服务器，另一个做从服务器。主从两台服务器的配置没有额外的改变，只是**在从服务器的配置中添加一句配置**：

```
replicaof  host  port  比如：slaveof 192.168.1.103 7000

则如上配置将当前的redis服务器设置为(192.168.1.103:7000)的从服务器
# 注意 需要在主服务器中 设置bind 0.0.0.0
```

- 如此，则主服务器的所有数据会在初始接收到从服务器的连接时全部发送到从服务器。之后每次主服务器执行完一个写操作，都会发送到从服务器。如上则是主从的运行模式。

- 可以向如上设置多台从服务器，则以后的所有读取操作由从服务器完成，主服务器只负责写操作。