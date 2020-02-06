# class Rect:
#     def __init__(self,l=0,w=0):
#    #初始化长和宽
#         self.l=l
#         self.w=w
#     def area(self):
#      #求面积
#         return self.l*self.w
#     def __setattr__(self, key, value):
#         if key=='square':
#             self.l=self.w=value
#         else:
#           #设置其他属性
#             super().__setattr__(key,value)
#
# a=Rect(2,3)
# a.square=10
# print(a.area())


# class A:
#     '''
#     HHHHHH
#     '''
#     age=10
#     def __init__(self,name='aaa'):
#         self.name=name
# a=A()
# print(A.__dict__)
# print(a.__dict__)
# # A.__dict__['age']=20
# a.__dict__['name']='adwada'
# print(a.name)
# print(a.__doc__)


# class A:
#     age=10
#     def __getattribute__(self, item):
 #          #调用父类的__getattribute__
#         print('aaaa')
#         return super().__getattribute__(item)
#         # return self.__dict__[item]
#     def __init__(self):
#         self.hh=100
#     def __setattr__(self, key, value):
#         #调用父类的__setattr__() 或者在__dict__中加入键值对
#         print('bbbbbbb')
#         return  super().__setattr__(key,value)
#         # self.__dict__[key]=value
# a=A()
# # a.age=20
# a.hh=21
# print(a.hh)



# class My:
#     def __init__(self,mget,mset,mdel):
#         self.mget=mget
#         self.mset=mset
#         self.mdel=mdel
#     def __get__(self, instance, owner):
#       #把实例对象传入mget
#         return self.mget(instance)
#     def __set__(self, instance, value):
#       #把实例对象和value传入mset
#         self.mset(instance,value)
#     def __delete__(self, instance):
#       把实例对象传入mdel
#         self.mdel(instance)
# class A:
#     def __init__(self,n=1):
#       #构造方法
#         self.n=n
#     def getN(self)
#         return self.n
#     def setN(self,value):
#         self.n=value
#     def delN(self):
#         del self.n
#       #设置描述符 把get set del 函数名传进My
#     x=My(getN,setN,delN)
# a=A()
# print(a.x)
# a.x=10
# print(a.x)
# del a.x
# print(a.x)



# class C:
#     def __init__(self):
#         self.value=25
#     def __get__(self, instance, owner):
#         return self.value
#     def __set__(self, instance, value):
#         self.value=value
#
#
# class F:
#     def __get__(self, instance, owner):
#         return instance.c*1.8+32
#     def __set__(self, instance, value):
#         instance.c=(value-32)/1.8
#
# class T:
#     c=C()
#     f=F()
# a=T()
# a.c=100
# print(a.f)
# a.f=100
# print(a.c)
