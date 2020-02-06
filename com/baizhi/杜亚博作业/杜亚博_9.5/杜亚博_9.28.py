# def fib():
#     a,b=0,1
#     while 1:
#         a,b=b,a+b
#         yield a
# a=fib()
# n=int(input('输入n'))
# for i in range(n):
#     print(next(a))


# def f():
#     x=yield 1
#     print('x=%s'%x)
#     yield ('x=%s'%x)
# a=f()
# print(next(a))
# print(a.send('haha'))
