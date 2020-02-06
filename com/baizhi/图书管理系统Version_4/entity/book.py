class Book:
    count=3
    def __init__(self,name,author,price,category,desc):
        '''
        :param ids: 系统内部编号
        :param name: 书名
        :param author: 作者
        :param price: 价格
        :param category: 类别
        :param desc: 评价
        '''
        Book.count+=1
        self.ids=self.count
        self.name=name
        self.author=author
        self.price=price
        self.category=category
        self.desc=desc