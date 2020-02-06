# 字典
#1
# a={'a':12,'y':121,'t':116,'h':104,'o':111,'n':110}
# print(a)

#2
# 不对，集合也是花括号

#3
# 会把这个键值对添加到字典里

#4
# 字典的检查效率高，hash算法，直接查找hash缓存表找到对应下标，获取键值对

#5
#键必须是可哈希的，不可变类型

#6
# a=dict()
# print(a.fromkeys((1, 2, 3), ('one', 'two', 'three')))
# print(a.fromkeys((1,3),'数字'))
# {1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
# {1: '数字', 3: '数字'}

#7
# 第一个是dict(**kwargs)：使用命名关键字参数创建字典
# 第二个变量={键1：值1，键2：值2，...}
# 第三四五个是dict(iterable)：使用可迭代对象创建字典

#8
# d1={'one':1,'two':2,'three':3}
# d2=dict(d1)
# d2=d1
# print(d2)

#9
# d1=dict()
# print('____欢迎进入通讯录程序____\n____1:查询联系人资料____\n____2:插入新的联系人____\n____3:删除已有联系人____\n____4:退出同学录程序____')
# while 1:
#     n=int(input('请输入相关指令:'))
#     if n==1:
#         #查询
#         name=input('请输入联系人姓名')
#         if name not in d1:
#             print('没有改用户')
#         else:
#             print(name+':'+d1[name])
#     elif n==2:
#         name=input('请输入联系人姓名')
#         if name in d1:
#             print('你输入的姓名在通讯录中已存在---')
#             print(name + ':' + d1[name])
#             n1=input('是否修改用户资料(yes/no):')
#             if n1=='yes':
#                 num = input('请输入用户联系电话')
#                 d1[name]=num
#         else:
#             num = input('请输入用户联系电话')
#             d1.update({name:num})
#     elif n==3:
#         #删除
#         name = input('请输入联系人姓名')
#         if name not in d1:
#             print('没有该用户')
#         else:
#             d1.pop(name)
#     else:
#         #退出
#         exit()


#10
# d1={'du':123}
# def found():
#     global d1
#     name=input('请输入用户名')
#     while name in d1:
#         name=input('此用户名已经使用，请重新输入')
#     pwd=int(input('请输入密码'))
#     d1.update({name:pwd})
#     return d1
# def goin():
#     global d1
#     name=input('请输入用户名')
#     pwd = int(input('请输入密码'))
#     if d1[name]==pwd:
#         print('登录成功')
#     else:
#         print('用户名不存在或密码错误')
# while 1:
#     print('____新建用户:N/n____\n____登录账号:E/e____\n____退出程序:Q/q____\n')
#     a=input('请输入指令:')
#     if a=='n' or a=='N':
#         found()
#     elif a=='E'or a=='e':
#         goin()
#     else:
#         exit()


#集合
#1
#1. 无序 2. 是可迭代对象 3. 不是序列 4. 是可变类型

#2
#frozenset(): 创建不可变空集合

#3
#用len()

#4
# s=set([1,2,3,4,5])
# print(s[0])
#报错 集合不支持索引

#5
# s={[1,2]}
# print(s) 报错 集合的元素不能是可变类型的
# s=set([1,2])
# print(s) 可以创建

#6
#结果是1

#7
# add（value）： 向集合增加一个元素
# clear()：清空集合 2. pop():随机删除一个元素 3. remove（value）: 删除指定元素



