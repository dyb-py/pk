# MixIn编程

~~~markdown
1. 是一种开发模式： 插件模式
2. mixin编程是一种将多个类中的功能单元进行组合使用的方式
~~~

* 组合

~~~python
# 1. 组合可以实现部分扩展功能
class A:
    age=18

class B:  # A扩展了B
    hehe=A()  #组合

b=B()
print(b.hehe.age)

~~~

* 继承

~~~python
class A:
    age=18
    def hehe(self):
        print('this is A hehe')

class C:
    def func(self):
        print('this is c')


class B(A,C):  # 继承： 父类扩展了子类
    pass

b=B()
print(b.age)
b.hehe()
print(b.func())
~~~

* __bases\_\_

~~~python
class  A:
    def methodA(self):
        print('A')

    def hehe(self):
        print('hehe')

class B:
    def methodB(self):
        print('B')

class C(A):
    pass

class D:
    def methodD(self):
        print('this is D')

c=C()
print(C.__bases__)  # 记录父类信息
C.__bases__+=(B,)   # 修改父类信息    本质继承
print(C.__bases__)

C.__bases__+=(D,)

c.methodA()
c.methodB()
c.methodD()

~~~

* 插件模式

~~~python
# 使用继承扩展子类：弊端：
# 插件模式的好处： 不需要继承关系，可以指定扩展的成员，随时使用，随时回收
class PlugIn:
    def __init__(self):
        self.methods=[]  # 创建一个仓库，用于存储别的类传进来的方法
    def plugIn(self,obj):
        # obj:被扩展对象
        for method in self.methods:
            obj.__dict__[method.__name__]=method

    def plugOut(self,obj):
        for method in self.methods:
            del obj.__dict__[method.__name__]

class A(PlugIn):
    def __init__(self):
        super().__init__() # 为了创建 列表
        self.methods.append(self.heheA)
        self.methods.append(self.heheA2)

    def heheA(self):
        print('heheA')

    def heheA2(self):
        print('heheA2')

class B(PlugIn):
    def __init__(self):
        super().__init__() # 为了创建 列表
        self.methods.append(self.heheB)

    def heheB(self):
        print('heheB')

class C:
    pass

a=A()  # 开启了A下的仓库，放入了heheA   A- 2个
b=B()  # 开一了B下的参数，放入了heheB   B- 1个
c=C()
a.plugIn(c) # 给c插入两个方法,A的heheA方法 heheA2
b.plugIn(c)

c.heheA()
c.heheA2()
c.heheB()
b.plugOut(c)
# c.heheB()
c.heheA()
~~~

