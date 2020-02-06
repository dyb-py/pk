
# a=0
# b=1
# count=0
# n=int(input('请输入一个整数'))
# while count<n:
#     a,b=b,a+b
#     count+=1
#     print(a)
# class Fib:
#     def __init__(self):
#         self.a=0
#         self.b=1
#         # self.count=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         return self.a
# f=Fib()
# for i in range(12):
#     print(next(f))

class Fib:
    def __init__(self,n):
        self.a=0
        self.b=1
        self.count=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        self.count+=1
        self.a,self.b=self.b,self.a+self.b
        if self.count>self.n:
            raise StopIteration
        else:
            return self.a
#
f=Fib(12)
# for i in range(12):
#     print(next(f))
for i in f:
    print(i)
#










