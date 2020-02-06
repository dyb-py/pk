# Python基础语法

* 输出函数

~~~markdown
print() ：向控制台打印数据
1. print(*objects,sep=' ',end='\n',file=sys.stdout,flush=False)
		*objects: 可以传入多个数据
		sep：分割符号  （当传入多个数据时生效）
		end：结尾符号   
		file：文件流
		flush： 设置缓冲区
2. print函数，可以如何使用：
		1. 打印一个数据
		2. 打印多个数据
		3. 打印表达式的结果
~~~

* 输入函数

~~~markdown
input（）： 从控制台获取用户输入的数据
1. input（pompt=None）：
		pompt：在获取用户数据之前，显示提示信息（没有类型限制）
2. input会将获取的数据，以字符串的形式进行返回
3. input在执行时，会等待用户数据数据，用户输入完毕（出发了回车）之后才会继续运行
		这种行为称之为：阻塞
~~~

* 变量

~~~markdown
1. 没有默认值
2. 先定义后使用
3. 变量中存储的是数据的首地址
4. 变量名，要符合标识符命名规范
~~~

* 标识符命名规范

~~~markdown
标识符： 和名字相关的

1. 语法规范：
		1. 合法标识符：数字（数字不能开头），字母，下划线
		2. 大小写敏感
		3. 不能使用关键字和保留字：
			1. 关键字：Python中内置的，具有特殊含义的字符，且这些字符不可更改
			if else  for while and or not True False class def assert as with is yield pass 
			2. 保留字：Python中预制使用的函数名，方法名，类名等字符，是可以被修改的
			print  input  type zip next  iter  int str bool dict float set list tuple frozenset 
		4. 没有长度限制
		
2. 开发习惯：
		1. 望文生义
		2. 大小写：
			1. 包名：全小写
			2. 类名：大驼峰
			3. 函数名/变量名/方法名：小驼峰
			4. 常量：全大写
			5. 其他命名：单词和单词之间用下划线连接（单词全小写）
						hello_world
			
注： 驼峰命名法： 单词首字母大写，其他字母小写
			HelloWorld：大驼峰
			helloWorld：小驼峰
~~~

---

* 数据类型

~~~markdown
Python是没有类型的概念， Python只有一种类型： 对象类型   整型对象：1  字符串对象：‘呵呵’ 浮点型对象：1.5

1. 整型： int
		1  2  3 
2. 浮点型： float
		1.5  
		科学计数法，也是浮点型
		1.23e+8
		浮点数，是由定点整数和定点小数构成的
			定点整数：  1.
			定点小数：  .5
		如何存储：通过两个slot分别存储两个定点数
3. 布尔型：bool  
		True:1
		False:0
		任何非零:True 
		任何零:False   []  ''  0  
4. 字符串：str
		1. 字符串天生具有跨平台特性
		2. 分类：
			1. 单引号字符串
			2. 双引号字符串
			3. 三印号字符串
		3. 字符串的嵌套使用
			"Let's Go"
5. 空值： None
6. 其他复杂数据：
		list：列表
		dict:字典
		tuple：元组
		set：集合
		frozenset：不可变集合
		pipe：管道
		queue:队列
~~~

* 数据类型转换

~~~markdown
1. 要转换成谁，就用谁
2. 数据之间转换要兼容
~~~

~~~python
a=123
b=str(a)
print(b,type(b))
c=float(a)
print(c,type(c))

a='123'
print(int(a))
# print(int('hehe'))

print(float('1.5'))
# print(float('1.5.'))
print(float('1.'))
print(int('1.'))
~~~

* 获取类型信息的方式

~~~markdown
1. type（obj）： 本质是一个类
		返回obj参数的类型
2. isinstance（obj，class）：  本质是一个函数
		判断obj是不是class类型的
~~~

~~~python
a=10
print(type(a))
print(isinstance(a,int))
~~~

---

* 表达式

~~~markdown
定义：变量和字面值用某个式子（运算符）连接的模式
字面值：变量类型所指代的值  
a=10   #10是int的字面值   
‘呵呵’ # ‘呵呵’是str的字面值 
~~~

* 运算符

~~~markdown
1. 一般运算符：
		+ - * /(真除法) % ** //（地板除法）直接去掉小数点之后的数
        幂运算：一元运算符
2. 赋值运算：
		=  
		a=10 # 把10的首地址复制给a
         b=a  # 把a中存储的地址赋值给b
         a=b=c=10 # 连续赋值
         a=10
         b=20
         换值： a,b=b,a
		增强赋值运算：
		+= -= *= /= %= **= //=
		a=a+1  : 执行效率低：线程安全的操作：加了锁
		a+=1   : 执行效率高：线程不安全的操作：没加锁
3. 布尔运算符（比较运算符）
		> < >= <= == !=
		a>b>c  # a>b and b>c 
4. 逻辑运算符：
		and or not
5. 三元运算符：
		（值1 if 布尔值 else 值2）
		如果布尔值为真，返回值1，反之返回值2
~~~

* 优先级

~~~markdown
1. 四则运算：
		先乘除，后加减
		（）：括号 可以干预优先级
2. 元和优先级的关系
		元数越多，优先级越低
		幂运算优先级较高
		三元运算符优先级较低
3. 逻辑运算符优先级：
		not > and > or
~~~

---



















