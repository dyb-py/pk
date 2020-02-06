#1
# 用issubclass()判断一个类是否是另一个子类
#2
#用isinstance()判断a是否是A的实例对象
#7
#hasattr（）判断obj是否有name属性
#8
# 将一个属性和另一个属性关联起来，同生共死
#14
class C:
    def __init__(self, size=10):
        self.size = size
    def getXSize(self):
        print('get')
        return self.size
    def setXSize(self, value):
        print('set')
        self.size = value
    def delXSize(self):
        print('def')
        del self.size
    x=property(getXSize,setXSize,delXSize)
c=C()
print(c.x)
c.x=12
print(c.x)