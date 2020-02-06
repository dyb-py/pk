#1
# 类是对象共性的抽象
# 类是对象的模板
# 类是客观对象在人脑的主观反应

#2
#尽可能的抽象

#3
#使用私有化

#4
#方法是类内部的函数，和实例对象绑定在一起

#5
#__init__()构造方法

#6
# 1. self：指代当前对象
# 2. self在方法中不需要主动传值，自动将当前对象 传递给self
# 3. 在方法中，self相当于外面的对象
# 4. self之后可以添加参数，用于方法的形参
# 5. self是开发习惯的写法，方法调用时，编译器会 将当前对象传递给第一个参数

#7
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def baoming(self):
#         print(self.name,self.age)
# a=Person('杜亚博',18).baoming()

#8
# class Worker():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def work(self,time):
#         self.time=time
# a=Worker('杜亚博',18,'20k')
# print(a.age,a.name,a.salary)
# a.work(10)
# print(a.time)

#9
# class ParkTicket():
#     def __init__(self,adult,child):
#         self.adult=adult
#         self.child=child
#     def ticket(self,time):
#         self.time=time
#         if time=='周末':
#             money=self.adult*120+self.child*60
#             print('money为'+str(money))
#             return money
#         else:
#             money=self.adult*100+self.child*50
#             print('money为'+str(money))
#             return money
# a=ParkTicket(2,1).ticket('周末')

#10
class Address():
    def __init__(self,address,zipCode):
        self.address=address
        self.zipCode=zipCode

#11

class Worker():
    def __init__(self,name,age,salary,address):
        self.name=name
        self.age=age
        self.salary=salary
        self.address=address
    def work(self,time):
        self.time=time
a=Worker('杜亚博',18,'20k',Address('北京',10084))
print(a.age,a.name,a.salary,a.address.address,a.address.zipCode)
a.work(10)
print(a.time)


