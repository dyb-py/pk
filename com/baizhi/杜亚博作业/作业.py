# 3. 一个类中的属性是另一个对象---  组合（电脑---小对象组成大对象）

# 5. 继承和组合没有必然联系

# class A:
#     age=18
#
# class B(A):
#     pass
#
# class C:
#     a=A()
#
# b=B()
# c=C()
# print(b.age)  # 继承
# print(c.a.age) # 组合

# 9： 1. class 时  2. 虚拟机在加载 字节码文件时（.pyc）
# 字节码文件：
# .pyc(由python源代码实现的)
# .pyo（.pyc的精简版，用于嵌入式）
# .pyd （有其他语言构建的字节码：C语言）

# 10  属性 方法名
# class A:
#     age=18
#     def age(self): # 方法名相当于：变量
#         print('this is age method')
#     age=20
#
# a=A()
# print(a.age)
# 1. 类属性和方法名重名：谁最后出现，则会覆盖前面的内容
# class  A:
#     def age(self):
#         print('this is age method')
#     def hehe(self):
#         self.age=20
#
# a=A()
# # print(a.age)
# # a.hehe()
# # print(a.age)
# a.hehe()
# print(a.age)

# 2. 实例属性和方法名重名：如果实例属性被创建，必定覆盖方法

# class A:
#     def __init__(self):
#         self.age=18
#
#     def age(self):
#         print('this is age method')
#
# a=A()
# print(a.age)

# class A:
#     def age(self):
#         self.age=18
#
# a=A()
# a.age()
# # print(a.age)
# a.age()

# 13
# class A:
#     def __init__(self):
#         pass
#
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         super().__init__() # 默认会传入: 当前类，当前实例对象
#         # super(B,self).__init__()
#         # super(B).__init__()
#         # super(A,B).__init__()

# class A:
#     @staticmethod
#     def hehe():
#         pass
#
#     @classmethod
#     def hehe2(cls):
#         pass
#
# a=A()
# a.hehe()


# # 22
# class Role:
#     def __init__(self,name):
#         self.name=name
#
#     def attack(self):  # 用于被子类覆盖
#         pass
#
# class Magicer(Role):
#     damage=5
#     def __init__(self,level,name):
#         if level>10:
#             self.level=10
#         else:
#             self.level=level
#         super().__init__(name)
#     def attack(self): # 覆盖了父类的方法
#         return self.level*self.damage
#
# class Soldier(Role):
#     def __init__(self,hurt,name):
#         self.hurt=hurt
#         super().__init__(name)
#     def attack(self):
#         return self.hurt
#
#
# class Team:
#     def __init__(self):
#         self.team=[]  # 存储成员
#
#     def addMember(self,*role): # role: 元组
#         # 先判断是否满员
#         if len(self.team)+len(role)>6:
#             print('超出队伍容量')
#         else:
#             self.team.extend(role)
#
#     def attackSum(self):
#         # sums=0
#         # for role in self.team:
#         #     sums+=role.attack()
#         # return sums
#         return  sum([i.attack() for i in self.team])
#
#
#
# t=Team()
# t.addMember(Magicer(11,'zhang3'),Magicer(10,'li4'),Magicer(5,'xiaobo'),
#             Soldier(100,'jianggang'),Soldier(100,'feige'),Soldier(50,'liuhao'))
#
# # t.addMember(Magicer(10))
#
# print(t.attackSum())
# for role in t.team:
#     print(role.name)
#
# # 1. 可读性：越简单越好，越明确越好
# # 2. 减少判断条件，减少判断次数
# # 3. 减少循环层数，减少循环次数
# # 4. 增加稳定性，容错性
# # 5. 减少内存消耗
# # 6. 减少变量的定义


# # 23 ：
# class Account:
#     def __init__(self,id,balance,password):
#         self.id=id
#         self.balance=balance
#         self.__password=password
#     def getPwd(self):
#         pass
#
#     def SetPwd(self,newpass):
#         if len(newpass)!=6:
#             pass
#         else:
#             self.__password=newpass
#
# class SavingAccount(Account):
#     def __init__(self,interestRate):
#         self.__interestRate=interestRate
#     def setInterestRate(self,newRate):
#         if 0<newRate<0.1:
#             self.__interestRate=newRate
#
# class CreditAccount(Account):
#     def __init__(self,creditLine):
#         self.creditLine=creditLine

# # 24
# class  Shape:
#     def area(self): # 面积
#         pass
#     def girth(self): # 周长
#         pass
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*self.r**2
#     def girth(self):
#         return 3.14*self.r*2
# class Rect(Shape):
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w
#     def area(self):
#         return self.l*self.w
#     def girth(self):
#         return (self.l+self.w)*2
#
# class Square(Rect):
#     def __init__(self,a):
#         super().__init__(a,a)
#
# s=Square(1)
# print(s.area())
# print(s.girth())

# # 28:
class Account:
    def __init__(self,id,password,balance=0):
        self.id=id
        self.balance=balance
        self.__password=password
    def getPwd(self):
        pass

    def SetPwd(self,newpass):
        if len(newpass)!=6:
            pass
        else:
            self.__password=newpass

class SavingAccount(Account):
    def __init__(self,interestRate,id,password):
        super().__init__(id,password)
        self.__interestRate=interestRate
    def setInterestRate(self,newRate):
        if 0<newRate<0.1:
            self.__interestRate=newRate

class CreditAccount(Account):
    def __init__(self,creditLine,id,password):
        super().__init__(id, password)
        self.creditLine=creditLine

class Bank:
    def __init__(self):
        self.bank=[]
    def openAccount(self,id,pwd,types):
        if types==0:
            self.account=Account(id,pwd)
        elif types==1:
            self.account=SavingAccount(id,pwd)
        elif types==2:
            self.account=CreditAccount(id,pwd)
        self.bank.append(self.account)
        return self.account

    def saveMoney(self,id,money):
        for account in self.bank:
            if account.id==id:
                account.balance+=money
                return account.balance
        return '没找到该账号'

    def getMoney(self,money):
        for account in self.bank:
            if account.id == id:
                if account.balance<money:
                    if type(account)!=CreditAccount:
                        print('余额不足')
                    else:
                        account.balance -= money
                        return account.balance
        return '没找到该账号'
a=Bank()
a.openAccount('ad',123,0)

b=[i for i in range(10)]
b=iter(b)

print()
# # 25
# class Employee:
#     def __init__(self,name,birth):
#         self.name=name
#         self.birth=birth
#     def getSalary(self,intMonth,salary):
#         # 如果过生日，则额外奖励100
#         if self.birth==intMonth:
#             return salary+100
#         else:
#             return salary
#
#
# class SalariedEmployee(Employee):
#     def __init__(self,baseSalary,name,birth):
#         super().__init__(name,birth)
#         self.baseSalary=baseSalary
#     def getSalary(self,intMonth):
#         return super().getSalary(intMonth,self.baseSalary)
#
# class HourlyEmployee(Employee):
#     def __init__(self,hourlySalary,hour,name,birth):
#         super().__init__(name, birth)
#         self.hourlySalary=hourlySalary
#         self.hour=hour
#     def getSalary(self,intMonth):
#         if self.hour>160:
#             return super().getSalary(intMonth,(160+(self.hour-160)*1.5)*self.hourlySalary)
#         else:
#             return super().getSalary(intMonth,self.hourlySalary*self.hour)
#
# class SalesEmployee(Employee):
#     def __init__(self,sales,rate,name,birth):
#         super().__init__(name, birth)
#         self.sales=sales
#         self.rate=rate
#     def getSalary(self,intMonth):
#         return super().getSalary(intMonth,self.sales*self.rate)
#
# class BasePlusSalesEmployee(SalesEmployee):
#     def __init__(self,baseSalary,sales,rate,name,birth):
#         super().__init__(sales,rate,name, birth)
#         self.baseSalary=baseSalary
#     def getSalary(self,intMonth):
#         return self.baseSalary+super().getSalary(intMonth)
#
#
# l=[SalesEmployee(1000000,0.1,'xiaobo',3),SalariedEmployee(10000,'jiangang',4),
#    HourlyEmployee(1000,10,'liuhao',4),BasePlusSalesEmployee(10000,1000000,0.1,'feige',3)]
# for i in l:
#     print(i.getSalary(3))


# 27
# class Stack:  # 封装
#     def __init__(self):
#         self.__l=[]  # 工具： 只自己使用的对象，不提供get/set方法
#     def isEmpty(self):
#         # if len(self.__l)==0:
#         #     return True
#         # else:
#         #     return False
#         return not len(self.__l)
#
#     def push(self,value):
#         self.__l.append(value)
#
#     def pop(self):
#         return self.__l.pop()
#
#     def top(self):
#         return self.__l[-1]
#
#     def bottom(self):
#         return self.__l[0]
#
#     # def getItems(self):
#     #     return self.__l
#     def __iter__(self):
#         return iter(self.__l)
#
#
#
# s=Stack()
# s.push(1)
# s.push(2)
# for i in s:  # 1. iter(s)   2. next(iter(s))  3. StopIteration
#     print(i)

# print(s.getItems())
# s.__iter__()
# iter(s)   #ｓ是个可迭代对象　



# 可迭代对象： 拥有迭代器的对象      iter()有对象返回   迭代器对象
# 迭代器对象： 实现了__iter__   __next__  的对象

# 列表： l=[1,2,3]   没有__next__   有__iter__     列表.__iter__/  iter(列表)  有对象返回： 列表是可迭代对象
# next(列表) / 列表.__next__ 没有值，说明列表不是迭代器，仅仅是个可迭代对象








