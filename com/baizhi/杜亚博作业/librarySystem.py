# Version2.0
# 非结构化编程---》 结构化编程  函数

# 项目： 启动函数   初始化函数   管理器函数

def initDataBase():
    pass

def login():
    pass

def regist():
    pass

def welcome():
    print('***********欢迎来到飞哥图书管理系统************')
    while 1:
        r=input('1.登录 2.注册 3. 修改密码')
        if r=='1':
            login()
        elif r=='2':
            regist()
        elif r=='3':
            pass
        else:
            print('输入有误请重新输入')


def manager(): # 管理器函数：用于系统整体调配
    # 1. 加载数据库
    initDataBase()
    # 2. 启动项目---欢迎界面
    welcome()

def start(): # 程序的入口  run start  main
    manager()




