#1
# SyntaxError 语法错误

#2
#下标越界 IndexError

#3
#属性错误 AttributeError

#4
#KeyError

#5
# SyntaxError

#6
# NameError

#7
#
# UnboundLocalError

#8
# try-except 之类的语句来处理异常

#9
# 可以， 因为异常有多种 多个except可以捕捉多个异常

#10
#自定义异常类 直接或间接继承BaseException
#except捕捉一切异常
#except（异常1，异常2.。。）

#11
#不建议 可读性极差 出现异常后 不清楚是那种异常 不好维护

#12
#用finally关闭文件

#13
# try:
#     for i in range(3):
#         for j in range(3):
#             if i==2:
#                 raise KeyboardInterrupt
#             print(i,j)
# except KeyboardInterrupt:
#     print('退出了')

#14


# def in_input():
#     a=input('输入整数')
#     try:
#         a=int(a)
#         print(a)
#     except:
#         print('输入的不是整数')
# in_input()


#15
#出现NameError
# try:
#     f=open('my.txt')
#     print(f.read())
# except OSError as reason:
#     print('出错了'+str(reason))
# finally:
#     try:
#         f.close()
#     except NameError as e :
#         print(e)