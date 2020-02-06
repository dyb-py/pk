# Javascript

## 一、简介

JavaScript 是互联网上最流行的脚本语言，可用于 HTML 和 web，更可广泛用于服务器、PC、笔记本电脑、平板电脑和智能手机等设备。

作用：用来操作html css，实现 交互 。

前端：

* HTML  人的骨骼


* CSS 衣服
* Javascript  人 动起来 行为

JavaScript是一种轻量级、解释性、脚本编程语言，可以执行在所有现代浏览器中。

~~~python

(1) 脚本语言。JavaScript是一种解释型的脚本语言,C、C++、java等语言先编译后执行,而JavaScript是在程序的运行过程中逐行进行解释。
(2) 基于对象。JavaScript是一种基于对象的脚本语言,它不仅可以创建对象,也能使用现有的对象。
(3) 简单。JavaScript语言中采用的是弱类型的变量类型,对使用的数据类型未做出严格的要求,是基于Java基本语句和控制的脚本语言,其设计简单紧凑。
(4) 动态性。JavaScript是一种采用事件驱动的脚本语言,它不需要经过Web服务器就可以对用户的输入做出响应。在访问一个网页时,鼠标在网页中进行鼠标点击或上下移、窗口移动等操作JavaScript都可直接对这些事件给出相应的响应。
(5) 跨平台性。JavaScript脚本语言不依赖于操作系统,仅需要浏览器的支持。因此一个JavaScript脚本在编写后可以带到任意机器上使用,前提上机器上的浏览器支持JavaScript脚本语言,目前JavaScript已被大多数的浏览器所支持。
~~~

**学习目标：JavaScript语法，将JavaScript运用在HTML中定制交互行为，定制前端逻辑**

## 二、第一个程序

```html
<html>
<head>
  <script>
  	//警告弹窗
    alert('Hello, world');
    //向开发者工具的console中输出日志,用来测试
    console.log("日志内容")；
  </script>
</head>
<body>
  ...
</body>
</html>
```

## 三、JS书写三种方式

* javascript定义在script 标签内；

  > script标签可以出现在html的任何位置，一般常放在body内的最下面；在页面加载完成的时候执行
  > ​此脚本代码。
>
> ​	页面中可以有多个script标签，逐个解析。
>
> ​	javascript（以下简称JS）的每个语句建议用分号结尾


* 引入外部的js文件

  ```javascript
    //-- abc.js
    a=10;
    function test(){
      alert("this is test")
    }
  ```

  ```javascript
    //在html文件中如此导入，并使用其中内容
    <script src="abc.js"></script>
    <script>
      test()
      console.log(a)
    </script>
  ```

  >  **注意，script标签如果用来导入外部的js文件，则其中不能再写任何js语句**

* js写在标签内（事件时详细讲解）

## 四、注释

>"//" 注释单行
>
>/* ..  */

## 五、基础语法

#### 1.变量

JS是弱类型的

##### 声明变量并赋值

~~~python
var name = "lilei";
var city = 'beijing';
var age = 18;
console.log(name);
alert(city)
~~~

##### 也可先声明，后赋值

~~~javascript
var a;
a = 1;
~~~

##### 同时定义多个

~~~javascript
第①种：var name1,name2,name3;
第②种：var n1=12,n2=23;
~~~

##### 命名规范

~~~javascript
1、只能有数字、字母、下划线、$这4种符号组成；
2、首字符不能是数字；
3、不能是js语言的关键字与保留字；
4、严格区分大小写
5、-,*,#类似的特殊字符不允许使用
6、习惯上，采用驼峰式命名，除第一个单词外，剩余单词首字母大写。例如：myCar\myDiv
~~~

#### 2.数据类型

##### 1.字符串类型

~~~javascript
字符串由字符构成，用单引号或双引号括起
字符是指计算机中使用的字母、数字和符号，包括：0、1、2、3…、A、B、C…、a、b、c….、~！·# ￥%……—*（）——+等等
~~~

```javascript

var name2 = "bye";
var name3 = 'hello';
var name4 = name2 + name3
```

##### 2.数字类型

```javascript
var age =18；
var price =100.51
var a=3;
```

##### 3.布尔

```javascript
var gender = true; //false

0/非0  ""/非""  null/非null  NaN/非NaN  undefined/非undefined 也可作真假使用
```

##### 4.特殊类型

```javascript
undefined：未赋值的变量的默认值 var a;alert(a)
NaN:not a number, 比如 b = "sf"/2; b的值就是NaN   
	判断是不是一个数字使用：   isNaN(x)
null:Javascript中的关键字，它表示一个特殊值。通常用来描述“空值”
用于置空变量，不是默认值，需要手动赋值  var a="sdf"; a=null;alert(a)
```

##### 5.数据类型转换

```javascript 
转换为字符串：toString() String() 加号拼接（隐式转换）
	String(10)  # '10'    
    10 + ''   # '10'
转换为数值：
  - Number() parseInt() parseFloat()
  - - * / % 隐式转换
转换为布尔类型：Boolean()
	- js中，0 null undefined NaN 都认为是 false
```
**使用 typeof 来检测数据类型**



##### 5.日期

> 注意：月份从0开始

```javascript
var date1 = new Date() //当前系统时间
var date2 = new Date(2018,5,28,10,9,10) // year month day hour minute second ,月份从0开始
var date3 = new Date(2018,5,28)
date3.getFullYear();
date3.getMonth(); //月份，一月是0
date3.getDate(); 
date3.getDay(); //一周的第几天 周日是0
date3.getHours();
date3.getMinutes();
date3.getSeconds();
```

##### 6.数组

```javascript
var a = new Array(); //不建议使用
a[0]="abc"
a[1]="abcd"
var b = [18,"efaga",1000.5]
b[0] // 18
b[1] // "fafag"
```

```javascript
b.length //数组长度:length属性
```

##### 7.Object对象

> 如下两种创建方式，obj的创建方式不建议使用，obj2的创建方式更轻便，建议使用

```javascript
var obj = new Object();
obj.name="claire";
obj.age=18;
obj.sayHi=function(){ //为对象添加方法
			console.log("hi~")
		  }
		  
var obj2={name:'claire',age:18,sayHi:function(){console.log("hi~");}}
//使用
console.log(obj.name)
console.log(obj2.name)
obj.sayHi()
obj2.sayHi()
```

##### 8.Math

```javascript
Math.round(4.5) // 5，四舍五入 取整
Math.ceil(4.1) // 5,向上舍入
Math.floor(4.6) // 4,向下舍入
Math.random() // 0-1之间的随机数，包含0，不包含1
Math.round(Math.random()*10) // 0-10之间的随机整数
Math.round(Math.random()*9)+1 // 1-10之间的随机整数
```



#### 3.运算符

表达式（字面量）是由字符、字符串、数值或者变量名，运算符构成。

##### 1.算术运算符

**%  + - * / **

~~~javascript
+ 
    - 算数运算符
	- 拼接运算符
		任何其他数据类型的数据和字符串做拼接运算，结果都为字符串
		- 10 + ‘abc'  # '10abc'
~~~

##### 2.比较运算符

**>    <    <=    >=    !=  == ===** 

* == 值相等，数据类型可以不等
* === 全等 恒等 值相等，数据类型也相等

##### 3.逻辑运算符

**&&  || ！**

* &&  与  and
* ||  或  or
* ！  非  not

##### 4.赋值运算符

**=  +=   -=   *=  /=   %= ++ --**  

```javascript
a=10; //10
a+=10; //20
a*=10; //200
a/=2; //100
a%=3; //1
```

~~~javascript
var age =18;

// var age2 = age++;//age2=18,先取age的值，然后age取自增
var age3 = ++age;//age3=19

前置和后置的区别
   · 在没有赋值操作，前置和后置是一样的。但在赋值操作时，如果递增或递减运算符前置，
   · 那么前置的运算符会先累加或累减再赋值，如果是后置运算符则先赋值再累加或累减。
~~~



##### 5.三目运算符

**表达式1 ? 表达式2 : 表达式3**

```javascript
var a = prompt("请输入第一个数字");
var b = prompt("请输入第一个数字");
var max = a > b ? a : b;
console.log(max);
```





#### 4.分支判断

* 顺序执行结构
  * 最基本的程序设计思路。顺序程序执行是按照语句出现的顺序一步一步从上到下运行，直到最后一条语句。从总体上看，任何程序都是按照语句出现的先后顺序，被逐句执行。
  * 所有的程序首先它是一个顺序执行结构
* 选择执行结构
  * 通过对条件（或表达式）的判断来选择执行不同的程序语句。

##### 1.if

> if(布尔表达式true/false){代码块}
>
> if(布尔表达式){代码块1}else{代码块2}
>
> if(布尔表达式1){代码块1}else if(布尔表达式2){代码块2}...else{代码块}
>
> 注意：在判断真假时：[null，0，NaN，“”，undefined]都被视为false处理
>
> && || ！ （与  或  非）

```javascript
1.如果张浩成绩 大于 90分，就奖励一个苹果
练习:
	 从prompt输入四位数的卡号，若卡号的四位数之和大于20，那么输出 “此用户为幸运客户"。
2.如果张浩成绩 大于90分，就奖励一个苹果，否则就奖励一个 笔记本。
3.对学生结业考试成绩测评：
   成绩>=80:良好
   成绩>=60:中等
   成绩<60:差 
4.举行百米赛跑。跑进11s的进入决赛，进入决赛的人员分为男子组和女子组。
```

##### 2.switch..case

```
1.电话快捷键。如果是1 打电话给父亲，2 打电话给母亲， 3 打给爷爷，4 打给奶奶，没有其他快捷键。
2.根据用户输入月份，显示对应的季节（例如：3,4,5为春季）
```



#### 5.循环

##### 循环四部分

~~~javascript
1.循环变量初始化
2.循环判断条件
3.循环体
4.迭代部分（循环步进/循环变量增加或减少处理）

~~~



##### 1.while

> ##### 语法：
>
> while(表达式) {
>    //代码块 循环体 + 循环步进
> ​	
> }
```javascript
1.输出1-100内每个整数。
2.输出1-100内能被7整除的整数。
```

##### 2.do.. while

> 写法和while一致，只是即使第一次while判断都不对，也会执行一次do中的逻辑

![1567480373005](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567480373005.png)

~~~javascript
  var count1 = 1;
    do {
        console.log(count1);
        count1++;
    }while(count1 <= 100);
~~~



##### 总结：

​	* 当循环条件满足时，do—while与while的执行结果一样；
​	* 但是当循环条件一开始就不满足时，do--while还是会执行一次，但是while一次也不会执行

##### 3.for

> ##### 语法：
>
>    for(表达式1;表达式2;表达式3) {
>        //代码段  循环体
>    }
>     表达式1：初始化变量
>     表达式2：循环判断条件
>     表达式3：循环步进
>
> ![1567480554605](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567480554605.png)
```javascript

for(var i=1;i<=10;i++){
  console.log(i);
}
1.练习：计算1-100的偶数和以及奇和
```

##### 4.break&continue

* break：用于跳出循环，退出循环结构

* continue：用于跳过循环中的当次循环


~~~javascript

1.依次打印输出1-10数字，打印输出到5 则停止，后续不再输出。
2.依次打印输出1-10数字，但是不包含5。
~~~



##### 5.循环嵌套

~~~javascript
循环内部嵌套循环
完成九九乘法表
~~~









#### 6.函数

##### 概念&作用

~~~javascript
函数概念：
   函数是由一系列语句构成的代码块，主要用于完成特定的功能。如果把函数比作一台机器的话，那么每个机器的作用各不相同，比如，爆米花机器，放入玉米出来的是爆米花。
 
函数的作用：
   函数需要的作用是为了方便编程，提高程序的重复利用率；方便调试程序，方便维护。一个功能，可以分解成若干的函数，提高程序的开发效率以及程序代码的利用率。 

~~~

##### 函数分类

* 系统内置函数
  * parseInt() parseFloat() 
* 自定义函数

##### 1.基本语法

> 	function 函数名(参数1,参数2){
> ​		...
> ​		return ...
> }

~~~javascript
function test(){
	alert("hello");
}
// 函数调用 
test();
~~~

##### 2.参数分类

* 形参：在函数定义时，函数名后面的变量
* 实参：调用时，函数名后面的参数
* **JavaScript语言的特殊之处：不检查实参的类型，不检测形参的个数**

```javascript

function test3(name,gender){
    if(gender){
    	return "Mr "+name+",hello!";
    }else{
   		return "Ms "+name+",hello!"
    }
}
test3(‘houqn’,'female');
```

* 如果当前多个实参，具体数量不详，可以使用 arguments对象来进行监听
  * JavaScript 函数有一个名为 arguments 对象的内置对象
  * arguments的length属性返回调用程序传递给函数的实际参数数目

~~~javascript
x = sumAll(1, 123, 500, 115, 44, 88);

function sumAll() {
    var i, sum = 0;
    for (i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
   	console.log(sum);
}
~~~

##### 3.return作用

* 函数到此结束

* 函数的值通过该语句往外传递结果

* 注：若没有return返回值时，返回undefined


##### 4.函数作用域

* 作用域：**作用域指的是您有权访问的变量集合。**

* 作用域分类

  * 全局作用域

    * 全局变量：函数之外声明的变量，会成为*全局变量*。能够被页面中（以及窗口中）的所有脚本和函数使用和修改。
    * 在 HTML 中，全局作用域是 window。所有全局变量均属于 window 对象

  * 局部/本地作用域

    * 每个函数创建一个新的作用域

    * 局部变量：只能用于其被定义的函数内部。对于其他函数和脚本代码来说它是不可见的。

    * 函数参数也是函数内的局部变量。


##### 5.递归

函数本身调用，跟循环类似

案例：使用递归计算1-100的和，求阶乘，斐波那契数列

##### 6.匿名函数

没有名字的函数

```javascript  半天完结
var fn = function(a,b){ //定义匿名函数，并赋值给一个变量
			alert(a+" -- "+b)
		}
fn(18,"houqn") //调用

//自执行函数
(function(i,j){
       return i + j;
   })(2,3);
```

##### 7.js执行顺序

~~~javascript
Hoisting 是 JavaScript 将所有声明提升到当前作用域顶部的默认行为（提升到当前脚本或当前函数的顶部）
注：
1.在加载整个HTML界面时，只要遇到script标签，那么就会优先执行预编译以及执行，会阻塞之后（html代码，css代码）的代码；等script标签执行完成，在执行之后的代码 
2. Js代码最好放在body底部，或者是使用onload等事件；加载外部的js最好放在body的底部，避免阻塞html界面。

~~~

##### 8.变量提升

~~~python
<script>
  var a=18;//全局变量，定义之后，整张页面有效
  function abc(){
    b="c115";//全局变量，定义之后，整张页面有效（声明时没有使用“var”关键字）
    var c = true;//局部变量，定义之后，仅方法内部有效
    ...
  }
  abc();
  console.log(c);
  console.log(b);
</script>
//注意在局部位置定义变量，如果不写"var",则变量成为全局变量
~~~

##### 9.闭包

##### **变量的生命周期**

* 全局变量活得和您的应用程序（窗口、网页）一样久。

* 局部变量活得不长。它们在函数调用时创建，在函数完成后被删除。


**9.1 想使用变量来计数，并且希望此计数器可用于所有函数。可以使用全局变量和函数来递增计数器：**

~~~javascript
// 初始化计数器
var counter = 0;

// 递增计数器的函数
function add() {
  counter += 1;
}

// 调用三次 add()
add();
add();
add();

// 此时计数器应该是 3
~~~

**注意：页面上的任何代码都可以更改计数器，而无需调用 add()。**



**9.2 add() 函数，计数器应该是局部的，以防止其他代码更改它：**

~~~javascript
// 初始化计数器
var counter = 0;

// 递增计数器的函数
function add() {
  var counter = 0; 
  counter += 1;
}

// 调用三次 add()
add();
add();
add();

//此时计数器应该是 3。但它是 0。
~~~

**注意：它没有用，因为我们显示全局计数器而不是本地计数器。**

**9.3 通过让函数返回它，我们可以删除全局计数器并访问本地计数器：**

~~~javascript
// 递增计数器的函数
function add() {
  var counter = 0; 
  counter += 1;
  return counter;
}

// 调用三次 add()
add();
add();
add();

//此时计数器应该是 3。但它是 1。
~~~

**注：它没有用，因为我们每次调用函数时都会重置本地计数器。**

**9.4 使用嵌套函数**

~~~javascript
function add() {
    var counter = 0;
    function plus() {counter += 1;}
    plus();     
    return counter; 
}
~~~

这样即可解决计数器困境，如果我们能够从外面访问 plus() 函数。

还需要找到只执行一次 counter = 0 的方法。

**9.5 使用闭包**

~~~javascript
var add = (function () {
    var counter = 0;
    return function () {return counter += 1;}
})();

add();
add();
add();

// 计数器目前是 3 

~~~

add 成为了函数。它能够访问父作用域中的计数器。

被称为 JavaScript *闭包*。它使函数拥有“*私有*”变量成为可能

计数器被这个匿名函数的作用域保护，并且只能使用 add 函数来修改。

闭包指的是有权访问父作用域的函数，即使在父函数关闭之后。



#### 7.内置对象

JavaScript 开发人员将常用的功能封装到固定对象

##### 1.数组

~~~javascript
值的有序集合，可以存放多个数据。
数组中的每一个值叫做元素。每一个元素都有自己的位置，这个位置叫做索引。索引是从0开始的
~~~

##### 数组特点

~~~javascript
ECMAScript是一种由Ecma国际（前身为欧洲计算机制造商协会，European Computer Manufacturers Association）通过ECMA-262标准化的脚本程序设计语言。这种语言在万维网上应用广泛，它往往被称为JavaScript或JScript，所以它可以理解为是JavaScript的一个标准
~~~

~~~javascript
数组是没有类型的；
同一个数组中可以存储相同类型或不同类型的数据；
ECMAScript语言中数组的长度是可以动态变化的；
Array是ECMAScript中常用的引用类型之一。
~~~

##### 数组创建

~~~javascript
1.构造函数法
	- var arr = new Array(10,20,30);  //创建一个数组 里面存放数据 10 20 30
	- var arr1  = new Array(); //空数组
	- var arr2 = new Array(3); //创建一个存储3个数据的数组。
		- 最后一个元素之后不要添加逗号
		- 使用构造函数方法创建时，可以省略new关键字。
2.字面量
	- var arr = [10,20,30]; //创建包含3个数据的 数组。末尾元素不要添加逗号，否则在IE8以及之前显示数组个数为4个。
	- var arr1 = []; //空数组
~~~

##### 数组元素操作

~~~javascript
1.访问
	- 数组[下标/索引]
		- 索引从0开始，之后的自然数。
2.修改
	- 数组[下标] = 新值
3.增加
	- 数组[下标] = 值
	- 数组的length属性非常有特点--他不是只读的。可以通过数组的length属性向数组的末尾扩大数组的容量，或者从数组末尾移除数组元素。
4.删除
	- 数组.length = 值

~~~

##### 数组遍历

~~~javascript
1.for循环
	for (var i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
2.for in循环
	for (var i in arr) {
        console.log(arr[i]);
    }
~~~

##### 数组常用方法

![1567566987279](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567566987279.png)

##### 数组排序

~~~javascript
1.冒泡排序
基本思想：在要排序的一组数中，对当前还未排好序的范围内的全部数，自上而下对相邻的两个数依次进行比较和调整，让较大的数往下沉，较小的往上冒。即：每当两相邻的数比较后发现它们的排序与排序要求相反时，就将它们互换
~~~

~~~javascript
var arr = [9,4,7,3,1,6,2,5,8];
for (var i = 0; i < arr.length - 1; i++) {
    for (var j = 0; j < arr.length - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            	var temp;
            	temp = arr[j];
            	arr[j] = arr[j+1];
            	arr[j+1] = temp;
            }
    }
}
~~~

~~~javascript
2.选择排序
每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。

~~~

~~~javascript
var arr = [9,4,7,3,1,6,2,5,8];
for (var i = 0; i < arr.length - 1; i++) {
    for (var j = i + 1; j < arr.length; j++) {
        if (arr[i] > arr[j]) {
            	var temp;
            	temp = arr[j];
            	arr[j] = arr[i];
            	arr[i] = temp;
            }
    }
}
~~~



#### 2.字符串

~~~javascript
基本认识：
	- var s1 = 'abc'; // string 基本类型
	- var s2 = new String('abcd'); //字符串对象 引用类型
长度概念。length
~~~

##### 字符串常用方法

| 方法                          | 描述                                   |
| --------------------------- | ------------------------------------ |
| str.charAt(n)               | 获取字符串str中指定索引位置的字符                   |
| str.charCodeAt(n)           | 获取字符串str中指定索引位置的字符对应的unicode码        |
| str.indexOf(s,[startindex]) | 获取字符串s在str中首次出现的位置，不存在返回值-1          |
| str.lastIndexOf(s)          | 获取字符串s在str中出现的位置，从后往前进行查找，不存在返回值为-1  |
| str.slice(n,m)              | 截取字符串str第n到m之间的字符串 也可为负数(IE8以及之前不支持) |
| str.substring(n,m)          | 截取返回字符串str第n到m之间的字符串,不接受负数           |
| str.substr(n,m)             | 截取字符串str从索引n开始的m个字符                  |
| str.split(s)                | 用字符串s将str分隔为一个数组                     |
| str.toLowerCase()           | 将字符串str转换为小写                         |
| str.toUpperCase()           | 将字符串str转换为大写                         |
| str.concat(s)               | 将字符串str和字符串s拼接                       |
| str.trim()                  | 去除字符串中前后空格（IE8以及之前不支持）               |

#### 3.Math对象

~~~javascript
ECMAScript 还为保存数学公式和信息提供了一个对象，即Math 对象
~~~

~~~javascript
属性：
Math.PI
方法：
min()和max()方法，求一组数中的最小值和最大值
         alert(  Math.min(1,2,3,4,6,12,3,44,5) );
         alert(  Math.max(1,2,3,4,6,12,3,44,5) );
舍入方法
         Math.ceil()执行向上舍入，即它总是将数值向上舍入为最接近的整数；
         Math.floor()执行向下舍入，即它总是将数值向下舍入为最接近的整数；
         Math.round()执行标准舍入，即它总是将数值四舍五入为最接近的整数； 
random()方法:Math.random()方法返回介于0 到1 之间一个随机数，包括0 不包括1。

~~~

#### 4.时间

~~~javascript
格林尼治时间（GTM），是英国郊区皇家格林尼治天文台的时间，因为地球自转的原因，不同经度上的时间是不相同的，格林尼治天文台是经度为0的地方。世界上发生的重大时间都是以格林尼治时间时间为标准的。
【例如】北京是东八区，时间比格林尼治时间快8个小时。比如格林尼治时间是1日0点，北京时间就是1日早8点。
世界协调时间（UTC），世界时间。1970年1月1日0点。
~~~

~~~javascript
ECMAScript 中的Date 类型是在早期Java日期基础上构建的。为此，日期类型使用UTC 
(Coordinated Universal Time，国际协调时间[又称世界统一时间]) 1970 年1 月 1 日
午夜(零时)开始经过的毫秒来保存日期。在使用这种数据存储格式的条件下，Date 类型
保存的日期能够精确到1970 年1 月1 日之前或之后的285616 年
~~~

##### 日期创建

~~~javascript
构造函数
date1 = new Date() // 创建当前时间日期对象
~~~

##### 日期格式化

~~~javascript
   alert(box.toString());   
   alert(box.toLocaleString());
   alert(box.toDateString()); //以特定的格式显示星期几、月、日和年
   alert(box.toTimeString()); //以特定的格式显示时、分、秒和时区
   alert(box.toLocaleDateString()); //以特定地区格式显示星期几、月、日和年
   alert(box.toLocaleTimeString()); //以特定地区格式显示时、分、秒和时区
   alert(box.toUTCString()); //以特定的格式显示完整的UTC 日期。
	
~~~



##### 日期时间获取/设置

~~~javascript
   alert(box.getFullYear()); //获取四位年份
   alert(box.setFullYear(2012)); //设置四位年份，返回的是毫秒数
   alert(box.getMonth()); //获取月份，没指定月份，从0 开始算起
   alert(box.setMonth(11)); //设置月份
   alert(box.getDate()); //获取日期
   alert(box.setDate(8)); //设置日期，返回毫秒数
   alert(box.getDay()); //返回星期几，0 表示星期日，6 表示星期六
   alert(box.setDay(2)); //设置星期几
   alert(box.getHours()); //返回时
   alert(box.setHours(12)); //设置时
   alert(box.getMinutes()); //返回分钟
   alert(box.setMinutes(22)); //设置分钟
   alert(box.getSeconds()); //返回秒数
   alert(box.setSeconds(44)); //设置秒数
   alert(box.getTime()) //获取某个日期自1970年以来的毫秒数
date1 = new Date(‘2019-1-1 17:00:00’) // 设置指定时间日期对象      
~~~

## 六、BOM

BOM 也叫浏览器对象模型，它提供了很多对象，用于访问浏览器的功能。**允许 JavaScript 与浏览器对话**

不存在浏览器对象模型（BOM）的官方标准。

现代的浏览器已经（几乎）实现了 JavaScript 交互相同的方法和属性，因此它经常作为 BOM 的方法和属性被提到。

##### WINDOW对象

~~~javascript

所有浏览器都支持 window 对象。它代表浏览器的窗口。

所有全局 JavaScript 对象，函数和变量自动成为 window 对象的成员。

全局变量是 window 对象的属性。

全局函数是 window 对象的方法。
~~~

~~~javascript
编程人员可以利用window对象控制浏览器窗口的各个方面，如改变状态栏上的显示文字、弹出对话框、移动窗口的位置等。
对window对象的属性和方法的引用，可以省略“window.”这个前缀
~~~

##### window对象常用方法

| **名称**                          | **说明**               |
| ------------------------------- | -------------------- |
| alert(提示信息)                     | 显示包含信息的对话框           |
| confirm(提示信息)                   | 显示一个确认对话框，包含一个确认取消按钮 |
| prompt(提示信息)                    | 弹出提示信息框              |
| open()                          | 打开具有指定名称的新窗体         |
| setTimeout(调用的函数func,等待的毫秒数ss)  | 等待ss毫秒后，调用func函数     |
| clearTimeout(ID)                | 清除定时器                |
| setInterval(调用的函数func,间隔的毫秒数ss) | 每隔ss毫秒数，调用func函数     |
| clearInterval(ID)               | 清除定时器                |

![1567569315708](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567569315708.png)



##### location对象

location提供了与当前窗口中加载的文档有关的信息，还提供了一些导航功能。location对象是window 对象的属性又是document 对象的属性，所有window.location 和document.location指同一个对象

| **属性名称**     | **说      明**              |
| ------------ | ------------------------- |
| **host**     | **返回主机名**                 |
| **hostname** | **返回当前URL的主机名**           |
| **href**     | **返回完整的URL**              |
| **pathname** | **返回URL中的目录或文件名**         |
| **port**     | **返回URL中的端口号，无则返回空字符串**   |
| **protocol** | **返回页面使用的协议**             |
| **search**   | **返回URL的查询字符串，这个字符串以？开头** |

| **方法名称**      | **说      明**    |
| ------------- | --------------- |
| **reload()**  | **重新加载当前文档**    |
| **replace()** | **用新的文档替换当前文档** |
| **assign()**  | **加载新的url**     |

##### history对象

history对象中保存着用户上网的历史记录，从窗口打开的那一刻起。因为history是window对象的属性，所以每个浏览器窗口或者每个框架，都有自己的history对象与特定的window对象关联

![1567569562422](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567569562422.png)



## 七、DOM

~~~javascript
DOM（Document Object Model）即文档对象模型。js可以操作html文档。
DOM 有三个等级，分别是DOM1、DOM2、DOM3，并且DOM1 在1998 年10 月成为
W3C 标准。DOM1 所支持的浏览器包括IE6+、Firefox、Safari、Chrome 和Opera1.7+。
PS：IE 中的所有DOM 对象都是以COM 对象的形式实现的，这意味着IE 中的DOM
	可能会和其他浏览器有一定的差异
~~~

#### 1.节点

W3C 的 HTML DOM 标准，HTML 文档中的所有内容都是节点。

~~~javascript
整个文档是一个文档节点
每个 HTML 元素是元素节点（标签节点）
HTML 元素内的文本是文本节点
每个 HTML 属性是属性节点
注释是注释节点
…
一切都是节点
~~~

##### 1.1 节点层级

当网页被加载时，浏览器会创建页面的文档对象模型（*D*ocument *O*bject *M*odel）。

*HTML DOM* 模型被结构化为*对象树*：

![1567663844135](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567663844135.png)

~~~javascript
html 标签没有父辈，没有兄弟，所以html 标签为根标签。head 标签是html 子标签，meta 和title 标签之间是兄弟关系。如果把每个标签当作一个节点的话，那么这些节点组合成了一棵节点树。
~~~



##### 1.2 获取元素节点

> - `document.getElementById("ID")`   
> - `document.getElementsByTagName("标签名")`
> - `document.getElementsByName("name属性值")` IE9以及之前版本，只对表单元素起作用
> - `document.getElementsByClassName("abc")`不适用于IE8以及之前版本
> - `document.querySelectorAll("p.intro")`不适用于 Internet Explorer 8 及其更早版本
> - 补充：`document.forms` ==选取页面中所有form的快捷方式
> - document.body - 文档的 body
> - document.documentElement - 完整文档

##### 1.3 元素节点层级属性

![1567673126660](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567673126660.png)

##### 1.4 节点相关属性

* nodeName 属性规定节点的名称
  * nodeName 是只读的
  * 元素节点的 nodeName 等同于标签名
  * 属性节点的 nodeName 是属性名称
  * 文本节点的 nodeName 总是 #text
  * 文档节点的 nodeName 总是 #document
* nodeValue属性
  * 元素节点的 nodeValue 是 undefined
  * 文本节点的 nodeValue 是文本文本
  * 属性节点的 nodeValue 是属性值
* nodeType属性 
  * 返回节点类型

![1567673162950](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567673162950.png)



#### 2.属性节点操作

> - 点语法
> - setAttribute(属性,属性值) IE8以及之前版本不支持
> - getAttribute(属性名)
> - removeAttribute(属性名)

```javascript
var ele = document.get....('xx');

ele.value="new_value"; //多用于设置文本框的显示内容
ele.name="new_name";
ele.href="new_href"; //可用于修改a标签的链接地址
ele.src="new_src"; //可用于修改img标签的图片

ele.checked=true/false;//适用于radio-button 和 checkbox标签
ele.selected=true/false;//适用于select内的option标签、
ele.disabled=true/false;//禁用标签，多用于按钮
sel = document.getElementById("lang"); //选中select
ops = sel.children;//获取所有的option
ops[1].selected=true; //将第二个option选中
<input type="button" value="click_me" disabled="true"/>

ele.className="a";//修改标签的class属性值，要使用className;为标签更换css样式类  <div class="b">

ele.innerHTML="平文、HTML代码"; //设置标签体中的内容 (html标签+文本内容)
```

**案例：点击按钮 进行改版**

**案例：form表单点击按钮 打印输出表单中内容**

**案例：表格选择**

![1567673403068](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567673403068.png)



![1567673415668](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567673415668.png)

![1567673469213](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567673469213.png)

#### 3.CSS样式操作

> - 设置css样式: 元素节点.style.样式 = 样式值

```javascript
ele.style.height="50px"; //单独修改标签的某一项css属性.
ele.style.backgroundColor="#abcdef";//单独修改标签的某一项css属性. 修改的属性为‘background-color’

```

#### 4.元素节点的增删改查操作

> - createElement()：创建节点
> - createTextNode():创建文本节点
> - appendChild()：追加孩子节点
> - insertBefore(new,old): 插入新节点在某个节点之前
> - cloneNode()：复制节点
> - removeChild()：移除子节点
> - remove()：移除节点 DOM4的规范，浏览器支持不友好。
> - replaceChild(new,old) 替换节点

**案例：动态表格操作**

![1567673846588](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1567673846588.png)

#### 5.DOM动画

~~~javascript
#container {
    width: 400px;
    height: 400px;
    position: relative;
    background: yellow;
}
#animate {
    width: 50px;
    height: 50px;
    position: absolute;
    background: red;
} 
~~~



~~~javascript
function myMove() {
    var elem =  document.getElementById("animate"); 
    var pos = 0;
    var id = setInterval(frame, 5);
     function frame() {
        if (pos ==  350) {
             clearInterval(id);
        } else {
             pos++; 
             elem.style.top = pos + 'px'; 
             elem.style.left = pos + 'px'; 
        }
     }
}
~~~





## 七、事件

HTML DOM 允许 JavaScript 对 HTML 事件作出反应。

#### 1.事件注册

> 事件注册方式一：定义函数myClick , 并在标签的事件中设置属性：onclick="myClick()"

```javascript
function myClick(){
	alert("button clicked~")
}
<input type="button"  onclick="myClick();"  value="click_me"/>
```

事件注册方式二：脚本模型 

~~~javascript

<input type="button" value="click_me"/>
var btn = document.getElementsByTagName('input')[0];
btn.onclick = function(){
	alert("button clicked~")
}
~~~

**注：多次绑定同一事件，会发生覆盖**

##### **1.可用事件**

| 事件名             | 事件描述                     |
| :-------------- | ------------------------ |
| **onclick**     | 单击时触发                    |
| **ondblclick**  | 双击时触发                    |
| **onfocus**     | 获得焦点时触发                  |
| **onblur**      | 失去焦点时触发                  |
| **onchange**    | 内容改变且焦点失去时触发，多用于select标签 |
| **onmouseover** | 鼠标指针移入时触发一次              |
| **onmousemove** | 鼠标指针在内部移动时，不断触发          |
| **onmouseout**  | 鼠标指针移出时触发一次              |
| **onload**      | 用于body标签，在整个页面加载完毕时触发    |

##### 2.事件对象

代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。

> 在 **onclick="myClick(event)"**  传入参数 **'event'** 
>
> 在事件函数中接收参数 **function myClick( event )**

```javascript
<script>
  	function myClick(event){ //event = 接收事件对象 ，从onclick="myClick(event);"中传来
		alert("button clicked~")
		console.log(event)
        var e = event;
		console.log(e.type) //事件类型
		console.log(e.clientX) //事件触发x坐标
		console.log(e.clientY) //事件触发x坐标
		console.log(e.target || e.srcElement)  //事件源-触发事件的标签
		
	}
</script>
<input type="button" onclick="myClick(event);" value="click_me"/>
```

#### 2.事件冒泡

~~~javascript
事件流是描述的页面接受事件的顺序（事件传播方式），当几个都具有相同事件的元素层叠在一起的时候，那么你点击其中一个元素，并不是只有当前被点击的元素会触发事件，而层叠在你点击范围的所有元素都会触发事件。事件流包括两种模式：冒泡和捕获。
事件冒泡，是从里往外逐个触发。
事件捕获，是从外往里逐个触发。
那么现代的浏览器默认情况下都是冒泡模型。捕获模式则是早期的Netscape 默认情况。而现在的浏览器要使用DOM2模型的事件绑定机制才能手动定义事件流流模式。

~~~



```javascript
function myClick(event){
	alert("button clicked~")
    
	event.stopPropagation();//标准属性
    //IE属性
    //e.cancelBubble=true;
}
function myClick2(){
	alert("div clicked~~")
}
<div onclick="myClick2()">
   <input type="button" onclick="myClick(event);" value="click_me"/>
<div>
```

> 事件的冒泡，不会因为事件源没有该事件，而不冒泡；也不会因为某个中间的父标签没有该事件而停止冒泡。
>
> 注意：当父元素和子元素都有某一个事件，且需要独立执行时，冒泡会使得事件同时执行，所以需要防止

#### 3.常用技巧

> 为超链接注册单击事件，需要阻止其href

```html
function click9(){
    .....
}
<a href="javascript:void(0)" onclick="click9();">go~</a>
```

> form表单提交前，如果需要处理其他逻辑
>
> 先将提交按钮改为普通按钮，然后在按钮事件中手动提交表单。即可实现灵活的表单控制！

```html
function submit9(){
    ....逻辑处理...
    document.forms[0].submit();//手动获取from，并提交
    //document.getElementById("ff").submit();
}
<form .... id="ff">
	.....
	<input type="button' onclick="submit9();" value="提交"/>
</form>
```

```javascript
<form action="http://www.baidu.com" method="get">
  <input type="text" name="usermae"><br/>
  <input type="text" name="password"><br/>
  <input type="button" value="提交" id="btn">
</form>
<script type="text/javascript">
  //1.获取按钮
  var btn115 = document.getElementById("btn");
	//2.注册事件
  btn115.onclick=function(){
    console.log('form submit');
    document.forms[0].submit();
  }
</script>
```

~~~javascript
阻止默认行为：比如 点击表单中 submit，自动提交表单。
function someHandle(event) {
      event = event || window.event;
      if(event.preventDefault){
         event.preventDefault();
      }else{
         event.returnValue = false;
      }
   }
或者 使用 return false
function someHandle(event) {
    		   return false;    
}

~~~



#### 4.补充

~~~javascript
目前推荐绑定事件方式：DOM2事件模型
为指定元素指定事件处理程序，为元素附加事件处理程序而不会覆盖已有的事件处理程序。
优势：
	- 能够向一个元素添加多个事件处理程序。
	- 能够向一个元素添加多个相同类型的事件处理程序
	- 更容易控制事件传播方式。

	标准浏览器：addEventListener()
                                                             							       addEventListener("eventType","handler","true/false")
                   eventType：指事件类型，注意不要加‘on’前缀
                   第二个参数是处理函数
                   第三个使用事件冒泡，还是事件捕获。可选，默认false
   IE浏览器：
          attachEvent( eventType,handler);
       				eventType：事件类型，需要添加前缀on，例如：onclick
       				handler:事件处理函数

~~~

