# 图书管理系统，3.0
# 先找对象  找方法
# 1. 用户  2. 书籍   3. 系统（管理者） 4. 数据库
class User:
    def __init__(self,ids=0,name='',pwd='',phone='',mail=''):
        '''
        :param ids:
        :param name:
        :param pwd:
        :param phone:
        :param mail:
        '''
        self.ids=ids
        self.name=name
        self.pwd=pwd
        self.phone=phone
        self.mail=mail

def ist(i):
    if '~' in i or '!' in i or '@' in i or '#' in i or '$' in i or '%' in i or '^' in i or '&' in i or '*' in i or '-' in i or '=' in i or '[' in i or ']' in i or '\\' in i or ';' in i:
        return True
    else:
        return False
class ZhuCe:
    #注册用户信息
    B=3
    def __init__(self):
        ZhuCe.B+=3
        self.name = input('输入name')
        while 1:
            self.pwd = input('输入密码')
            n = len(self.pwd)
            a, b, c = 0, 0, 0
            a1 = 0
            x = self.pwd[0]
            if x.isalpha():
                a1 = 1
            for j in self.pwd:
                if j.isdecimal():
                    a = 1
                if j.isalpha():
                    b = 1
                if ist(j):
                    c = 1
            if n <= 8 or a == 1 and b == 0 or a == 0 and b == 1:
                print('等级为低')
            if a + b + c == 2 and n >= 8:
                print('等级为中')
            if a + b + c == 3 and n >= 16 and a1 == 1:
                print('等级为高')
                break
            if self.pwd == '':
                print('密码不能为空')
            if a1 == 0:
                print('必须字母开头')
            for i in range(10):
                if self.pwd.startswith('{0}'.format(i)):
                    print('不能以数字开头')
            if n < 16:
                print('长度不够，不能少于16位')
            if a + b + c < 3:
                print('需要由数字，字母及字符三种组合')
        self.phone = input('输入电话')
        self.mail = input('输入邮箱')
        self.user = User(ZhuCe.B, self.name, self.pwd, self.phone, self.mail)

    def getUser(self):
        return self.user
class Book:
    def __init__(self,ids,name,author,price,category,desc):
        '''
        :param ids: 系统内部编号
        :param name: 书名
        :param author: 作者
        :param price: 价格
        :param category: 类别
        :param desc: 评价
        '''
        self.ids=ids
        self.name=name
        self.author=author
        self.price=price
        self.category=category
        self.desc=desc

class InputBook():
    #输入书籍信息
    def __init__(self):
        self.name = input('输入name')
        self.author = input('输入作者')
        self.price = float(input('输入价格'))
        self.category = input('输入类别')
        self.desc = input('输入评价')
        InputBook.A+=1
        self.book=Book(self.name,self.author,self.price,self.category,self.desc)
    def getBook(self):
        return self.book

class DataBase:
    def __init__(self):
        self.l=[]
    # 增加数据
    def add(self,obj):
        self.l.append(obj)
    # 修改数据
    def modify(self,ids):
        for i in self.l:
            if i.ids==ids:
                if isinstance(i,Book):
                    n=input('1.修改书名 2.修改作者 3.修改价格 4.修改类别 5.修改评价')
                    if n=='1':
                        i.name=input('输入书名')
                    elif n=='2':
                        i.author=input('输入作者')
                    elif n=='3':
                        i.price=float(input('输入价格'))
                    elif n=='4':
                        i.category=input('输入类别')
                    elif n=='5':
                        i.desc=input('输入评价')
    # 删除数据
    def remove(self,x):
        if x=='1':
            ids=int(input('输入id'))
            for obj in self.l:
                if obj.ids==ids:
                    self.l.remove(obj)
                    print('删除成功')
                    return
            print('没有该书籍')
        if x=='2':
            name=input('输入书名')
            for i in self.l:
                if i.name==name:
                    self.l.remove(i)
                    print('删除成功')
        if x=='3':
            a=input('输入作者')
            for i in self.l:
                if i.author==a:
                    self.l.remove(i)
                    print('删除成功')
    # 查询数据
    def select(self,ids):
        for i in self.l:
            if i.ids==ids:
                return i

    # 返回数据库的迭代器
    def __iter__(self):
        # return self.l.__iter__()
        return iter(self.l)

class Manager:  # 业务
    # 初始化数据库
    def __init__(self):
        self.userDB=DataBase()
        self.userDB.add(User(ids=1,name='xiaobo',pwd='123456'))
        self.userDB.add(User(ids=2,name='admin',pwd='123456'))
        self.userDB.add(User(ids=3,name='hehe',pwd='123456'))
        self.bookDB=DataBase()
        self.bookDB.add(Book(ids=1,name='三体',author='刘',price=29,category='科幻',desc='很好看'))
        self.bookDB.add(Book(ids=2, name='活着', author='余华', price=159, category='文学', desc='好看'))
        self.bookDB.add(Book(ids=3, name='斗破苍穹', author='土豆', price=299, category='小说', desc='一般'))

    # 打印欢迎界面
    def welocme(self):
        print('*********欢迎来到飞哥图书馆************')
    # 获取用户登录或注册
    def getUserInput(self):
        return input('1.登录  2. 注册  3. 修改密码')
    # 登录
    def login(self):
        name=input('name:')
        pwd=input('pwd:')
        for i in self.userDB:
            if i.name==name and i.pwd==pwd:
                return True
        return False
    def Select(self,x):
        #('1.根据类型查询 2.根据作者查询 3.书名查询 4.价格查询')
        if x=='1':
            print('书的类型有 1科普  2科幻  3励志小说 4科幻小说 5文学小说 6科学文献 7古典文学 8网络小说 9魔幻巨作\n ')
            n = int(input('请选择书籍类型\n'))
            if n == 1:
                for i in self.bookDB:
                    if i.category == '科普':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 2:
                for i in self.bookDB:
                    if i.category == '科幻':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 3:
                for i in self.bookDB:
                    if i.category == '励志小说':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 4:
                for i in self.bookDB:
                    if i.category == '科幻小说':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 5:
                for i in self.bookDB:
                    if i.category == '文学小说':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 6:
                for i in self.bookDB:
                    if i.category == '科普':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 7:
                for i in self.bookDB:
                    if i.category == '古典文学':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 8:
                for i in self.bookDB:
                    if i.category == '网络小说':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
            elif n == 9:
                for i in self.bookDB:
                    if i.category == '魔幻巨作':
                        print(i.ids,i.name,i.author,i.price,i.category,i.desc)
        if x=='2':
            n=input('输入作者姓名')
            for i in self.bookDB:
                if i.author==n:
                    print(i.ids,i.name,i.author,i.price,i.category,i.desc)
        if x=='3':
            n=input('输入书名')
            for i in self.bookDB:
                if i.name==n:
                    print(i.ids,i.name,i.author,i.price,i.category,i.desc)
        if x=='4':
            print('书的价格区间有 1. <=50  2. 50<<100  3. 100<<200 4. 200<< \n')
            n = int(input('选择价格区间\n'))
            if n == 1:
                for i in self.bookDB:
                    if i.price<=50:
                        print(i.ids, i.name, i.author, i.price, i.category, i.desc)
            elif n == 2:
                for i in self.bookDB:
                    if i.price>=50 and i.price<=100:
                        print(i.ids, i.name, i.author, i.price, i.category, i.desc)
            elif n == 3:
                for i in self.bookDB:
                    if i.price>=100 and i.price<=200:
                        print(i.ids, i.name, i.author, i.price, i.category, i.desc)
            elif n == 4:
                for i in self.bookDB:
                    if i.price>=200:
                        print(i.ids, i.name, i.author, i.price, i.category, i.desc)
            else:
                print('输入错误')
    def ExchangePwd(self):
        #修改密码
        name=input('name:')
        pwd=input('old pwd:')
        for i in self.userDB:
            if i.name==name and i.pwd==pwd:
                i.pwd=input('new pwd:')
                print('修改成功')
                return
        print('密码错误')
    #登陆成功后 界面
    def mainPage(self):
    # 展示管理系统界面
        print('+++++++++++进入主页面++++++++++++++',end='\n')
        return input('1.查看书籍信息\n2.查找书籍\n3.增加一本书籍\n4.修改一本书\n5.删除一本书\n6.退出系统\n')
    # 管理程序（操作系统）
    def manager(self):
        self.welocme()
        while 1:
            r=self.getUserInput()
            if r=='1':
                # 登录
                if self.login():
                    # self.librarySystem()
                    print('登录成功')
                    while 1:
                        r=self.mainPage()
                        if r=='1':
                            #查看书
                            for i in self.bookDB:
                                print(i.ids,i.name,i.author,i.price,i.category,i.desc)
                        elif r=='2':
                            n=input('1.根据类型查询 2.根据作者查询 3.书名查询 4.价格查询')
                            self.Select(n)
                        elif r=='3':
                            #添加书籍
                            print('请输入书的信息')
                            self.bookDB.add(InputBook().getBook())
                        elif r=='4':
                            #修改书籍
                            n=int(input('输入修改书籍的id'))
                            self.bookDB.modify(n)
                        elif r=='5':
                            #删除书籍
                            n=input('1.id删除 2.书名删除 3.作者删除')
                            self.bookDB.remove(n)
                        elif r=='6':
                            #退出系统
                            exit()
                        else:
                            print('输入有误，请重新输入')
                    else:
                        print('重新登陆')
            elif r=='2':
                # 注册
                print('输入个人信息')
                self.userDB.add(ZhuCe().getUser())
            elif r=='3':
                # 修改密码
                self.ExchangePwd()
            else:
                print('输入有误，请重新输入')


def start():
    Manager().manager()

start()

