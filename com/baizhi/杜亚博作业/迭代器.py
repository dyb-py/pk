class Iterator:
    def __init__(self,iterable):
        self.__l=[i for i in iterable]
        self.__a=iter(self.__l)  # __a:列表的迭代器对象
    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__a)
        # return 1

a=Iterator([1,2,3])
for i in a:  # 1. a  2. next()  3. 获取异常？
    print(i)


# 1. 获取迭代器  2. 调用next  3. 获取异常

# for i in 'abc':   # 自动处理异常
#     print(i)
#

#1. 获取迭代器
# a_iterator=iter(a)
# while 1:
#     try:
#         # 2调用next
#         print(next(a_iterator))
#     except:
#         break




