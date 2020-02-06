# def f1():
#     a=[1,2]
#     return a
# a=[1,2]
# a.append(f1()[1]+f1()[0])
# print(a)
# def f1(s,t,m,n):
#     if n==1:
#         print('%s-->%s'%(s,t))
#     else:
#         #n-1 a-->c
#         f1(s,m,t,n-1)
#         #a-->b
#         print('%s-->%s'%(s,t))
#         #n-1 c-->b
#         f1(m,t,s,n-1)
# f1('a','b','c',3)


# def f1(n):
#     if n==1:
#         n=0
#         return 0
#     elif n==2:
#         n=1
#         return 1
#     else:
#         n=f1(n-2)+f1(n-1)
#         return n
# n=int(input('asd'))
# for i in range(1,n+1):
#     print(f1(i),end=' \t')

# class A():
#     a=1
#     b=2
# s1=A()
# s1.a=3
# s2=A()
# print(s1.a,s2.a)
# A.a=5
# print(s1.a,s2.a)
# A.b=6
# print(s1.b,s2.b)


# def fun(s):
#     global start
#     start=time.time()
#     return s
#
# @fun
# def main():
#     for i in range(10000):
#         print('hello')
#     end=time.time()
#     print(end-start)
# main()


# def fun(s):
#     global start
#     start=time.time()
#     def f2():
#         for i in range(10000):
#             print('hello')
#         end = time.time()
#         print(end - start)
#     return f2
#
# @fun
# def main():
#     pass
# main()

# class Plug:
#     def __init__(self):
#         self.methods=[]
#     def plugIn(self,obj):
#         for method in self.methods:
#             obj.__dict__[method.__name__]=method
#     def plugOut(self,obj):
#         for method in self.methods:
#             del obj.__dict__[method.__name__]
# class A(Plug):
#     def __init__(self):
#         super().__init__()
#         self.methods.append(self.p)
#     def p(self):
#         print('ppppp')
# class B:
#     pass
# a=A()
# b=B()
# a.plugIn(b)
# b.p()

# def f(a):
#     print(a)
#     def f1(f):
#         print('f1f1')
#         return f
#     return f1
# @f('aa')
# def a():
#     print('a')
# a()

# class F1():
#     def __init__(self,f):
#         self.f=f
#     def __call__(self, *args, **kwargs):
#         print('f1')
#         return self.f()
# @F1
# def a():
#     print('aaa')
# a()
# import time
# class Fun:
#     def __init__(self,f):
#         self.f=f
#     def __call__(self):
#         start=time.time()
#         self.f()
#         print(time.time()-start)
#         return
# @Fun

# import threading
# import queue
# import random
# import time
# l=[]
# def send(name,q):
#     while 1:
#         n=random.randint(1,1000)
#         q.put(n)
#         print('{}说:这是数字{}'.format(name,n))
#         r=q.get()
#         l.append(r)
#         time.sleep(2)
# def rec(name):
#     count=0
#     while 1:
#         r=l[count]
#         print('{}收到: 这是数字{}'.format(name,r))
#         count+=1
#         time.sleep(1)
#         # time.sleep()
# if __name__=='__main__':
#     q=queue.Queue()
#     t1=threading.Thread(target=send,args=('老王',q),daemon=True)
#     t2=threading.Thread(target=send,args=('老赵',q),daemon=True)
#     t3=threading.Thread(target=send,args=('老钱',q),daemon=True)
#     t4=threading.Thread(target=rec,args=('老王',),daemon=True)
#     t5=threading.Thread(target=rec,args=('老赵',),daemon=True)
#     t6=threading.Thread(target=rec,args=('老钱',),daemon=True)
#
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t5.start()
#     t6.start()
#
#     time.sleep(7)

# def zhi():
#     count=99
#     while 1:
#         count += 1
#         f=0
#         for i in range(2,int(count**0.5)+1):
#             if count%i==0:
#                 f=1
#         if f==0:
#             yield count
# a=zhi()
# while 1:
#     print(next(a))
