import time

class TimeJ():
    start=''
    end=''
    def start(self):
        print('开始计时')
        self.start=time.localtime()
    def end(self):
        if self.start:
            print('结束计时')
            self.end=time.localtime()
        else:
            print('未开始计时')
    def jiShi(self):
        if self.start and self.end:
            self.h=self.end[3]-self.start[3]
            self.m=self.end[4]-self.start[4]
            self.s=self.end[5]-self.start[5]
            print('经过了'+str(self.h)+'小时 '+str(self.m)+'分 '+str(self.s)+'秒')
        else:print('没有start或end')

    def __add__(self, other):
        h = self.h+other.h
        m = self.m + other.m
        s = self.s + other.s
        return ('一共经过了' + str(h) + '小时 ' + str(m) + '分 ' + str(s) + '秒')

a=TimeJ()
a.start()
time.sleep(2)
a.end()
a.jiShi()
b=TimeJ()
b.start()
time.sleep(2)
b.end()
b.jiShi()
print(a+b)