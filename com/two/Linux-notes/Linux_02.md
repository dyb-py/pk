# Django环境部署

### 一、MySQL5.7安装 

#### 1、安装方式

##### 1.1 方式一 yum安装（推荐使用该方式）

在CentOS中默认安装有MariaDB，这个是MySQL的分支

如果必须要安装MySQL，首先必须添加mysql社区repo通过输入命令：

`rpm -ivh http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm`

或先下载好mysql57-community-release-el7-10.noarch.rpm，再通过指令 `rpm ivh 文件`进行安装

’然后再`yum install -y mysql-server`  # yum安装，需要外网环境      

##### 1.2 方式二 rpm安装（不建议） 

- `rpm -ivh perl-*.rpm`  #安装所有perl依赖  
- `rpm -Uvh mysql-libs-5.1.73-7.el6.i686.rpm`  #更新mysql的类库
- `rpm -ivh mysql-5.1.73-7.el6.i686.rpm  mysql-server-5.1.73-7.el6.i686.rpm ` #安装mysql主服务



#### 2、启动MySQL服务

` systemctl start/stop/restart/status mysqld`

查看MySQL运行状态：

`systemctl status mysqld.service `

#### 3、使用MySQL

**注意：以下方式针对mysql5.7**

初次使用，需要找到root的密码：

`grep "password" /var/log/mysqld.log`

找到密码后，连接数据库  `mysql -uroot -p密码`

输入初始密码，此时不能做任何事情，因为MySQL默认必须修改密码之后才能操作数据库： 

`ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';`

```
遇到错误：
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements  
解决方案：
1、首先需要设置密码的验证强度等级，设置 validate_password_policy 的全局参数为 LOW 即可，
输入设值语句 “ set global validate_password_policy=LOW; ” 进行设值
2、当前密码长度为 8 ，如果不介意的话就不用修改了，按照通用的来讲，设置为 6 位的密码，设置 validate_password_length 的全局参数为 6 即可，
输入设值语句 “ set global validate_password_length=6; ” 进行设值
3、再重置密码
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';
4、查看 mysql 初始的密码策略，
输入语句 “ SHOW VARIABLES LIKE 'validate_password%'; ” 进行查看
```

**注意：如果是MySQL5.6版，则初始密码为空，直接在命令行中输入 `mysql -uroot `即可进入**

此时进入mysql库中的user表，输入`select host,user,authentication_string from user;`查看表中的数据，发现密码为空。

更新密码即可：`set password for root@localhost=password('123456')`

再刷新权限：`flush privileges;`



- 选择数据库`use mysql`
- 选择表
- 查询表



#### 4、MySQL远程连接

- 到mysql库的user表中
- desc user; 查看表结构中 查看 host,user,authentication_string 查看用户账户信息
- `update user set host='%' where user='root';` #添加可以远程访问的账号 **MySQL5.7版本**
- `update user set host='%',password=password('123456') where host='127.0.0.1';` **MySQL5.6版本**
- `flush privileges;` #刷新权限，保证新添加的账号可用
- 关闭linux的防火墙，保证3306可以访问



**注意：防止mysql本地客户端数据乱码**

```
/etc/my.cnf 中添加如下配置，即可
[client]
default-character-set=utf8

注意：同时注意查看 客户端 自身 编码设置，如果有需要 同样修改为 utf8
```

  

#### 5、MySQL卸载

- `rpm -e mysql-server需要完整的包名 通过rpm -qa | grep mysql查找包名` #只需卸载主服务即可                 
- `rm  -rf  /var/lib/mysql` #删除所有mysql的数据



#### 6、MySQL root密码找回（重置）

找到`/etc/my.cnf`

```
[mysqld]
...
skip-grant-tables   //注意，建议在拆除网线的情况下添加  (而且添加配置后，需要重启mysqld服务)
```

```
[root@Server ~] mysql -uroot
mysql> use mysql;
mysql> update user set password=password('123') where host='root'; //5.6修改密码
mysql> update user set authentication_string=password('123') where host='root'; //5.7修改密码
mysql> flush privileges;
```

然后将如上配置删除或注释



### 二、Python安装

#### 1、安装依赖

- yum -y install  python-devel  openssl-devel  bzip2-devel  zlib-devel  expat-devel ncurses-devel sqlite-devel gdbm-devel xz-devel tk-devel readline-devel  gcc 
- yum -y groupinstall "Development tools"

如上两步，汇总安装了python生产环境的各种第三方依赖包



#### 2、安装Python 

- 将python的tar包发送给linux (建议位置：/usr/local/)

- 解压tar包:`tar -zxvf Python-3.5.2.tgz` 

- cd到解压目录中配置：`./configure --prefix=/usr/local/Python3 --enable-optimizations` 

  目的：检测环境中依赖是否完整，设置python的安装位置，
  同时生成一个编译文件，用于进行python编译：make

- 在解压目录中：先 `make` 编译  然后  `make  install` 安装

```shell
安装后的日志如下
....
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-8.1.1 setuptools-20.10.1
```



- 将python3 设置为系统默认python解释器

  - 将/usr/bin下的`python`文件改名   `mv /usr/bin/python /usr/bin/python2.7.5`

  - 将python3的执行文件链接到  /usr/bin/python  快捷方式

    `ln -s /usr/local/Python3/bin/python3 /usr/bin/python`

* echo $PATH 查看linux下的环境变量



- 设置环境变量：/etc/profile中添加配置  

```
以保证 Python3目录下的 所有的指令可以快捷使用
在文件末尾追加，不要改动文件的其他内容！！！！！！！
export python_home=/usr/local/Python3
export PATH=$PATH:$python_home/bin
```

**注意，设置好后，为了让环境变量生效：**`source /etc/profile`，然后 `python`即可进入python3的环境

**注意，此时系统自带的python2 依然是默认python解释器**

- 更新pip
  - `pip3 install --upgrade pip`

**补充：**

- 如果安装的是mysql5.6及以下版本，需要安装`yum install mysql-devel`

- 由于`yum`用python2编译执行，所以需要单独为`yum`设置为python2，找到`/usr/bin/yum`文件，修改文件头：`#!/usr/bin/python2.7.5`




### 三、Django安装

- 安装数据库驱动：`pip install mysqlclient`

- `pip install django=="2.0.6"`


- 测试使用：
  - `django-admin startproject testproj`  在当前目录下创建一个project:"testproj"

  - cd到testproj目录下的testporj目录下settings.py 修改配置：`ALLOWED_HOSTS = ["*"]`

  - 启动django内置的web服务器。cd到testproj目录下，执行：`python manage.py runserver 0.0.0.0:port`

  - 在Windows的浏览器中访问：`ip:port` -- ip为Linux系统的ip地址


### 四、uWSGI服务器

#### 1、WSGI协议

- 使用Django或Flask框架编写的Web应用程序，在`python manage.py runserver`  时都启动的是框架内置的服务器来运行Web应用程序，而内置的服务器遵循了WSGI协议（WSGI Server）。

- WSGI：全称是`Web Server Gateway Interface`，WSGI不是服务器，python模块，框架，API或者任何软件，只是一种规范，描述web server如何与web application通信的规范。

  - `WSGI server`负责从客户端接收请求，将`request`转发给`application`，将`application`返回的`response`返回给客户端；

  - `WSGI application`接收由`server`转发的`request`，处理请求，并将处理结果返回给`server`。

    ![wsgi.png-22.9kB](Linux_pic\wsgi.png)  

- 要实现WSGI协议，必须同时实现web server和web application，当前运行在`WSGI`协议之上的`web`框架有`Bottle`, `Flask`, `Django`。 

**总结：**WSGI是Web 服务器(uWSGI)与 Web 应用程序或应用框架(Django)之间的一种低级别的接口。 



#### 2、uWSGI服务器安装 

WSGI协议下web服务器很多：django内置，uWSGI，gunicorn。

`uWSGI`服务器自己实现了基于`wsgi`协议的`server`部分，我们只需要在`uwsgi`的配置文件中指定`application`的地址，`uWSGI`就能直接和应用框架中的`WSGI application`通信。 

##### 2.1 服务器安装

- 将uWSGI的tar包发送linux 建议位置 `/usr/local/`

- 解压tar：`tar -zxvf  uwsgi-2.0.17.tar.gz`

- cd到解压目录下，编译：`make`

- 为了可以更方便的执行  uwsgi   启动uWSGI服务器，定制链接：

  `ln -s /usr/local/uwsgi-2.0.17/uwsgi /usr/bin/uwsgi`

  则可以在任意目录下执行 `uwsgi` 去启动uWSGI服务器

- 测试使用python的wsgi服务器-uWSGI

  - 在任意的一个目录中定义一个python脚本：hello.py

    ```python
    def application(env, start_response):
        start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
        return [bytes('你好啊！！','utf-8'),b'houqn']    # 基于wsgi协议规范实现的代码
    ```

  - 启动uWSGI服务器，并部署hello.py程序

    `uwsgi --http 192.168.248.128:8001 --wsgi-file hello.py`   **#注意hello.py可以写成绝对路径**

  - 浏览器访问：`192.168.248.128:8001`

  - control +C 停止服务

#### 3、 uWSGI部署django项目

- **设置mysql的引擎默认为：innodb**

  在`/etc/my.cnf`的`[mysqld]`中添加配置：`default-storage-engine=InnoDB`

- **建议设置为严格模式:**     

  在`/etc/my.cnf`的`[mysqld]`中添加配置 :  `sql_mode=STRICT_TRANS_TABLES`

  - `mysql> show variables where variable_name like '%mode%';#可以查看mysql的配置参数`

  修改完配置后，要重启Mysql的服务

- **在数据库中建好项目需要的database：“ems”**

  - 使用Navicat创建即可,注意字符集为 utf8

- **在Django项目的settings.py中修改配置**

  ```python
  DEBUG = False  #去掉开发模式          
  ALLOWED_HOSTS = ["*"] #开放访问host
  DATABASES = { #合适数据库参数
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'ems',
          'USER': 'root',
          'HOST': 'localhost',
          'PORT': '3306',
          'PASSWORD': '123456'
      }
  }

  ```

- **发送项目到linux并做移植**

  `python manage.py makemigrations`

  `python manage.py migrate`

- **编写uWSGI的配置文件**

  ```python
  #随意找一个目录，创建一个文件：config.ini -- 建议放在项目的根目录下
  [uwsgi]
  http = 192.168.134.128:9000 # uWSGI服务器访问地址
  #uWSGI和nginx通信的port
  socket = 192.168.134.128:9001
  # the base directory (full path)
  chdir = /usr/local/django_projects/ems #项目所在目录
  # Django's wsgi file
  wsgi-file = ems/wsgi.py #基于项目目录的相对路径
  # maximum number of worker processes
  processes = 4
  #thread numbers startched in each worker process
  threads = 2
  #monitor uwsgi status 通过该端口可以监控 uwsgi 的负载情况
  stats = 192.168.134.128:9002
  # clear environment on exit
  vacuum = true
  pidfile = /usr/local/django_projects/ems/uwsgi.pid #进程ID存放于此文件，位置可以自定义
  #daemonize-run ,file-to-record-log
  daemonize = /usr/local/django_projects/ems/uwsgi.log #后台启动模式，日志文件记录位置自定义
  #http://ip:port/static/...请求会进入该目录找资源，此处可以指向某个app下的static目录
  #或是将所有静态文件汇总到项目的某一个目录下，然后配置在此是更好的选择
  #汇集所有已安装app的静态资源到一个目录下，请参见后续内容
  #http://ip:port/static/a/b/c/d.png   ==>  /usr/local/xxxx/static/a/b/c/d.png
  static-map =/static=/usr/local/xxx/static  # 只在你写的static-map中找静态资源 
  ```

- **根据如上配置启动uWSGI服务器**

  `uwsgi --ini config.ini`  **#注意：config.ini是一个相对路径**

- **关闭服务器**

  `uwsgi --stop uwsgi.pid` **#通过进程id文件**

  * 可以通过 `ps -ef | grep uwsgi` 查看是否启动该服务

- **部署项目技巧：静态资源管理之汇总**

- 开发服务器 -> 查找静态资源 在app下或项目的根目录下找

- 而uWSGI服务器有自己的查找静态资源的规则


  - 在project的settings.py中添加配置：`STATIC_ROOT = os.path.join(BASE_DIR,'static')`

    STATIC_ROOT指向project目录下的`static`目录

  - 执行汇总指令：`python manage.py collectstatic`  

    **会将所有已安装   *APP下的静态资源*    以及**

    **额外添加的静态目录   *STATICFILES_DIRS*  汇总到指定目录**

  - 然后在uWSGI的配置文件中：`static-map =/static=/usr/local/xxx/xxx  ==>指定目录`
