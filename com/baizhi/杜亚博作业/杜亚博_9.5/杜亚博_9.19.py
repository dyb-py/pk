#7
#可以将一个类更加真实的模拟成一个属性

#8
#__get__()
#__set__()
#__delete__()

#13
#super()

#23
# 当设置一个属性时，会调用该方法，
#不正确 return super().__setattr__(name,value+1)
        # self.__dict__[name]=value+1
#24
# 3
# 2
# None


#25
#2
#1
#报错

#26
#没有count属性

#27
# class MyDes:
#     def __get__(self, instance,owner):
#         print("getting...")
# class Test:
#     a = MyDes()
#     x = a
# test = Test()
# test.a

# 都会输出getting

#28
# class MyDes:
#     def __init__(self, value = None):
#         self.val = value
#     def __get__(self, instance,owner):
#         return self.val - 20
#     def __set__(self, instance,value):
#         self.val = value + 10
#         print(self.val)
# class C:
#     x = MyDes()
# if __name__ == '__main__':
#     c = C()
#     c.x = 10
#     print(c.x)
#20
#10

#29
#Mydes实例对象

#38
# class F:
#     def __get__(self, instance, owner):
#         instance.t=instance.t*1.8+32
#         return instance.t
# class fun:
#     def __init__(self,t):
#         self.t=t
#     a=F()
# a1=fun(32)
# print(a1.a)

#40
# class F:
#     def __getattr__(self, item):
#         print('该属性不存在')
# a=F()
# a.name

#41
# class MyDes:
#     def __init__(self,value,x):
#         self.value=value
#         self.x=x
#     def __get__(self, instance, owner):
#         print('正在获取变量:x')
#         print(self.value)
#     def __set__(self, instance, value):
#         print('正在修改变量:x')
#         self.value=value
#     def __delete__(self, instance):
#         print('噢 这个没办法删除')
# class Test:
#     x=MyDes(10,'x')
# text=Test()
# y=text.x
# text.x=8
# del text.x
# text.x

#42
# i=0
# while i<=4:
#     print(i)
#     i+=1

#45
# class F:
#     def __init__(self):
#         self.a='FishC'
#     def __get__(self, instance, owner):
#         print(self.a)
#     def __set__(self, instance, value):
#         self.a=value
#         print(self.a)
# class Demo:
#     x=F()
# demo=Demo()
# demo.x
# demo.x='X-man'
# demo.x
