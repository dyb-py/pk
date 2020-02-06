#1
# 魔法方法，会自动被调用，不需要手工调用
# 魔法方法修改，会影响原有类或对象，类或对象的修改，也会影响魔法方法
# 魔法方法是Python的一切
#9
# __new__()

#10
#需要初始化数据的时候

#11
#不会触发

#12
# 当对象在加号右端：不具有主动性
# 当对象在加号左边： 具有主动性
# 当加号左边的对象，是数据时，没有任何方法，则此时主动性会后置，加法后面的对象具有主动性 #
# 此时加号后面的对象，会触发反运算
#15
#__add__()


#21
#
# class A:
#     def a(self):
#         self.a = "hehe"
#         return self.a
# a=A()
# print(a.a())
# print(a.a)
# 实例属性和方法重名 实例属性将方法名覆盖


#22
# class Test:
#     def __init__(self,x,y):
#         return x+y
# __init__()应该return None

#30
# 1. 不需要手工调用，在创建对象时，自动调用
# 2. new方法的返回值是对象，当前类创建的实例对象
# 3. 创建对象时第一个调用的方法是new方法
# 4. 调用完new之后，在new的内部会自动调用init init是new方法调用的
# 5. 一般不建议修改new方法

#31
# 对象被垃圾回收机制回收时，被自动调用
# del a   del只是删除了引用，并没有删除对象， 真正删除对象的是垃圾回收机制

#34
# +  __add__()
# # - __sub__()
# # *  __mul__()
# # /  __truediv__()
# # //  __floordiv__()
# # % __mod__()
# # ** __pow__()
# # <<  __lshift__()
# # >>  __rshift__()
# # &  __and__()
# # ^  __xor__()
# # |  __or__()

#35
#说明python的多态性
#方便 简单 可以传任意值

#36
# class A:
#     def __init__(self,*args):
#         pass
#     def __new__(cls, *args, **kwargs):
#         n=len(args)
#         print(n)
# a=A(1,2,3,4,5,6,'a','b')

#39
# class World(str):
#     def __init__(self,n):
#         self.n=n
#     def __lt__(self, other):
#         s=0
#         for i in self.n:
#             if i!=' ':
#                 s+=1
#             else:
#                 break
#         o = 0
#         for i in other.n:
#             if i != ' ':
#                 o += 1
#             else:
#                 break
#         if s<o:
#             return True
#         if s==o:
#             return '相等'
#         if s>o:
#             return False
#
# a=World('asd a')
# b=World('sadwd SD')
# print(a<b)

#46
# class Fu(int):
#     def __new__(cls,n):
#         if type(n)!=str:
#             n=int(n)
#         else:
#             b=0
#             for i in n:
#                 b+=int(ord(i))
#             n=b
#
#         return super().__new__(cls,n)
# a=Fu('aa')
# print(a)


#47
# class Nstr(str):
#     def __init__(self,n):
#         self.n=n
#     def __sub__(self, other):
#         if other.n in self.n:
#             return self.n.replace(other.n,'')
#         else:
#             return '无法-'
# a=Nstr('hello world')
# b=Nstr('world')
# print(a-b)

#48
# class Nstr(str):
#     def __init__(self,n):
#         self.n=n
#     def __lshift__(self, other):
#         self.n=self.n[other:]+self.n[:other]
#         return self.n
#     def __rshift__(self, other):
#         other=0-other
#         self.n = self.n[other:] + self.n[:other]
#         return self.n
# a = Nstr('Hello World')
# print(a>>3)
# a = Nstr('Hello World')
# print(a<<3)


#49
# class Fu(int):
#     def __new__(cls,n):
#         if type(n)!=str:
#             n=int(n)
#         else:
#             b=0
#             for i in n:
#                 b+=int(ord(i))
#             n=b
#         return super().__new__(cls,n)
#     # def __add__(self, other):
# a=Fu('Hello')
# b=Fu('World')
# print(a-b)
# print(a+b)
# print(a*b)
# print(b//a)
# print(b/a)