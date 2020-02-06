import MySQLdb
class MyDbTool():
    def __init__(self,*,host,port,user,password,db,charset):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset
    def conntion(self):
        # 连接数据库
        self.conn = MySQLdb.connect(db=self.db, user=self.user, password=self.password,
                                    host=self.host, port=self.port, charset=self.charset)
        # 创建游标
        self.cursor = self.conn.cursor()
    def add(self,sql):
        self.conntion()
        self.cursor.execute(sql)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        # 删除
        def delete(self, sql):
            # 连接数据库：
            self.conntion()
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

        # 修改
        def modify(self, sql):
            # 连接数据库：
            self.conntion()
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

        # 查询
        def get(self, sql):
            # 连接数据库：
            self.conntion()
            self.cursor.execute(sql)
            r = self.cursor.fetchall()
            self.cursor.close()
            self.conn.close()
            return r

if __name__ == '__main__':
    tool = MyDbTool(db='test123', user='root', password='123456', host='localhost', port=3306, charset='utf8')
    print(tool.get('select * from student'))



