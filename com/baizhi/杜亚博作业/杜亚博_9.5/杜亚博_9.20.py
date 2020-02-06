#2
#实现了__iter__()  __next__()方法的对象，称为迭代器

#3
#迭代器是一个特殊的可迭代对象 迭代器的迭代器时本身，
# 容器 ： 支持存储多种数据，存储多个数据 支持成员关系符

#4
#该容器实现了 __iter__()  __next__()方法 print(iter(容器))打印的是一个迭代器

#5
#当获得StopIterationg时

#6
#集合

#14
# class A:
#     pass
# class B:
#     pass
# class C(A):
#     pass
#
#
# print(C.__bases__)
# C.__bases__+=(B,)
# print(C.__bases__)

#16
# __getattribute__()

#17
#字符串 列表 元组

#18
#__setitem__()

#19
# __reversed__()

#20
# __len__()

#32
# @staticmethod
#33
# 静态方法 可以没有任何参数
# 一般用于编辑工具方法

#37
# class A:
#     def __init__(self,*args):
#         self.l=args
#         n=len(self.l)
#         if n==0:
#             print('没有传入参数')
#         else:
#             print('传入了'+str(n)+'个参数,分别是',end=' ')
#             print(*self.l)
#
# a=A(1,2,3,4)

#42
# a=iter(range(5))
# while 1:
#     try:
#         print(next(a))
#     except:
#         break

#43
# class LeapYear:
#     def __init__(self):
#         self.l=[]
#         for i in range(2019,1999,-1):
#             if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
#                 self.l.append(i)
#         self.a=iter(self.l)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return next(self.a)
# a=LeapYear()
# for i in a:
#     if i>=2000:
#         print(i)
#     else:
#         break

#44
# class MyRev:
#     def __init__(self,s):
#         self.s=s[::-1]
#         self.a=iter(self.s)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return next(self.a)
# m=MyRev('ADW')
# for i in m:
#     print(i,end=' ')

#50
# class CountList:
#     def __init__(self, *args):
#         self.values = [x for x in args]
#         self.count = [0 for i in args]
#     def __len__(self):
#         return len(self.values)
#     def __getitem__(self, item):
#         self.count[item]+=1
#         return self.values[item]
#     def counter(self,index):
#         print(self.count[index])
#     def append(self,s):
#         self.values.append(s)
#         self.count.append(0)
#     def pop(self,index):
#         self.values.pop(index)
#         self.count.pop(index)
#     def remove(self,obj):
#         self.count.pop(self.values.index(obj))
#         self.values.remove(obj)
#     def insert(self,index,obj):
#         self.values.insert(index,obj)
#         self.count.insert(index,0)
#     def clear(self):
#         self.values.clear()
#         self.count.clear()
#     def reverse(self):
#         self.values.reverse()
#         self.count.reverse()
# a=CountList(1,2,3)
# a[1]
# a[2]
# a[1]
# a.counter(1)
# a.reverse()
# a.counter(2)
# a.insert(3,'a')
# a[3]
# a.counter(3)
# print(a.values)
# print(a.count)