# def fun(d,*,a,b,c):# 只影响*号之后的参数
#     print(d,a,b,c)
#
# fun(100,a=1,b=2,c=3)


# print('*'.join(['a', 'b', 'c']))
#
# d={1:'one',2:'two',3:'three'}
# for i in d.keys():
#     print(i)
#
# for i in d.values():
#     print(i)
#
# for i in d.items():
#     print(i)



# l=['a']
# print(','.join(l))
# data = {
#     'db': 'test123',
#     'user': 'root',
#     'password': '123456',
#     'host': 'localhost',
#     'port': 3306,
#     'charset': 'utf8'}
#


# a=[[1,2],[2,3],[3,4]]
# print(a)
# print(*a)
#
# def fun(*a):
#     print(a)
#     print(*a)
# fun(1,2,3,4)
#
#
# def fun(**a):
#     # print(a)
#     print(*a)
#     print(a.values())
#
# fun(a=1,b=2,c=3)  # a=1,b=2,c=3 ---  {a:1,b:2,c:3} --- a=1 b=2 c=3

def funa(*a):
    print(a)

def funb(**a):
    print(**a)
    # funa(*a) # funa(1 2 3)

funb()
#
# def func(**a):
#     print(a)
#
# def fund(**a): # {a:1,b:2,c:3}
#     func(**a)  #func(a=1 b=2 c=3)
#
# fund(a=1,b=2,c=3)

# d={'one':1,'two':2,'three':3}
#
# print(d.setdefault('ones','hehe'))

# import configparser # 配置文件解析器模块
#
# # 创建解析对象（工具）
# cp=configparser.ConfigParser()
# # 加载配置文件
# cp.read(r'E:\Python186共享文件夹\第二阶段\code\day12_mysql的封装\config.ini',encoding='utf-8')
# # 解析数据
# print(cp.get('DATA', 'db'))




























