import com.baizhi.图书管理系统Version_4.systems.book_system.booksys as booksys
import com.baizhi.图书管理系统Version_4.systems.user_system.usersys as usersys
import com.baizhi.图书管理系统Version_4.yichang.yichangs as yichang
import pickle
import threading
# 创建数据库
f=open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\book.db','rb')
bookDB=pickle.load(f)  # 反序列化    将二进制文件转化成Python对象
f.close()
f=open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\user_db','rb')
userDB=pickle.load(f)  # 反序列化    将二进制文件转化成Python对象
f.close()


class Manager:
    # 打印欢迎界面
    def welocme(self):
        print('*********欢迎来到飞哥图书馆************')

    # 获取用户登录或注册
    def getUserInput(self):
        return input('1.登录  2.用户管理')
    def findN(self,name):
        for i in userDB.userBianli():
            if i.name==name:
                break
        else:
            print('没有该用户')
    # 登录
    def login(self):
        name = input('name:')
        t1 = threading.Thread(target=self.findN, args=(name,),daemon=True)
        t1.start()
        pwd = input('pwd:')
        for i in userDB.userBianli():
            if i.name == name and i.pwd == pwd:
                print('登录成功')
                return True
        print('用户名密码错误')
        return False

    def mainPage(self):
    # 展示管理系统界面
        print('+++++++++++进入主页面++++++++++++++',end='\n')
        return input('1.查看书籍信息\n2.查找书籍\n3.增加一本书籍\n4.修改一本书\n5.删除一本书\n6.返回登录界面')

    # 注册
    # 修改密码
    # 展示管理系统界面
    # 查询书籍
    # 修改书籍
    # 添加书籍
    # 删除书籍
    # 退出系统
    # 管理程序（操作系统）
    def dengLuXC(self):
        #登录线程
        if self.login():
            # self.librarySystem()
            while 1:
                r = self.mainPage()
                try:
                    if r == '1':
                        # 查看书
                        for i in bookDB.bianLi():
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    elif r == '2':
                        n = input('1.根据类型查询 2.根据作者查询 3.书名查询 4.价格查询')
                        booksys.Select(n, bookDB)
                    elif r == '3':
                        # 添加书籍
                        print('请输入书的信息')
                        bookDB.add(booksys.InputBook().getBook())
                        f = open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\book.db', 'wb')
                        pickle.dump(bookDB, f)
                        f.close()
                    elif r == '4':
                        # 修改书籍
                        n = int(input('输入修改书籍的id'))
                        bookDB.modify(n)
                        f = open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\book.db', 'wb')
                        pickle.dump(bookDB, f)
                        f.close()
                    elif r == '5':
                        # 删除书籍
                        n = input('1.id删除 2.书名删除 3.作者删除')
                        bookDB.remove(n)
                        f = open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\book.db', 'wb')
                        pickle.dump(bookDB, f)
                        f.close()
                    elif r == '6':
                        # 返回登录界面
                        break
                    else:
                        raise yichang.PrintError('输入有误，请重新输入')
                except yichang.PrintError as e:
                    print(e)
    def zhuCeXC(self):
        #注册线程
        print('输入个人信息')
        userDB.add(usersys.ZhuCe().getUser())
        f = open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\user_db', 'wb')
        pickle.dump(userDB, f)
        f.close()
    def xiuGaiXC(self):
        #修改线程
        usersys.ExchangePwd(userDB)
        f = open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\user_db', 'wb')
        pickle.dump(userDB, f)
        f.close()
    def geRenXC(self):
        #修改个人信息线程
        usersys.ExchangeUser(userDB)
        f = open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\user_db', 'wb')
        pickle.dump(userDB, f)
        f.close()
    def manager(self):
        #欢迎界面
        self.welocme()
        while 1:
            try:
                #用户输入登录界面
                r = self.getUserInput()
                if r == '1':
                    # 登录
                    t=threading.Thread(target=self.dengLuXC)
                    t.start()
                    t.join()
                elif r=='2':
                    r=input('1.注册 2.修改密码 3.查看修改个人信息')
                    if r == '1':
                        # 注册
                        t = threading.Thread(target=self.zhuCeXC)
                        t.start()
                        t.join()
                    elif r == '2':
                        # 修改密码
                        t = threading.Thread(target=self.xiuGaiXC)
                        t.start()
                        t.join()
                    elif r=='3':
                        #修改个人信息
                        t = threading.Thread(target=self.geRenXC)
                        t.start()
                        t.join()
                else:
                    raise yichang.PrintError('输入错误 请重新输入')
            except yichang.PrintError as e:
                print(e)
    def run(self):
        self.manager()

