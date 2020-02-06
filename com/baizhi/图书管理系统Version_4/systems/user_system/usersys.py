import com.baizhi.图书管理系统Version_4.entity.user as user
import com.baizhi.图书管理系统Version_4.yichang.yichangs as yichang
import threading
import re
import pickle
f=open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\user_db','rb')
userDB=pickle.load(f)  # 反序列化    将二进制文件转化成Python对象
f.close()
def ist(i):
    if '~' in i or '!' in i or '@' in i or '#' in i or '$' in i or '%' in i or '^' in i or '&' in i or '*' in i or '-' in i or '=' in i or '[' in i or ']' in i or '\\' in i or ';' in i:
        return True
    else:
        return False
# def findN(name):
#     for i in userDB.userBianli():
#         if i.name==name:
#             f=1
#             print('该用户名已存在')



# def findP(pwd):
#     n = len(pwd)
#     a, b, c = 0, 0, 0
#     a1 = 0
#     if pwd[0].isalpha():
#         a1 = 1
#     for j in pwd:
#         if j.isdecimal():
#             a = 1
#         if j.isalpha():
#             b = 1
#         if ist(j):
#             c = 1
#     if n <= 8 or a == 1 and b == 0 or a == 0 and b == 1:
#         print('等级为低')
#     if a + b + c == 2 and n >= 8:
#         print('等级为中')
#     if a + b + c == 3 and n >= 16 and a1 == 1:
#         print('等级为高')
#     if pwd == '':
#         print('密码不能为空')
#     if a1 == 0:
#         print('必须字母开头')
#     for i in range(10):
#         if pwd.startswith('{0}'.format(i)):
#             print('不能以数字开头')
#     if n < 16:
#         print('长度不够，不能少于16位')
#     if a + b + c < 3:
#         print('需要由数字，字母及字符三种组合')
class ZhuCe:
    #注册用户信息
    def __init__(self):
        self.f=1
        self.f1=1
        while self.f==1 :
            self.name = input('输入name')
            t1 = threading.Thread(target=self.findN, args=(self.name,))
            t1.start()
        while self.f1==1 :
            self.pwd = input('输入密码')
            t2 = threading.Thread(target=self.findP, args=(self.pwd,))
            t2.start()
        self.age = input('输入age')
        self.sex = input('输入性别')
        while 1:
            self.phone = input('输入电话')
            a = re.match('[0-9]{11}', self.phone)
            if a:
                break
            else:
                print('格式错误')
        while 1:
            self.mail = input('输入邮箱')
            n = '^[0-9A-Za-z]{1,9}@[0-9a-zA-Z]{1,5}\.(com|cn|net)'
            a = re.match(n, self.mail)
            if a:
                break
            else:
                print('格式错误 重新输入')
        self.addr = input('输入地址')
        self.user = user.User(self.name, self.age,self.sex, self.phone, self.mail,self.pwd,self.addr)
        print('------注册成功------')

    def findN(self,name):
        for i in userDB.userBianli():
            if i.name == name:
                print('该用户名已存在,重新输入')
                return None
        else:
            self.f = 0

    def findP(self,pwd):
        n = len(pwd)
        a, b, c = 0, 0, 0
        a1 = 0
        if pwd[0].isalpha():
            a1 = 1
        for j in pwd:
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
            self.f1=0
        if pwd == '':
            print('密码不能为空')
        if a1 == 0:
            print('必须字母开头')
        for i in range(10):
            if pwd.startswith('{0}'.format(i)):
                print('不能以数字开头')
        if n < 16:
            print('长度不够，不能少于16位')
        if a + b + c < 3:
            print('需要由数字，字母及字符三种组合')

    def getUser(self):
        return self.user
def ExchangePwd(userDB):
    #修改密码
    name=input('name:')
    pwd=input('old pwd:')
    for i in userDB.userBianli():
        if i.name==name and i.pwd==pwd:
            while 1:
                i.pwd = input('输入密码')
                n = len(i.pwd)
                a, b, c = 0, 0, 0
                a1 = 0
                x = i.pwd[0]
                if x.isalpha():
                    a1 = 1
                for j in i.pwd:
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
                if i.pwd == '':
                    print('密码不能为空')
                if a1 == 0:
                    print('必须字母开头')
                for a in range(10):
                    if i.pwd.startswith('{0}'.format(i)):
                        print('不能以数字开头')
                if n < 16:
                    print('长度不够，不能少于16位')
                if a + b + c < 3:
                    print('需要由数字，字母及字符三种组合')
            print('修改成功')
            return
    print('密码错误')
def ExchangeUser(userDB):
    #修改用户信息
    name=input('name:')
    pwd=input('pwd:')
    for i in userDB.userBianli():
        if i.name==name and i.pwd==pwd:
            print('name:'+i.name+'   age:'+i.age+'   sex:'+i.sex+'   phone:'+i.phone+'   mail'+i.mail+'   addr'+i.addr)
            while 1:
                try:
                    n=input('1 修改name 2 修改age 3 修改性别 4 修改电话 5修改邮箱 6修改地址 7修改完成')
                    if n=='1':
                        i.name=input('new name：')
                    elif n=='2':
                        i.age=input('new age：')
                    elif n=='3':
                        i.sex=input('new sex：')
                    elif n=='4':
                        i.phone=input('new phone:')
                    elif n=='5':
                        i.mail=input('new mail')
                    elif n=='6':
                        i.addr=input('new addr')
                    elif n=='7':
                        return
                    else:
                        raise yichang.PrintError('输入错误')
                except yichang.PrintError as e:
                    print(e)
    print('用户名或密码错误')