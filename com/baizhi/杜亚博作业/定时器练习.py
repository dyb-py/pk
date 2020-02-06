#
import time
class Timmer:
    def __init__(self):
        self.begin=0
        self.end=0
        self.total=0

    def start(self):
        self.begin=time.localtime()

    def stop(self):
        if self.begin==0:
            print('尚未开始计时')
        else:
            self.end=time.localtime()
            # total 是一个时间差，列表
            self.total=self.sub(self.begin,self.end) # 元组之间不能相减

    def sub(self,begin,end):
        # begin  end : 元组
        temp=[]
        for i in range(6):
            # 引入时间算法
            r=end[i]-begin[i]  #  13:59:59   14:00:00
            temp.append(r)
            # [年差，月差，日差，时差，分差，秒差]
        return temp

    def __add__(self, other):
        # self: t1  other:t2
        r2=list(map(lambda x,y:x+y,self.total,other.total))
        # r2: map对象： 元素：年差，月差，日差，时差，分差，秒差
        print(self.format(r2)) # 把时间数据 格式化成 年月日时分秒的形式

    def format(self,iterable):
        iterable=list(iterable)
        # iterable: (年差，月差，日差，时差，分差，秒差)
        s=['年','月','日','小时','分','秒']
        temp=''
        for i in range(6):
            if iterable[i]==0:
                continue
            else:
                temp+=str(iterable[i])+s[i]+'\t'
        return temp

t1=Timmer()
t2=Timmer()

t1.start()
time.sleep(3)
t1.stop()

t2.start()
time.sleep(3)
t2.stop()

t1+t2
