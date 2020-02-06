#1
#1. 提高代码的可维护性
# 2. 减少代码冗余
# 3. 提高程序的可重用性
# 4. 提高代码的灵活性

#2
# 1. 形式参数：在函数定义处，出现的参数 简称：形参‐‐‐Parameter
# 2. 实际参数：函数调用处，出现的参数（传入的参数） 简称：实参‐‐‐Argument

#3
#def

#4
#global

#5
#nonlocal

#6
#传入参数时位置不一致 导致参数错误

#7
#关键字字参数是相对于实参 参数传值和位置无关
#默认参数是相对于形参 当没有传入参数是 使用默认值

#8
#不行 ，return只能返回一个值

#9
#两个参数 参数是列表形式

#12
# Hello World!
# hello python

#13
#只输出  outside

#14
# def outside():
#     var = 5
#     def inside():
#         print(var)  把print和var对换
#         var = 3
#     inside()
# outside()

#15

#funout()

#funOut()()

#16
# def funX():
#     x=5
#     def funY():
#         nonlocal x
#         x += 1
#         return x
#     return funY
# a = funX()
# print(a())
# print(a())
# print(a())
# 6
# 7
# 8

#17
# print((lambda x,y=3:x*y)(2))

#18
# def f1(x):
#     if x%2:
#         return x
#     else:None
# print(f1(4))

#19
# n=int(input('输入一个整数n'))
# def f1(n):
#     for i in range(1,n):
#         if n%i==0:
#             print(i)
# f1(n)

#20
# n=int(input('输入一个整数n'))
# def f1(n):
#     for i in range(n):
#         print('Helloworld?')
# f1(n)

#21
n=input('输入一个整数n')
def f1(n):
    print(str(len(n))+'位')
f1(n)