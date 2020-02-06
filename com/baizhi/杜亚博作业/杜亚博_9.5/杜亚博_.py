#3
# 一个类的属性可以是另一个对象，该形式称之为组合

#4
# 1. 子类可以继承父类的成员
# 2. 父类扩展了子类
# 3. 父类的私有成员不能直接继承给子类 子类继承到了父类的私有成员，但是不能直接使用
# 4. Python中的继承是多继承 可以继承多个父类的成员
# 5. 调用某成员，优先调用子类成员，如果没有则向父类调用

#5
#组合是一个类的属性是另一个类对象，而继承是这个类继承了父类的属性和方法，

#9
# 在调用类+（）时 对象创建

#10
#方法名会自动遮蔽对象的属性

#11
# 不会， 调用某成员，优先调用子类成员，如果没有则向父类调用

#12
# 企鹅类中使用飞的同名方法 覆盖父类的飞的方法

#13

#15
# xy是实例属性 count是类属性

#16
# printBB()应该写出printBB(self)

#17
# 会造成A类被调用两次

#18
# class A():
#     def __init__(self):
#         print("进入A…")
#         print("离开A…")
# class B(A):
#     def __init__(self):
#         print("进入B…")
#         super().__init__()
#         print("离开B…")
# class C(A):
#     def __init__(self):
#         print("进入c…")
#         super().__init__()
#         print("离开C…")
# class D(B, C):
#     def __init__(self):
#         print("进入D…")
#         # B.__init__(self)
#         # C.__init__(self)
#         super().__init__()
#         print("离开D…")
# d=D()


#22
# class Role:
#     hurt=1
#     name=''
#     def attack(self,hurt):
#         return hurt
# class Magicer(Role):
#     def __init__(self,magicGrade):
#         self.name='magicer'
#         self.magicGrade=magicGrade
#     def attack(self):
#         self.hurt=self.magicGrade*5
#         return self.hurt
# class Soldier(Role):
#     def __init__(self,hurt):
#         self.name = 'soldier'
#         self.hurt=hurt
#     def attack(self):
#         return self.hurt
# class Team:
#     member=[]
#     num=0
#     hurt=0
#     def addMember(self,role):
#         self.num+=1
#         if self.num<=6:
#             self.role=Role()
#             self.member.append(role)
#         else:print('队伍已满')
#     def attackSum(self):
#         for i in self.member:
#             self.hurt+=i.attack()
#         return self.hurt
# t=Team()
# z1=Soldier(100)
# m1=Magicer(20)
# m2=Magicer(10)
# m3=Magicer(80)
# m4=Magicer(10)
# m5=Magicer(10)
# m6=Magicer(12)
# t.addMember(z1)
# t.addMember(m1)
# t.addMember(m2)
# t.addMember(m3)
# t.addMember(m4)
# t.addMember(m5)
# t.addMember(m6)

#23
class Account:
    id=0
    balance=0
    __password=''
    def __init__(self,id,balance,password):
        self.id=id
        self.__password=password
        self.balance=balance
    def getPassword(self):
        return None
    def setPassword(self,password):
        if len(password)==6:
            self.__password=password
        else:
            print('密码应为六位数')
class SavingAccount(Account):
    __interestRate=0
    def __init__(self,id,balance,password,interestRate,):
        super().__init__(id, balance, password)
        self.interestRate=interestRate
    def setInterestRate(self,interestRate):
        if interestRate>0 and interestRate<0.1:
            self.interestRate=interestRate
        else:print('利率应该大于0小于10%')
    def getInterestRate(self, interestRate):
        return self.interestRate
class CredAcoount(Account):
    def __init__(self,id,balance,password,creditLine):
        super().__init__(id, balance, password)
        self.creditLine=creditLine





#24
# class Shape:
#     def area(self):
#         pass
#     def girth(self):
#         pass
# class Circle(Shape):
#     radius=0
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         self.area=3.14*(self.radius**2)
#         return self.area
#     def girth(self):
#         self.girth=2*3.14*self.radius
#         return self.girth
# class Rect(Shape):
#     l=0
#     w=0
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w
#     def area(self):
#         self.area=self.l*self.w
#         return self.area
#     def girth(self):
#         self.girth=2*(self.l+self.w)
#         return self.girth
# class Square(Rect):
#     def __init__(self,length):
#         self.length=length
#     def area(self):
#         self.area=self.length**2
#         return self.area
#     def girth(self):
#         self.girth=4*self.length
#         return self.girth
# s=Square(5)
# print(s.girth(),s.area())


#25
# class Employee:
#     # name=''
#     # birth=0
#     # salary=0
#     def __init__(self,name,birth,salary):
#         self.name=name
#         self.birth=birth
#         self.salary=salary
#     def getSalary(self,intmonth):
#         if self.birth==intmonth:
#             a=self.salary+100
#         else:a=self.salary
#         return a
# a=Employee('du',10,10000)
# print(a.getSalary(9))
# class SalariedEmployee(Employee):
#     def __init__(self,name,birth,salary):
#         self.__name = name
#         self.__birth = birth
#         self.__salary = salary
# class HourlyEmployee(Employee):
#     def __init__(self,name,hour,salary,birth):
#         self.__hour=hour
#         self.__salary=salary
#         self.__birth=birth
#         self.__name = name
#     def getSalary(self,intmonth):
#         if self.__hour>160:
#             a=160*self.__salary+(160-self.__hour)*self.__salary*1.5
#         else:a=self.__hour*self.__salary
#         if self.__birth==intmonth:
#             a+=100
#         return a
# h=HourlyEmployee('h',160,100,10)
# print(h.getSalary(1))
# print(h.getSalary(10))
# print(h.getSalary(10))
# class SalesEmployee(Employee):
#     def __init__(self,name,birth,sales,rate):
#         self.__name = name
#         self.__birth = birth
#         self.__sales=sales
#         self.__rate=rate
#     def getSalary(self,intmonth):
#         a=self.__rate*self.__sales
#         if self.__birth==intmonth:
#             a+=100
#         return a
# s=SalesEmployee('s',10,10000,0.8)
# print(s.getSalary(10))
# class BasePlusSalesEmploryee(SalesEmployee):
#     def __init__(self,name,birth,sales,rate,baseSalary):
#         self.__name = name
#         self.__birth = birth
#         self.__sales = sales
#         self.__rate = rate
#         self.__baseSalary=baseSalary
#     def getSalary(self,intmonth):
#         a=self.__baseSalary+(self.__sales*self.__rate)
#         if self.__birth==intmonth:
#             a+=100
#         return a
# b=BasePlusSalesEmploryee('b',10,10000,0.8,2000)
# print(b.getSalary(10))




# 26
# Employee=[a,h,b,s]
# for i in Employee:
#     print(i.getSalary(1))




#27
# class Stack:
#     s=[]
#     def isEmpty(self):
#         if len(self.s)==0:
#             return True
#         else:return False
#     def push(self,num):
#         self.s.append(num)
#         print(self.s)
#         return self.s
#     def pop(self):
#         self.s.pop()
#         print(self.s)
#         return self.s
#     def top(self):
#         n=len(self.s)
#         print(self.s[n-1])
#         return self.s[n-1]
#     def bottom(self):
#         print(self.s[0])
#         return self.s[0]
# a=Stack()
# a.push(2)
# a.push('a')
# print(a.isEmpty())
# a.pop()
# a.push(1)
# a.push(1)
# a.push(3)
# a.top()


#28
class Bank:
    def openAccount(self,id,balance,password,type):
        self.id=id
        self.password=password
        self.type=type
        self.balance=balance
        if type==0:
            self.account=Account(id,balance,password,)
        elif type==1:
            self.account=SavingAccount(id,balance,password,interestRate=0.1)
        elif type==2:
            self.account=CredAcoount(id,balance,password,creditLine=1000)
        return self.account
    def deposit(self,amount):
        self.balance=self.account.balance+amount
        return self.balance
    def withdraw(self,amount):
        if self.type==1 or self.type==0:
            if self.balance>=amount:
                self.balance=self.balance-amount
                return self.balance
            else:
                print('不允许透支')
        elif self.type==2:
            if self.balance+self.account.creditLine<amount:
                print('额度不够')
            else:
                if self.balance>=amount:
                    self.balance=self.balance-amount
                    return self.balance
                else:
                    self.account.creditLine=self.account.creditLine-(amount-self.balance)
                    self.balance=0
                    print('还能透支'+str(self.account.creditLine))
b=Bank()
b.openAccount('du',10000,123,2)
b.deposit(10000)
b.withdraw(20500)
print(b.balance)