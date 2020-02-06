from com.baizhi.图书管理系统Version_4.entity.user import User
class UserDB:
    def __init__(self):
        self.__l=[]

    def add(self,user):  # 和业务无关
        self.__l.append(user)

    def moidfy(self,*args):
        pass

    def select(self):
        return self.__l
    def userBianli(self):
        for i in self.__l:
            yield i
    # def __iter__(self):
    #     return self.__l.__iter__()
