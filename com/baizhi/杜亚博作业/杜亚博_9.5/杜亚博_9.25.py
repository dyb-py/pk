#1
#第二种

#2
#默认是 'r'只读
#  r    | 只读           |      |
# | rb   | 以二进制格式只读     |      |
# | r+   | 读写           |      |
# | rb+  | 以二进制格式读写     |      |
# | w    | 只写---重写（覆盖写） |      |
# | wb   | 以二进制格式只写     |      |
# | w+   | 读写           |      |
# | wb+  | 以二进制格式读写     |      |
# | a    | 追加写          |      |
# | ab   | 以二进制格式追加写    |      |
# | a+   | 读写           |      |
# | ab+  | 以二进制格式读写

#3
#将python对象转换成二进制文件 也叫序列化

#4
# pickle.dump()

#5
#pickle.load()

#6
#不能保存

#7
#以二进制格式只写  ‘x’如果文件存在，则不可覆盖（报错），不存在，创建新文件
#8
# readlines（）
# 读取每一行字符串，并打包成列表返回（包括换行符）

#9
# 关闭资源
# I/O流在计算机中是重要的资源，资源有限
# 开启一个流后，要及时进行关闭（资源的释放）

#10
#用 read()或者readlines()

#11
# size=10 表示设置读取的字符数为10

#12
# tell()方法
# 13
# import os.path as path
# print(path.split(r'F:\pywork\com\baizhi\python186\hehe.mp3')[-1])
# 14
# import os
# os.rename(r'F:\pywork\com\baizhi\python186\hehe.mp3',r'F:\pywork\com\baizhi\python186\hehe.txt')
#15
# p=input('请输入文件名:')
# with open(p,'a')as f:
#     print('''请输入内容【单独输入':w'】保存退出''')
#     n=0
#     while 1:
#         n=input()
#         if n!=':w':
#             f.write(n)
#             f.write('\n')
#         else:
#             break

#16
# p1=input('请输入需要比较的头一个文件名:')
# p2=input('请输入需要比较的另一个文件名:')
# f1=open(p1,'r')
# f2=open(p2,'r')
# o1=f1.readlines()
# o2=f2.readlines()
# if len(o1)>len(o2):
#     l=len(o2)
# else:
#     l=len(o1)
# count=0
# a=[]
# for i in range(l):
#     if o1[i]!=o2[i]:
#         a.append(i+1)
#         count+=1
# print('两个文件一共有{0}处不同:'.format(count))
# for i in a:
#     if i:
#         print('第{0}行不一样'.format(i))
# f1.close()
# f2.close()

#17
# p=input('请输入要打开的文件:')
# n=int(input('输入显示前几行：'))
# print('文件{0}的前{1}行的内容如下：'.format(p,n))
# with open(p,'r') as f:
#     a=f.readlines()
#     for i in range(n):
#         print(a[i])

#18
# p=input('请输入要打开的文件:')
# n=input('输入显示文件行数的范围：')
# count=0
# for i in n:
#     count+=1
#     if i==':':
#         break
# n1=int(n[0:count-1])
# n2=int(n[count:])
# print('文件{0}的第{1}行到第{2}的内容如下：'.format(p,n1,n2))
# with open(p,'r') as f:
#     a=f.readlines()
#     for i in range(n2):
#         if i+1>=n1 and i+1<=n2:
#             print(a[i])
#19
# p=input('输入文件名')
# with open(p,'r')as f:
#     a=f.readlines()
#     n=input('请输入需要替换的单词或字符')
#     n1=input('请输入新的单纯或字符')
#     count=0
#     for i in a:
#         s=i.count(n)
#         count+=s
#     print('文件{0}一共有{1}个[{2}]'.format(p,count,n))
#     l=[]
#     for i in a:
#         l.append(i.replace(n,n1))
# na=input('你确定要把{}换成{}吗\n[yes/no]'.format(n,n1))
# if na=='yes':
#     with open(p,'w')as f:
#         for i in l:
#             f.write(i)
# else:
#     pass

#20
# import os.path as path
# import os
# l=os.listdir()
# l1=[]
# for i in l:
#     l1.append(path.splitext(i)[1])
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# for i in l2:
#     print('该文件下共有的类型为{0}的文件{1}个'.format(i,l1.count(i)))
#

#21
# import os.path as p
# import os
# l=os.listdir()
# for i in l:
#     print('{0}[{1}Bytes]'.format(i,p.getsize(i)))

#22
# import os
# import os.path as p
# n=input('请输入待查找的初始目录:')
# n1=input('请输入需要查找的目标文件:')
# if p.isfile(n):
#     print('该路径是文件 不是目录')
#     exit()
# def f(a,b):
#     a1=os.listdir(path=a)
#     #返回当前目录下的文件
#     for i in a1:
#         #查看所有文件
#         if i==b:
#             #找到文件
#             print(p.join(a,i))
#         elif  not p.isfile(p.join(a,i)):
#             #不是文件 是文件夹 则递归调用f(当前文件夹，目标文件)
#             f(p.join(a,i),b)
#         else:
#             #其他文件 pass
#             pass
# f(n,n1)



import os
import os.path as p
n=input('请输入待查找的初始目录:')
n1=input('请输入需要查找的关键字:')
if p.isfile(n):
    print('该路径是文件 不是目录')
    exit()
def f(a,b):
    a1=os.listdir(path=a)
    #返回当前目录下的文件
    for i in a1:
        #查看所有文件
        if  not p.isfile(p.join(a,i)):
            print(p.join(a,i))
            #不是文件 是文件夹 则递归调用f(当前文件夹，关键字)
            f(p.join(a,i),b)
        else:
            with open(p.join(a,i),'r',encoding='utf-8')as f1:
                l=f1.readlines()
                f2=0
                for i in l:
                    if b in i:
                        f2=1
                if f2==1:
                    print('在文件{0}找到关键字{1}'.format(p.join(a, i), b))
                    c=0
                    for i in l:
                        c+=1
                        if b in i:
                            print('关键字出现在第{0}行 位置[{1}]'.format(c,i.index(b)+1))

f(n,n1)
