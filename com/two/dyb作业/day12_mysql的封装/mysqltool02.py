import MySQLdb
# version1.0
# 代码冗余
# sql语句，不够简洁
# 不够安全

# version2.0
class MySqlTools(object):

    # 初始化方法
    def __init__(self,*,db,user,password,host,port,charset):
        self.__db=db
        self.__user=user
        self.__password=password
        self.__host=host
        self.__port=port
        self.__charset=charset

    # 连接数据库
    def _conntion(self):  # 希望在当前文件下使用（可以被其他类使用），不希望其他的模块使用  _a  受保护的
        # 连接数据库
        self.conn = MySQLdb.connect(db=self.__db, user=self.__user, password=self.__password,
                                    host=self.__host, port=self.__port, charset=self.__charset)
        # 创建游标
        self.cursor = self.conn.cursor()

    # 释放资源
    def _close(self):
        self.cursor.close()
        self.conn.close()

    #  增加
    # @staticmethod
    # def add_one_data():  # PEP8:规定了Python的书写规范           PEP:python开发增强建议书
    #     conn = MySQLdb.connect
    #     print(conn)
    def add(self,sql):
        # 连接数据库：
        self._conntion()
        self.cursor.execute(sql)
        self.conn.commit()
        self._close()

    # 删除
    def delete(self,sql):
        # 连接数据库：
        self._conntion()
        self.cursor.execute(sql)
        self.conn.commit()
        self._close()
    # 修改
    def modify(self,sql):
        # 连接数据库：
        self._conntion()
        self.cursor.execute(sql)
        self.conn.commit()
        self._close()
    # 查询
    def get(self,sql):
        # 连接数据库：
        self._conntion()
        self.cursor.execute(sql)
        r=self.cursor.fetchall()
        self._close()
        return r



if __name__ == '__main__':
    tool=MySqlTools(db='test123',user='root',password='123456',host='localhost',port=3306,charset='utf8')
    print(tool.get('select * from student where name="zhang3" '))

