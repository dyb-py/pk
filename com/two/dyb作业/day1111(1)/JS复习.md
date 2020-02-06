JS复习

ajax

1.创建xhr对象

​	浏览器兼容 IE5/6

​	var xhr = new XMLHttpRequest()

2.初始化配置工作

​	xhr.open(method,url,sync)  

3.发送请求

​	xhr.send(string)  string-post请求

4.接收响应

​	xhr.onreadystatechange = function(){

​		if (xhr.readyState === 4 && xhr.status === 200) {

​			xhr.responseText 接收响应  完毕 进行后续js dom操作

​	}

}