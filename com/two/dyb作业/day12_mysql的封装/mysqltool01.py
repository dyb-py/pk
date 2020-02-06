import MySQLdb

# 1. 是否有弊端
# 2. 是否更方便
# def get():
#     # 创建连接
#     conn=MySQLdb.connect(host='localhost',user='root',password='123456',port=3306,db='test123',charset='utf8')
#     # 创建游标
#     cursor=conn.cursor()
#     # sql语句
#     sql='select * from student'
#     # 执行sql
#     cursor.execute(sql)  # cursor对象也是一个迭代器
#     # 查看一个数据
#     print(cursor.fetchone())
#     # 查看多个数据
#     print(cursor.fetchall())
#     # 事务提交
#     conn.commit()
#     # 关闭资源   先关闭小资源，然后关闭大资源
#     cursor.close()
#     conn.close()


# version1.0
class MySqlTools(object):

    # 初始化方法
    def __init__(self,*,db,user,password,host,port,charset):
        self.db=db
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        self.charset=charset

    def conntion(self):
        # 连接数据库
        self.conn = MySQLdb.connect(db=self.db, user=self.user, password=self.password,
                                    host=self.host, port=self.port, charset=self.charset)
        # 创建游标
        self.cursor = self.conn.cursor()

    #  增加
    # @staticmethod
    # def add_one_data():  # PEP8:规定了Python的书写规范           PEP:python开发增强建议书
    #     conn = MySQLdb.connect
    #     print(conn)
    def add(self,sql):
        # 连接数据库：
        self.conntion()
        self.cursor.execute(sql)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    # 删除
    def delete(self,sql):
        # 连接数据库：
        self.conntion()
        self.cursor.execute(sql)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    # 修改
    def modify(self,sql):
        # 连接数据库：
        self.conntion()
        self.cursor.execute(sql)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    # 查询
    def get(self,sql):
        # 连接数据库：
        self.conntion()
        self.cursor.execute(sql)
        r=self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return r

if __name__ == '__main__':
    tool=MySqlTools(db='test123',user='root',password='123456',host='localhost',port=3306,charset='utf8')
    print(tool.get('select * from student'))





