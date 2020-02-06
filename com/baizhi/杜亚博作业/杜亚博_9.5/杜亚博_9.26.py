# count=0
# card=0
# totalMoney=0
# def shuaka():
#     n=random.randint(0,500)
#     global totalMoney
#     totalMoney+=n
#     for i in range(n):  # 一个人的 第几次
#         global card
#         card+=1
#         time.sleep(0.01)
#         print('%s刷卡1元,现在余额为：%s'%(getName(),card))
#
# l=[]
# for i in range(10):  #循环10次 创建了10个线程代表10个认
#     count+=1
#     l.append(threading.Thread(target=shuaka))
#
# for i in l: #ｉ：　每一个线程对象
#     i.start()
#
# for i in l:
#     i.join()
#
# print(totalMoney)


import threading
import random
# n=random.randint(0,1000)
# n1=1000-n
# def jinchangA():
#     for i in range(n):
#         print('{}号同学从前们进场'.format(random.randint(100000,999999)))
# def jinchangB():
#     for i in range(n1):
#         print('{}号同学从前们进场'.format(random.randint(100000,999999)))
# t1=threading.Thread(target=jinchangA)
# t2=threading.Thread(target=jinchangB)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print('{}个同学从前面进入，{}个同学从后门进入'.format(n,n1))


# import time
# def sus(n):
#     if n==1:
#         return False
#     elif n==2:
#         return True
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return False
#         else:
#             return True
#
# def su(a,b):
#     for i in range(a,b):
#         if sus(i):
#             time.sleep(0.001)
#             print('{}是素数'.format(i))
# t1=threading.Thread(target=su,args=(1,2500000))
# t2=threading.Thread(target=su,args=(2500000,5000000))
# t3=threading.Thread(target=su,args=(5000000,7500000))
# t4=threading.Thread(target=su,args=(7500000,1000001))
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
