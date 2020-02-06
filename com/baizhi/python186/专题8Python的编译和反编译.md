# Python的编译和反编译

* Python的运行机制

~~~markdown
.py源文件---编译器---.pyc（字节码文件）---PVM

1. 源文件：
		程序员直接编辑的文本文件
		接近自然语言，有固定的语法规范
2. 编译器：
		compiler
		将源文件转换成字节码文件
		作用：1. 检测语法规范 2. 预加载：加载部分类，加载函数，预运算    3. 提高虚拟机执行效率  
3. 字节码文件：
		本质：是一个二进制文件
		1. 提高虚拟机执行效率
		2. 不可以直接被编辑
		3. 符合虚拟机执行通用指令
4. PVM：
		1. 在不同的平台，有不同的虚拟机实现
		2. 可以执行相同的字节码文件
		3. 向操作系统发送请求
~~~

* Python涉及的文件

~~~markdown
1. .py  
		源代码文件，可以直接被Python的解释器运行
		可以直接被文本编辑器所编辑
2. .pyc 
		1. 是由py文件经过编译后生成的二进制字节码文件（byte code）
		2. 加载速度快于py文件
		3. 可以跨平台（依托于虚拟机）
		4. 和Python的版本相关（不同的Python版本，字节码不同）
3. .pyo
		应用于嵌入式
		Python3.5后.pyo文件：***.opt-n.pyc
4. .pyd
		Python的动态链接库
		动态链接库：.DLL 文件 程序运行的方法库
		.pyd文件的本质就是.dll文件，仅仅换了一个后缀
		一般使用的语言：C语言，C++，D语言
		.pyd文件是Python的动态模块
5. .pyz
		Python3.5开始 .pyz  .pyzw文件
		.pyz: python 的zip应用
		.pyzw: 在windows系统中的 zip应用		
~~~

* Python的编译过程

~~~markdown
windows：dos指令
mac： 终端

创建字节码文件：
1. 进入到源代码目录
2. 键入指令： python -m py_compile 文件名.py
		默认在当前目录下创建文件夹： __pycache__
		在__pycache__目录下，有字节码文件：
		文件名.cpython-版本.pyc

运行字节码文件：
1. 进入字节码文件目录
2. 键入指令： python 字节码文件名.后缀

创建.pyo文件： python3.5以后没有pyo文件
1. 进入到源代码目录
2. 2. 键入指令： python -O -m py_compile 文件名.py
~~~

* 反编译

~~~markdown
展示虚拟机指令

指令： python -m dis 文件名.py
~~~

---

