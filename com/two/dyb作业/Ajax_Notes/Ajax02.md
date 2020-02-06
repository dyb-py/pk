# Ajax-JSON  

### 一、引言

Ajax异步请求是Javascript和Python（或其它语言）的通信，也属于跨平台通信的范畴。数据格式采用了字符串的形式。    

（Ajax是运用在客户端浏览器的技术，用于向服务器发送一个异步请求。 从发送请求--服务器接收并处理请求--返回响应结果，在此过程中客户端和服务器完成了一次数据交换。客户端发送“用户名”给服务器，服务器返回“用户名已存在/用户名合法”）

之前通信的字符串中包含的数据量较小，OK、Error等简短的信息。   

如果要在异步请求中通信更大量的数据呢，如何做？ 

比如：客户端发送一个请求到服务器，请求查询所有用户的信息.

之前所学，通过HttpResponse() render()都不太合理。

 * 直接把数据作为 返回数据。数据类型为字符串，无法直接操作。 return HttpResponse(users)

 * 先渲染在页面html文件，然后返回，此时可以，但是会有大量额外非数据进行交换。return render(request,'xxx.html',{'users':users}) 

 * 需要 只传数据。自己拼接一个格式字符串，需要前端人员按照该格式进行分割，但是该方式不能官方。


### 二、数据交换格式 

#### 1、XML

1.1 XML简介

XML即可扩展标记语言(extensible Markup Language)。标记是指计算机所能理解的信息符号，通过此种标记，计算机之间可以处理包含各种信息 。

- XML是一种标记语言，类似HTML
- **XML的设计宗旨是传输数据，而非显示数据**    
- XML只是简单地描述信息,并以独立于平台的格式进行分发。 由于不需要使用任何一种特定的语言,因此 XML 与某一平台无关。 

```xml
<?xml version="1.0" encoding="utf-8"?>      //指明了XML的版本号和编码方式
<Employees> 
 	<Employee> 
    	<Name>Bob Smith</Name> 
    	<PhoneNumber>408-555-1000</PhoneNumber> 
	 </Employee> 
 	<Employee> 
    	<Name>Sally Jones</Name> 
		<PhoneNumber>415-555-2000</PhoneNumber>         
	</Employee> 
</Employees>
```

XML设计用来传送及携带数据信息，不用来表现或展示数据，HTML语言则用来表现数据，所以XML用途的焦点是它说明数据是什么，以及携带数据信息。 

#### 2、JSON

##### 2.1 简介

- JSON（JavaScript Object Notation）是一种轻量级的数据交换格式。
- JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C、C++、C#、JavaScript、Java、Perl、Python等）。这些特性使JSON成为理想的数据交换语言。 
- 易于人阅读和编写，同时也易于机器解析和生成(网络传输速度)。 
- JSON 文本格式在语法上与创建 JavaScript 对象的代码相同。由于这种相似性， 无需解析器， JavaScript 程序能够使用内建的parse() 函数（代替 之前的 eval()）， 用 JSON 数据来生成原生的 JavaScript 对象。  



##### 2.2 JSON结构

JSON有两种结构：

-   字典：表示为“{}”括起来的内容，如{key：value,key2：value2,...}的键值对的结构，key一般为字符串类型，value的类型可以是数字、字符串、数组、字典等。

-   数组（列表 ）：表示用“[]”括起来的内容， 如：["Tom","Jack",...] 经过字典、数组2种结构就可以组合成复杂的数据结构了。


按照最简单的形式，可以用下面这样的 JSON 表示"键/值对"：

```json
{"FirstName":"Brett"}
```

  当将多个"键 / 值对"串在一起时，JSON 就会体现出它的价值了。首先，可以创建包含多个”键 / 值对"的 记录，比如： 

```json
{"FirstName":"Brett","LastName":"McLaughlin","Email":"aaaa"}
```

更为复杂的JSON数据：

```json
{
	"people":[
        {"FirstName":"Brett","LastName":"McLaughlin","Email":"aaaa"},
        {"FirstName":"Jason","LastName":"Hunter","Email":"bbbb"},
        {"FirstName":"Elliotte","LastName":"Harold","Email":"cccc"}
    ]
}
```



#### 3、XML与JSON对比

![1534181711280](Ajax_pic\1534181711280.png)



编码的可读性，xml有明显的优势，毕竟人类的语言更贴近这样的说明结构。json读起来更像一个数据块，读起来就比较费解了。不过，我们读起来费解的语言，恰恰是适合机器阅读和解析。

编码的手写难度来说，xml还是舒服一些，好读当然就好写。不过写出来的字符JSON就明显少很多。去掉空白制表以及换行的话，JSON就是密密麻麻的有用数据，而xml却包含很多重复的标记字符。

虽然XML和JSON都有各自的编码工具，但是JSON的编码要比XML简单，即使不借助工具，也可以写出JSON代码，但要写出好的 XML代码就有点困难；与XML一样，JSON也是基于文本的，且它们都使用Unicode编码，且其与数据交换格式XML一样具有可读性。

主观上来看，JSON更为清晰且冗余更少些。JSON网站提供了对JSON语法的严格描述，只是描述较简短。从总体来看，XML比较适合于标记文档，而JSON却更适于进行数据交换处理。

在解析上，在普通的web应用领域，开发者经常为XML的解析伤脑筋，无论是服务器端生成或处理XML，还是客户端用Python解析XML，都常常导致复杂的代码，极低的开发效率。  

作为一种轻量级的数据交换格式，json正在逐步取代xml，成为网络数据的通用格式。

有的json代码格式比较混乱，可以使用此`http://www.bejson.com/`网站来进行JSON格式化校验。此网站不仅可以检测Json代码中的错误，而且可以以视图形式显示json中的数据内容，很是方便。



### 三、Model转JSON              

#### 1、json.dumps

在Pyhton中我们通过json模块，将常用的数据类型转化为json字符串。但是，json支持转化的数据类型是有限的。 

```python
import json

list = ['Tom','Jack','Lina','Jane']
str = json.dumps(list)

print(str)
print(type(str))
```

JSON序列化所能支持的Python数据类型：

```
+-------------------+---------------+
| Python            | JSON          |
+===================+===============+
| dict              | object        |
+-------------------+---------------+
| list, tuple       | array         |
+-------------------+---------------+
| str               | string        |
+-------------------+---------------+
| int, float        | number        |
+-------------------+---------------+
| True              | true          |
+-------------------+---------------+
| False             | false         |
+-------------------+---------------+
| None              | null          |
+-------------------+---------------+
```



#### 2、Model -> JSON

- 直接使用dumps序列化Model

  ```python
  def query(request):
      users = User.objects.all()    
      json_str = json.dumps(users)
      return HttpResponse("abc")
  ```

  当提交请求时，将发生以下错误：

  ​	TypeError：`<QuerySet []> is not JSON serializable`

- 将QuerySet 转为list：

  ```python
  def query(request):
      users = User.objects.all()    
      json_str = json.dumps(list(users))   #将QuerySet对象转为list
      return HttpResponse(json_str)
  ```

  再次访问，依然提示错误：

  TypeError：`<User: Tom> is not JSON serializable`



**原因：**

```
To extend this to recognize other objects, subclass and implement a
``.default()`` method with another method that returns a serializable
object for ``o`` if possible, otherwise it should call the superclass
implementation (to raise ``TypeError``).
```

**解决方案：**

```python
def user_default(u):
    if isinstance(u,User):
        return {'id':u.id,'name':u.name,'age':u.age,'salary':u.salary}
    u.salary-DecimalField python内置没有该数据类型，使用strftime()格式化成字符串
```

```python
def query(request):
    users = User.objects.all()    
    json_str = json.dumps(list(users),default=user_default)   #将QuerySet对象转为list
    return HttpResponse(json_str)
```

**或者：**

```python
def query(request):
    users = User.objects.all().values()  #返回字典形式的QuerySet    
    json_str = json.dumps(list(users))   #将QuerySet对象转为list
    return HttpResponse(json_str)
# 使用此方法，需要注意User类中不能有不可序列化的类型
```



#### 3、JsonResponse对象

原型：

```python
class JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None,**kwargs) 
```

这个类是HttpResponse的子类，它和父类的主要区别在于： 

- 它的默认Content-Type 被设置为： application/json     
- 第一个参数，data应该是一个字典类型，当 safe 这个参数被设置为：False ,那data可以填入任何能被转换为JSON格式的对象，比如list, tuple, set。 默认的safe 参数是 True. 如果你传入的data数据类型不是字典类型，那么它就会抛出 TypeError的异常。
- json_dumps_params参数是一个字典,它将调用json.dumps()方法并将字典中的参数传入给该方法。

```python
def query1(request):
    user = User.objects.get(pk=1)
    return JsonResponse(user,safe=False,json_dumps_params={"default":user_default})

def query2(request):
    users = list(User.objects.all())
    return JsonResponse({"users":users},json_dumps_params={"default":user_default})
```

总结：

​	1、JsonResponse内部会调用json.dumps，即JsonResponse的第一个参数可以直接接Model/集合

​	2、但使用JsonResponse仍然需要设置default --` JsonResponse(data，json_dumps_params={"default":user_default})`

​	3、如果data不是字典dict类型，需要将data转为dict ` {"key":data}` 或者直接将safe参数设置为False

​	4、如果JsonResponse的第一个参数是dict类型，则在Javascript中 JSON.parse() 解析成 js对象



### 四、Jquery-Ajax    

#### 1、$.ajax() 

```js
$.ajax({
   type:"POST",
   url:"{% url 'ajaxapp:test' %}",
   data:"name=lilei&age=18&csrfmiddlewaretoken="+"{{ csrf_token }}",
   success:function (msg) {
       alert(msg)
   }
})
```



#### 2、$.get()

- **url**:待载入页面的URL地址
- **data**:待发送 Key/value 参数。
- **callback**:载入成功时回调函数。
- **type**:返回内容格式，xml, html, script, json, text, _default。

```js
$.get(
    "{% url "ajaxapp:test" %}",          
    "name=lilei&age=18",
    function(data){
        alert(data)
    },
    "json"   # json对象格式
)
```

#### 3、$.post()

```js
$.post(
    "{% url "ajaxapp:test" %}",
    "name=lilei&age=18&csrfmiddlewaretoken="+"{{ csrf_token }}",
    function(data){
        alert(data)
    },
    "text"   # 字符串格式
)
```
#### 4、$.ajaxSetup()

使用jQuery的$.ajaxSetup方法可以设置AJAX请求的默认参数选项，当程序中需要发起多个AJAX请求时，则不用再为每一个请求配置请求的参数。 

```
对$.post和get无效
```

```js
//为所有的请求 设置headers和url参数选项
$.ajaxSetup({
    headers:{"X-CSRFToken":"{{ csrf_token }}"},
    url:"{% url 'ajax_query_user:query' %}"
    })
```



#### 5、load()方法

load() 方法通过 AJAX 请求从服务器加载数据，并把返回的数据放置到指定的元素中。

```js
$("#div_1").load("{% url 'ajaxapp:loadHTML' %}")
```

 

作业：

	 - 输入框 内 查询 内容。输入框输入内容时 键盘抬起，进行 相关数据 表格形式 呈现在页面。
	 - 以上作业 使用 JS /JQ来完成。
	 - 第一天作业，移植到ems项目