# Nginx服务器

### 一、Nginx概述

#### 1、简介

##### 1.1 什么nginx

Nginx是一款轻量级的Web服务器/反向代理服务器 ，其特点是占有内存少，并发能力强。



##### 2.2 nginx的作用

- 静态HTTP服务器（ 处理静态资源 - 动静分离）： 

  首先，Nginx是一个HTTP服务器，可以将服务器上的静态文件（图片、CSS、JS文件等）通过HTTP协议展现给客户端。   将静态资源的处理交给Nginx服务器

  Nginx提供的动静分离是指把动态请求和静态请求分离开，合适的服务器处理合适的请求，使整个服务器系统的性能、效率更高。 

  uWSGI更适合做动态内容的执行，nginx更适合做静态内容的处理，客户端请求直接访问nginx服务器，留下静态部分处理，动态部分转发给uWSGI服务器，最终实现“动静分离”。


- 反向代理服务器：  代理 -- 中介      客户发起一个租房的请求 ->中介-> 房东

  反向代理是指以代理服务器nginx来接受internet上的请求，然后将请求转发给内部网络上的其它服务器uWSGI，并将从uWSGI服务器上得到的结果返回给internet上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。


- 负载均衡 ：

  多在高并发情况下需要使用。其原理就是将数据流量分摊到多个服务器执行，减轻每台服务器的压力，多台服务器(集群)共同完成工作任务，从而提高了数据的吞吐量。 



#### 2、安装步骤

- 将tar包发送的linux

- 解压 `tar -zxvf nginx-1.11.1.tar.gz` 

- 安装依赖 `yum install gcc zlib-devel pcre-devel`   

- cd到解压目录：`./configure`    #配置检测

- cd到解压目录：`make && make install`  #编译并安装

- 安装完成，安装路径为`/usr/local/nginx`   ,日志路径为 `/usr/local/nginx/logs` ,

  可执行文件路径为 `/usr/local/nginx/sbin` ,配置文件路径为 `/usr/local/nginx/conf`

  欢迎页面路径为 `/usr/local/nginx/html`

- `ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx` 制作连接，便于执行`nginx`指令

- `nginx  #启动` 
  `nginx -s stop #关闭`
  `nginx -s reload #重启`

  `http://ip:80即可访问nginx欢迎页面`



### 二、nginx与uWSGI  

nginx配置--到配置路径中的`nginx.conf`      `/usr/local/nginx/conf/nginx.conf` 

```
upstream ems{
	server 192.168.157.141:9001; # uWSGI's socket = 192.168.x.x:9001
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

配置好后，重启nginx即可，可以使用Nginx服务器来访问项目

**注意关闭防火墙！！**

两台虚拟主机，一个运行nginx，其中保存project的静态资源；一个运行uwsgi，其中保存并部署project。



### 三、集群和负载均衡策略

搭建uWSGI集群，只需要多做几份uWSGI的配置文件，文件中设置不同的ip:port，指向相同的project，然后启动多个uWSGI即可。

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

至此，一个uWSGI集群搭建完成，nginx作为反向代理服务器和web服务器接收请求，然后处理静态的部分，动态部分按照负载均衡策略转发给某一个uWSGI服务器。

至此python-web-project成功运行于 一个对高并发有更好支持，具有高可用性（high-available）的系统中





作业：

​	1、完成负载均衡，访问登录页面，刷新时交替出现111，222

​	2、ems项目中的 登录页面，点击登录按钮时，用户名和密码错误时，在当前页面alert显示用户名或密码错误，正确的情况下正确跳转到员工页面

​	3、通过uWSGI直接访问项目时，所有功能实现演示是完整的（包括但不限于 验证码、cookie、session、强制登录、员工头像显示，分页显示、页号定位、添加员工头像等）