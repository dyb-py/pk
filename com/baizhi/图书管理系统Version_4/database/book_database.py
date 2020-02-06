from com.baizhi.图书管理系统Version_4.entity.book import Book
import com.baizhi.图书管理系统Version_4.yichang.yichangs as yichang
class BookBD:
    def __init__(self):
        self.__l=[]
    def add(self,book):
        self.__l.append(book)
    def modify(self,ids):
        for i in self.bianLi():
            if i.ids==ids:
                try:
                    print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    n=input('1.修改书名 2.修改作者 3.修改价格 4.修改类别 5.修改评价')
                    if n=='1':
                        i.name=input('输入书名')
                    elif n=='2':
                        i.author=input('输入作者')
                    elif n=='3':
                        i.price=float(input('输入价格'))
                    elif n=='4':
                        i.category=input('输入类别')
                    elif n=='5':
                        i.desc=input('输入评价')
                    else:
                        raise yichang.PrintError('输入错误')
                except yichang.PrintError as e:
                    print(e)
                break
        else:print('没有该id')
    # 删除数据
    def remove(self,x):
        try:
            if x=='1':
                ids=int(input('输入id'))
                for obj in self.bianLi():
                    if obj.ids==ids:
                        self.__l.remove(obj)
                        print('删除成功')
                        return
                print('没有该id')
            elif x=='2':
                name=input('输入书名')
                for i in self.bianLi():
                    if i.name==name:
                        self.__l.remove(i)
                        print('删除成功')
                        return
                print('没有该书名')
            elif x=='3':
                a=input('输入作者')
                for i in self.bianLi():
                    if i.author==a:
                        self.__l.remove(i)
                        print('删除成功')
                        return
                print('没有该作者')
            else:
                raise yichang.PrintError('输入错误')
        except yichang.PrintError as e:
            print(e)

    # 查询数据
    def select(self,ids):
        for i in self.bianLi():
            if i.ids==ids:
                return i
    # 返回数据库的迭代器
    def bianLi(self):
        for i in self.__l:
            yield i
    # def __iter__(self):
    #     # return self.l.__iter__()
    #     return iter(self.__l)
