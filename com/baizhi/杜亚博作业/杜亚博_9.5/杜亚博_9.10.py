#22
# def f1(a,b):
#     c=a**b
#     print(c)
# a=int(input('输入底数'))
# b=int(input('输入幂'))
# f1(a,b)

#23
# def count(s):
#     n=len(s)
#     a,b,c,d=0,0,0,0
#     for i in range(n):
#         if s[i]==' ':
#             a+=1
#         elif s[i].isdigit():
#             b+=1
#         elif s[i].isalpha():
#             c+=1
#         else:d+=1
#     print(str(a)+'个空格  '+str(b)+'个数字  '+str(c)+'个字母  '+str(d)+'个字符')
#
# def f1(*a):
#     n=len(a)
#     for i in range(n):
#         print('第'+str(i+1)+'个字符串有：',end='')
#         count(a[i])
# f1('asd','asd','kjk23ad','asl jkw: 21#@!')

#24
# print(list(filter(lambda x: False if x % 3 else True, range(1, 101))))

#25
# def f1(a,b):
#     c=(a[0]-b[0])**2+(a[1]-b[1])**2
#     d=c**0.5
#     print(d)
# f1((1,2),(1,3))

#26
# def f1(a,b,c):
#     if (b**2-4*a*c)<0:
#         print('无解')
#     else:
#         x1=(-b+(b**2-4*a*c)**0.5)/2*a
#         x2=(-b-(b**2-4*a*c)**0.5)/2*a
#         print(x1,x2)
# f1(2,4,2)

#27
# def f1(a):
#     if a==1:
#         return 1
#     elif a==0:
#         return 0
#     else:
#         a=a*f1(a-1)
#         return a
# def f2(a):
#     if int(a)==f1(int(a[0]))+f1(int(a[1]))+f1(int(a[2])):
#         print(a)
# for i in range(100,1000):
#     a=str(i)
#     f2(a)

#28
# def f1(a):
#     if a%2==0:
#         a=a/2
#         print(a)
#         return f1(a)
#     elif a==1:
#         return 1
#     else:
#         a=a*3+1
#         print(a)
#         return f1(a)
# f1(281)

#29
# def f1(a):
#     x=int(a**0.5)
#     if x*x==a:
#         return True
# def f2(a,b):
#     if f1(int(a))and f1(int(b)):
#         if f1(int(a[0]+b[0]))and f1(int(a[1]+b[1])) and f1(int(a[2]+b[2])):
#             print(a,b)
# for i in range(100,1000):
#     for j in range(100,1000):
#         a=str(i)
#         b=str(j)
#         f2(a,b)

#30
# def f1(a):
#     sum=0
#     for i in range(1,a):
#         if a%i==0:
#             sum+=i
#     return sum
# for i in range(2,3001):
#     for j in range(i+1,3001):
#         if f1(i)==j and f1(j)==i:
#             print(i,j,)

#31
# def f1(a):
#     for i in range(2,int(a**0.5)+1):
#         if a%i==0:
#             return 0
#     return a
# def f2(a):
#     for i in range(2,a//2+1):
#         if f1(i)+f1(a-i)==a:
#             print(str(a)+'='+str(i)+'+'+str(a-i))
# f2(14)

#32
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
# f1('a','b','c',5)
def f1(n):
    if n==1:
        n=0
        return 0
    elif n==2:
        n=1
        return 1
    else:
        n=f1(n-2)+f1(n-1)
        return n
n=int(input('asd'))
for i in range(1,n+1):
    print(f1(i),end=' \t')

