import com.baizhi.图书管理系统Version_4.entity.book as book
import com.baizhi.图书管理系统Version_4.yichang.yichangs as yichang
def Select(x,bookDB):
    # ('1.根据类型查询 2.根据作者查询 3.书名查询 4.价格查询')
    try:
        if x == '1':
            print('书的类型有 1科普  2科幻  3励志小说 4科幻小说 5文学小说 6科学文献 7古典文学 8网络小说 9魔幻巨作\n ')
            n = int(input('请选择书籍类型\n'))
            try:
                if n == 1:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '科普':
                            a+=1
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 2:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '科幻':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 3:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '励志小说':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 4:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '科幻小说':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 5:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '文学小说':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 6:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '科普':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 7:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '古典文学':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 8:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '网络小说':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                elif n == 9:
                    a=0
                    for i in bookDB.bianLi():
                        if i.category == '魔幻巨作':
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    if a==0:
                        print('没有该类型的书')
                else:
                    raise yichang.PrintError('输入错误')
            except yichang.PrintError as e:
                print(e)
        elif x == '2':
            n = input('输入作者姓名')
            f=0
            for i in bookDB.bianLi():
                if i.author == n:
                    print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    f+=1
            if f==0:
                print('没有该作者')
        elif x == '3':
            n = input('输入书名')
            f=0
            for i in bookDB.bianLi():
                if i.name == n:
                    print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                    f+=1
            if f==0:
                print('没有该书')
        elif x == '4':
            print('书的价格区间有 1. <=50  2. 50<<100  3. 100<<200 4. 200<< \n')
            n = int(input('选择价格区间\n'))
            try:
                if n == 1:
                    for i in bookDB.bianLi():
                        if i.price <= 50:
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                elif n == 2:
                    for i in bookDB.bianLi():
                        if i.price >= 50 and i.price <= 100:
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                elif n == 3:
                    for i in bookDB.bianLi():
                        if i.price >= 100 and i.price <= 200:
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                elif n == 4:
                    for i in bookDB.bianLi():
                        if i.price >= 200:
                            print(i.ids, i.name, i.author, i.price, i.category, i.desc)
                else:
                    raise yichang.PrintError('输入错误')
            except yichang.PrintError as e:
                print(e)
        else:
            raise yichang.PrintError('输入错误')
    except yichang.PrintError as e:
        print(e)
class InputBook():
    #输入书籍信息
    def __init__(self):
        self.name = input('输入name')
        self.author = input('输入作者')
        self.price = float(input('输入价格'))
        self.category = input('输入类别')
        self.desc = input('输入评价')
        self.book=book.Book(self.name,self.author,self.price,self.category,self.desc)
    def getBook(self):
        return self.book