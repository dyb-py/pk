#列表
# 1.[2,9,7]

#2.
#[9,7]

#3.
#不一样 list1[0:1]返回的是 列表 [1] list1[0]返回的是1

#4.
# a=[1,3,2,7,5]
# n=len(a)
# for i in range(1,n):
#     for j in range(n-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

#5.
# a=[1,3,2,7,5]
# n=len(a)
# for i in range(n-1):
#     for j in range(i,n):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

#13
# a=list()
# n=int(input('输入N'))
# for i in range(n):
#     a.append(True)
# for j in range(2,n):
#     if a[j]==True:
#         for d in range(j+1,n):
#             if d%j==0:
#                 a[d]=False
# for c in range(2,n):
#     if a[c]==True:
#         print(c)


#元组

#1
# append()在最后增加一个元素
# extend()扩展列表
# count()计算并返回指定元素的数量
# remove()删除一个元素
# pop()删除并返回最后一个元素
# sort()排序（从小到大）
# insert()在指定位置插入一个元素
# copy()拷贝一个副本
# clear()清空所有元素
# reverse()原地反转所有的数据
# index()寻找并返回参数的索引值


#2
# a='c',('a',)
# print(a)
#有一个元素是元组时 逗号和括号必须同时存在

#3
#不是

#4
# a和c是列表
# b是元组

#字符串
#1.''' '''和\

#2.多行字符串 多行注释

#3.
#print('Hello World We are the best'[12:18]

#4.
#print('Hello World We are the best'[-15:-9])

#5.
#  %c 格式化字符串及其编码值
#  %s  格式化字符串
#  %d  格式化整数
#  %o  格式化无符号八进制数
#  %x  格式化无符号十六进制数
#  %X   大写同上
#  %e  用科学计数法格式化定点数
#  %g  根据值的大小决定使用%f或%e

#6
#print('{{1}}'.format('打印','不打印'))
# {1}

#7
# 关键字参数

#8
#位置参数




