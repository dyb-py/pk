# Web第二阶段课程补充内容

### 一、关于uWSGI服务器

#### 1、为什么不能使用Django框架自带的服务器部署项目

虽然Django内置的服务器遵循了wsgi协议，但是只作为开发测试使用，并且它是单进程

`Django或其它框架开发的Python Web项目，必须要有一个server来运行application`

#### 2、什么是uWSGI服务器

uWSGI服务器是遵循了wsgi、uwsgi、http协议而实现的Web Server。uWSGI旨在为部署分布式集群的网络应用开发一套完整的解决方案 



#### 3、wsgi与uWSGI的区别

WSGI不是服务器，python模块，框架，API或者任何软件，只是一种规范，描述web server如何与web application通信的规范。 

uWSGI服务器是遵循了wsgi、uwsgi、http协议而实现的Web Server。

 ![201881100130096](uWSGI+Nginx+Django+EMS项目补充.assets/201881100130096.png)



#### 4、uWSGI部署Django项目

（1）可以在putty终端中使用` python manage.py runserver 0.0.0.0:8899` 来启动django项目（`allowed_hosts=["*"]`），此时开启的是django内置的开发服务器，然后打开Windows浏览器访问，保证项目可以正常访问。

（2）安装uWSGI服务器，并配置config.ini

```python
[uwsgi]
http = 192.168.134.128:9000 # uWSGI服务器访问地址  保证ip地址正确
socket = 192.168.134.128:9001
chdir = /usr/local/django_projects/ems_project #项目所在目录  保证项目路径正确
wsgi-file = ems_project/wsgi.py #基于项目目录的相对路径
processes = 4
threads = 2
stats = 192.168.134.128:9002
vacuum = true
pidfile = /usr/local/django_projects/ems/uwsgi.pid #进程ID存放于此文件，位置可以自定义   路径要正确
daemonize = /usr/local/django_projects/ems/uwsgi.log    # 路径要正确
static-map =/static=/usr/local/项目目录/static  # 只在你写的static-map中找静态资源    路径要正确
```

此时 通过`uwsgi --ini config.ini `如果提示错误，一定是配置文件有问题

**注意：**修改完配置文件，需要关闭当前的uWSGI服务

- `uwsgi --stop uwsgi.pid`
- `ps -ef | grep uwsgi`  `kill -9 进程号`

（3）如果此时没有提示错误，但在浏览器访问时，页面访问不到

​	未关闭防火墙或多次启动了uwsgi服务器

（4）如果页面能访问到，但提示server 500, 可能是mysql服务未启动 或  项目代码有问题

- 启动mysql服务  `service mysqld start` 如果 mysql服务无法启动，检查mysql配置文件`/etc/my.cnf`
- 项目代码有问题： 回到（1）第一步，或从linux中下载到windows，然后通过pycharm打开运行并检查

（5）打开页面，无css样式 

`static-map =/static=/usr/local/项目目录/static` 路径有问题

是否将每个app下的静态资源，收集汇总到一个总的static目录中，并将该目录作为static-map

（6）操作项目：

- 访问登录，注册页面  验证码是否显示？数据库是否配置正确--settings.py  数据库服务是否开启
- 提交注册，并回到登录页面，是否可以正常登录   
- 其它功能演示：员工列表，增删改操作

（7）上传头像，页面不显示

​	原因：原来的django内置的开发服务器，查找静态资源是在每个app的static目录，或`STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')`所指定的目录中查找静态资源，而uWSGI服务器是在`static-map =/static=/usr/local/项目目录/static`中查找。  

之前上传头像在项目根目录的media目录，为了让头像能作为静态资源显示，我们又将media目录增加在了了`STATICFILES_DIRS`中：

```python
# 头像上传到的目录
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

# 增加静态资源的查找路径
STATICFILES_DIRS = [os.path.join(BASE_DIR,"static"),MEDIA_ROOT]
```

​      如何解决：

把MEDIA_ROOT直接改为`MEDIA_ROOT = os.path.join(BASE_DIR,"static")`，即头像直接上传到项目根目录的static目录中，并且把项目根目录的static作为了static-map



# 终级目标任务：

通过uWSGI服务器，访问ems项目，所有功能都可以正常使用。



### 二、关于Nginx服务器

#### 1、nginx的作用

- 静态HTTP服务器（ 处理静态资源 - 动静分离）： 

  首先，Nginx是一个HTTP服务器，可以将服务器上的静态文件（图片、CSS、JS文件等）通过HTTP协议展现给客户端。   将静态资源的处理交给Nginx服务器，目的：uWSGI

  Nginx提供的动静分离是指把动态请求和静态请求分离开，合适的服务器处理合适的请求，使整个服务器系统的性能、效率更高。 

  uWSGI更适合做动态内容的执行，nginx更适合做静态内容的处理，客户端请求直接访问nginx服务器，留下静态部分处理，动态部分转发给uWSGI服务器，最终实现“动静分离”。

  

- 反向代理服务器：   代理商  中介   租户 ->租房的请求 -> 中介 -> 房东

  反向代理是指以代理服务器nginx来接受internet上的请求，然后将请求转发给内部网络上的其它服务器uWSGI，并将从uWSGI服务器上得到的结果返回给internet上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。  

  

- 负载均衡 ：

  多在高并发情况下需要使用。其原理就是将数据流量分摊到多个服务器执行，减轻每台服务器的压力，多台服务器(集群)共同完成工作任务，从而提高了数据的吞吐量。

#### 2、负载均衡策略

```python
*默认:轮询
		upstream django {
			server 192.168.0.103:8989;   
			server 192.168.0.104:8989;
		}
*iphash:基于ip的负载均衡.
		upstream django {
			ip_hash;
			server 192.168.0.103:8989;
			server 192.168.0.104:8990;
		}
*权重轮询:
        upstream django {
			server 192.168.0.103:8989 weight=1;   
			server 192.168.0.104:8990 weight=2;   
		}
*最小连接数：
		upstream django {
			least_conn;   
			server 192.168.0.103:8989;
			server 192.168.0.104:8990;
		}
```

#### 3、使用Nginx访问ems项目

（1）先搭建至少两台uWSGI服务器（克隆），服务器中的项目要完全一样 保证通过每台uWSGI服务器都可以访问项目

（2）修改Nginx的配置文件

到配置路径中的`nginx.conf`      `/usr/local/nginx/conf/nginx.conf` 

```
upstream ems{
	server 192.168.157.141:9001; # uWSGI's socket = 192.168.x.x:9001
	server 192.168.157.142:9001; # uWSGI's socket = 192.168.x.x:9001

	#可以在添加其他的uWSGI的服务器
}

server {
	listen 80;
	server_name  192.168.157.142;   # nginx服务器的ip
	charset utf-8;
	
	location / {
		uwsgi_pass ems; #和上面的upstream转接  
		include  /usr/local/nginx/conf/uwsgi_params; # the uwsgi_params file you installed
	}	
	location /static { #http://ip:80/static/a/b/c/d.png  ==> /usr/local/static/a/b/c/d.png	
		alias /usr/local/static; # your Django project's static files - amend as required
	}
 ...
｝
```

配置好后，重启nginx即可。

注意：每次修改完配置文件，`nginx -s reload` 不要重复开启nginx服务器  可以ps查看

（3）在命令行中直接输入` nginx`或``nginx -s reload` ,报错，此时一定是nginx的配置文件有问题 

（4）启动nginx服务器不报错，但在浏览器中输入ip访问不到页面，报错

- 防火墙是否关闭，数据库服务是否启动
- server 500    代码有问题，要修正代码，或可以在浏览器中使用F12-network查看检查
- 看nginx的错误日志 logs目录下的-error.log    
- 验证码不显示，看上一节uwsgi中提到的验证码不显示的解决方案

（3）操作ems项目

- 负载均衡时，要求每刷新一次，页面有变化 111 -- 222  

   但部分同学，刷新无变化，是由于在当前页面中，不只一个请求 （一个login,一个getcaptcha）

- 提交注册，并登录  如果无法登录，两台uwsgi中的项目使用的数据库是两个，不是指向同一台数据库

  在settings.py文件中，修改databases，把hosts指向某一台uWSGI服务器中的数据库 

  或 单独配置一台msyql服务器 -- 只运行着mysql服务

- 头像不显示

  在nginx中无法访问，是由于Nginx在查找静态资源时，是在nginx服务器的/usr/local/static   
  	 如果添加一条数据（包括头像），头像被上传到media目录中 

  	 如何解决： 
  	 （1）方案一：将头像上传到nginx的static中，而不是项目的media中，涉及到nginx文件上传 ，但在后续做uwsgi集群时头像显示依然有问题
  	
  	 （2）方案二：搭建一个分布式文件系统 -- 单独开一台服务器，FastDFS ，只需要在请求静态资源时，由nginx将请求转发给fastdfs文件系统

  补充：

```
STATICFILES_DIRS = [MEDIA_ROOT]  # 是使用pycharm运行，内置服务器查找静态资源的路径
如果是uwsgi访问时，该配置可以删除

STATIC_ROOT = os.path.join(BASE_DIR, 'static') 收集各个app下的静态资源时使用，当执行完python manage.py collectstatic后，该配置可以被删除


```



### 三、关于Django

#### 1、传值

- （1）view传值给template  render(request,'xxx.html',{'key':'value'})

- （2）重定向传值

  ```
  方式一：
  url = reverse("xxx")+"?name=Mr_lee&passworld=123456"
  return redirect(url)
  
  方式二：
  path("index1/<id>/<name>/",views.index1,name="index1"),
  def index1(request,id,name):
      xxx
  
  redirect("redirect:index1",1,"Tom")
  或  redirect("redirect:index1",id=1,name="Tom")
  ```

- （3）session传值



#### 2、错误提示

(用户名或密码错误，用户名已存在 ，验证码错误 -- 使用ajax)

#### 3、断点调试 breakpoint

#### 4、namespace



### 四、关于EMS项目![微信图片_20190106165753](uWSGI+Nginx+Django+EMS项目补充.assets/微信图片_20190106165753.png)

