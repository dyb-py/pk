# JQUERY

## 简介

JavaScript的框架，是一套工具库。简化了JavaScript的功能实现。可以使得开发者写更少的代码，却做更多的事-write less do more.

模仿CSS获取DOM元素，比原生的javascript要方便很多，并且可以对多个CSS集中处理，常用的CSS功能封装到了单独的方法 。最重要的是jquery代码兼容性非常好，不需要考虑不同浏览器的兼容性问题。

## 学习目标

* DOM编程的相关操作
* 事件的管理
* Ajax的封装

## 第一个程序

```javascript
//导入Jquery的js文件
<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
<!--<script src="{% static  'jquery_app/jquery-1.8.3.min.js' %}"></script>-->
<div style="height:100px;background-color: red" id="con"></div>
<script type="text/javascript">
	//jquery入口函数 简写：$(function(){});
  $(document).ready(function(){
    //选择id为con的标签
      var div = $("#con");
      //隐藏标签，隐藏间隔1000ms
      div.hide(1000);
    });
	
</script>
```

## 选择器 -- 元素节点获取

### 基本选择器

> **ID 选择器**
>
> $("#id")
>
> `$("#abc");//获得id为abc的标签`

> **类选择器**
>
> $(".样式类名")
>
> `$(".abc");//获得样式类名为abc的所有标签`

> **元素选择器**
>
> $("标签名")
>
> `$("span");//获得所有span标签`

> **全选择器**
>
> `$("*") 选出整个文档`

> **交集/并集选择器 （或、且）**
>
> 	//类名为a的div标签
> 	var div3 = $("div.a");//div且样式类为a，".adiv"是错误写法
> 	//. 逗号拼接多个选择器
> 	var div4 = $("div,.a,input");

### Jquery对象和Dom对象转换

> * **document.getElement...(xxx)     返回DOM对象**
>
> * **Jquery的选择器                                返回Jquery对象**
>
> * **都是对一个或多个标签的封装，都指向一个或多个标签，只是支持的功能不一样，DOM对象和Jquery对象都有各自的方法**
>
>   ```javascript
>   var a = document.getElementById("con");
>   var b = $("#a");
>
>   a.value; a.id;
>   b.val(); b.attr("id"); b.hide(1000);
>   ```
>
> * **相互转换**
>
>   * **DOM --> Jquery** 
>
>     ```javascript
>     var div = document.getElementById("con");//dom对象
>     var divJ= $(div);//jquery对象
>     ```
>
>   * **Jquery --> DOM**
>
>     ```javascript
>     var div = $("#con");//jquery对象
>     var divD= div.get(0);//dom对象
>     var divD= div[0];//dom对象
>     ```
>



### 层级选择器

> **后代选择器**
>
> $(selector1 selector2)
>
> `$("div .a");`//选择所有的div，其中样式类为a的后代
>
> `$("div .a input");`//选择所有的div，其中样式类为a的后代，再选择这些后代的input后代标签

> **子代选择器**
>
> $(selector1>selector2)
>
> `$("span>input");`//所有的span的input子标签
>
> `$("div span>input");`//所有div的span后代的input子标签

>**后续所有兄弟**
>
>$(selector1~selector2)
>
>`$("div~span~input");`//div的所有后续span兄弟标签的所有后续input兄弟标签

>**后续紧邻兄弟**
>
>$(selector1+selector2)
>
>`$("div+span+input");`//div后的所有紧邻的span后的所有紧邻input

>**后代选择方法 find() **
>
>`$("div").find("p"); `//选择到div后代中的p标签


>**子代选择器children() **
>
>`$("div").children("p");` //获取div中所有的p标签子元素（儿子，孙子，子孙后代）


>**父选择器parent()  **
>
>parentNode 原生js中
>
>`$("li").parent();` //获取li元素的父元素

>**后一个兄弟元素节点next()**
>
>`$("li").next(); `//获取li之后的下一个兄弟节点


>**前一个兄弟元素节点prev() ** 
>
>`$("li").prev();` //获取li之前的前一个兄弟节点


### 简单过滤选择器
* **`:first`  //选出匹配到的标签中的第一个元素**

  `$("div>input:first");//div下所有input子标签中的第一个`

* **`:last` //选出匹配到的标签中的最后一个元素**

  `$("div>input:first");//div下所有input子标签中的最后一个`

* **`:eq(index)` //选出对应索引值得元素 *index从0开始**

  `$("div span+div>input:eq(1)");//div下所有span后代的后续紧邻的div下的所有input子标签中的第二个`

* **`:gt(index)` //选出索引值大于index的元素  *index从0开始**

  `$("div>input:gt(1)");//div下所有input子标签中索引大于1的`


* **`:lt(index)` //选出索引值小于index的元素  *index从0开始**

  `$("div>input:lt(1)");//div下所有input子标签中索引小于1的`

* **`:odd` //选出索引值为奇数的元素  *从0开始**

  `$("div>input:odd");//div下所有input子标签中索引为1,3,5..的`

* **`:even` //选出索引值为偶数数的元素  *从0开始**

  `$("div>input:odd");//div下所有input子标签中索引为2,4,6..的`

* **`:not(selector)` //选出selector不能匹配到的元素**

  `$("div>input:not(.a)");//div下所有input子标签中样式类名不是a的``$("div>input(.a)");//div下所有input子标签中样式类名不是a的`

  `$("#abc>li:not(#a)");//id为abc的标签下的li子标签中id不是a的`

  `$("#abc>li:not(:eq(2))");//id为abc的标签下的li子标签中索引不是2的`

### 内容过滤选择器

* `:empty`   没有内容的标签 (标签体中的文字或子标签)

  ​	$("p:empty")

* `:parent`  有内容的标签

  ​	$("p:parent")

* `:has(selector)`  拥有某种后代的 标签

  ​	$("div:has(p)")

* `:contains(text)` 模糊匹配 (自己含有，或后代含有)

  ​	$("span:contains('hello')")

### 属性过滤选择器

* `$("[name]")`  有name属性的
* `$("[name='houqn']")`  name属性值为zhj的
* `$("[value='male']")`  value属性值为male的
* `$("[type='text']")`  type属性值为text的

### 可见性过滤选择器

* `:visible`  可见元素
* `:hidden`    隐藏元素 （包含隐藏域）

### 表单选择器

* `:text` 选择所有输入框
* `:radio`
* `:checkbox`
* `:checked`   适用于单选按钮 和 复选框
* `:selected`  适用于下拉框



## HTML标签操作

### 节点的增删插入

* 创建元素 
  `$("<div>我是div</div>"); `//创建了一个div元素节点

* append()  在某元素内的末尾追加元素节点

  `$("div").append('<input type="text"/>');`//div内部最后一个位置添加input

* prepend() 在某元素节点内的头位添加元素节点

  `$("div").prepend('<input type="text"/>');`//div内部第一个位置添加input

* A.before(B) A某元素节点之前添加新节点B

  `$("div").before('<input type="text"/>');`//div之前添加input兄弟

* A.after(B) A某元素节点之后添加新节点B

  `$("div").after('<input type="text"/>');`//div之后添加input兄弟

* empty() 清空所有子元素(光杆司令)

  `$("div").empty();`//清空div内容

* remove() 清空所有，先他杀，后自杀

  `$("div").reomve();`//删除div

### 属性增删改查 

* `attr("属性名")`  获取属性名`attr("属性名","属性值")`  设置属性值
* `attr({属性名1:属性值, 属性名2:属性值,...})`  一次设置多个属性值
* `removeAttr("属性名")`  删除标签的属性
* `prop`  和attr使用一致，作用一致,jquery1.6之后新增；但prop在获取bool类型属性时(checkd,selected)更友好

### 样式设置

* `css("样式属性名")` 获取样式属性值
* `css("样式属性名"，"样式属性值")` 设置样式属性值
* `css({"样式属性名1":"样式属性值","样式属性名2":"样式属性值",..})` 设置多个样式属性
* `addClass("样式类名")`  将一个样式表设置给标签
* `removeClass("样式类名")` 将标签的样式表移除

### 内容文本的设置

* `val()/val(txt)`   获取/设置value属性值
* `text()/text(txt)`  获取/设置标签体中的文字
* `html()/html(html)`   获取/设置标签体中的html代码(子标签+文本)

### 尺寸设置

*  `$(selector).height();` //带参数设置，不带参数获取,参数是number类型

*  `$(selector).width(200);` //带参数设置，不带参数获取

*  `innerWidth():` 获取匹配元素的外宽度，包含content + padding 
*  `outerWidth() :`获取匹配元素的外高度，包含content + padding + border,如果传一个参数true,就再加上margin

## 事件管理

### 事件的注册方式

* 基于标签：和之前JS中使用方式一致,Jquery未加干涉

* 基于编程：Jquery提供了全新的API  (解耦  强耦合)

  ```javascript
  <input type="button" id="abc" value="click"/>
      
  btn = document.getElementById("abc");
  btn.onclick=function(){
      .......
  }
  ```

### 事件注册示例

```javascript
$(function(){//ready的简写格式,等价于onload
  $("input").click(function(event){//为input注册单击事件，event是事件对象,event是可选参数
  	console.log($(this);//this = 触发事件的标签的dom对象
    console.log('click~~~');
  });
});
//如果不定义ready函数，则需要将事件注册代码置于标签之后
```

### Ready事件

> 等价于onload的作用，用于保证代码的执行在页面加载之后

```javascript
$(document).ready(function(){...});
$(function(){...})
```

### Jquery事件函数

* click()

* dblclick()

* blur()

* focus()

* mouseover()

* mouseout()

* mousemove()

* mouseup()  鼠标左键抬起

* mousedown()  鼠标左键按下

* keydown()  键盘按键按下，可能连续触发

* keyup()   键盘按键抬起

* change()

* hover()   鼠标移入移出的复合事件

* submit()

  `$("form").submit();`

  ```javascript


  $("div").hover(
    function(){//mouseover时触发
      $("div").css("background-color","blue");
    },
    function(){//mouseout时触发
      $("div").css("background-color","red");
    }
  );
  // 键盘事件
  $("input[type='text']").keydown(function(event){
       console.log("key down");
       event.stopPropagation();//停止冒泡
   });
  $("input[type='text']").keyup(function(event){
      console.log("key up");
      console.log(event.keyCode);//keyCode==键盘字符的ascii码
  });
  ```

> 技巧：THIS
>
> ```javascript
>  $("input[name='a']").click(function(){
>      //获取当前标签的vlaue
>      value1 = this.value;//this = 当前触发事件的标签 = dom
>      value2 = $(this).val();
>      console.log(value1);
>      console.log(value2);
>  });
> ```

### on 

```javascript
$("#con").click(function(){...});       <1>
$("#con").on("click",function(){...});  <2>与<1>等价
$( "#dataTable tbody" ).on( "click", "tr", function() {
      console.log( $( this ).text() );
    });给tbody的子元素tr绑定单击事件
```

### off 解绑

```javascript
$("body").on("click","p",foo);
$("body").off("click","p",foo);
```

### 事件对象

```javascript
$("body").click(function(e){
  console.log(e)
})

$("body").click(function(e){
  e.preventDefault();//阻止默认行为
  });
$("body").click(function(e){
  e.stopPropagation();//阻止冒泡
  })
```

## 动画

* 隐藏 显示 show() hide()  参数：指定毫秒数，回调函数
* show(1000,callback)  动画显示
* hide(1000)  动画隐藏
* slideUp(1000);  从下到上隐藏
* slideDown(1000); 从上到下显示
* slideToggle(1000); 卷起卷下切换
* fadeIn(1000); 淡入
* fadeOut(1000); 淡出
* fadeTo(1000,0.5) 淡入到不透明度为0.5
* 自定义动画：$(selector).animate({params},speed,callback);
  * animate({height:"200px",width:"200px",opacity:"0.5"},1000);  指定的属性会同时动画
  * speed："slow"、"fast" 或毫秒
  * params：中如果涉及到中间连字符，同样需要转成camel。如果颜色动画，需要借助插件。
* stop() 停止动画 参数，true false
  * 第一个参数：规定是否应该清除动画队列。默认是 false，即仅停止活动的动画，允许任何排入队列的动画向后执行
  * 规定是否立即完成当前动画。默认是 false
  * stop() 按钮会停止当前活动的动画，但允许已排队的动画向前执行
  * stop(true,false) 按钮停止当前活动的动画，并清空动画队列；因此元素上的所有动画都会停止。
  * stop(true,true) 会立即完成当前活动的动画，然后停下来。





## jQuery对象遍历

* each() 函数

```javascript
var cks=$("xxx");
for(var i=0;i<cks.size();i++){//jquery方法：size()==选中的标签数量
  var temp=cks.get(i);//jquery方法:get()==返回选中的标签中的对应索引的标签==dom
  var temp2=cks.eq(i);//jquery方法：eq()==返回选中的标签中的对应索引的标签==jquery
  alert($(temp).val());//jquery方法：val()==返回对应标签的value属性值
  alert(temp2.val());
}
或者：
var inps=$("xx");
inps.each(function(a){//jquery方法：each()  a为循环变量，从0开始,等价于上述的i
    //inps.get(a);//获取当前标签
  //this-->当前遍历到的标签对应的dom对象
  //$(this)-->当前遍历到的标签对应的jquery对象【dom对象转换成jquery对象】
  alert(a+" "+$(this).val());
  alert(this.value);
});
inps.each(function(){
  $(this).addClass("foo")
  })
inps.each(function(index,element){
  console.log(index + ":" + $(this).text())
  })
inps.map(function(element,index){})
```

## 链式chaining

* end() 结束当前链最近的一次过滤操作

`$("xxx").attr("","").attr("","").hide();`
`$("xxx").next().next();`
`$("xxxx").append("xxx").append("xxx").append("xxx").after("xxx").hide();`

