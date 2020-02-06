class Girl:
    def __init__(self):
        self.__age=18

    def getAge(self):
        print('get方法被执行')
        return self.__age

    def setAge(self,newAge):
        print('set 方法被执行')
        self.__age=newAge

    def delAge(self):
        print('del 方法被执行')
        del self.__age

    hehe=property(getAge,setAge,delAge)  # age属性是一个property对象

g=Girl()
# print(g.age) # 对象.属性 优势：访问简单   劣势：不安全
# print(g.getAge())  # 对象.方法   优势： 安全  劣势：访问不够优雅

# print(g.hehe)  # 对象.property() ---  getAge（）
# g.hehe=20   # 对象.property()=**  ---  setAge()
# print(g.hehe)
# del g.hehe  # del  对象.property() --- delAge()
# print(g.hehe)

print(g.hehe)
print(g.getAge())
g.hehe=20
print(g.getAge())
# del g._Girl__age
# print(g.hehe)
del g.hehe
print(g._Girl__age)