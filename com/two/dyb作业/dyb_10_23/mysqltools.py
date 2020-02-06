from com.two.dyb作业.dyb_10_23 import *
# from --- import  __all__
# 使用导包时：本质在调用 __init___.py文件

# version4.0
class MySqlTools(object):

    # 初始化方法
    def __init__(self,*,db,user,password,host='localhost',port=3306,charset='utf8'):
        '''
        初始化方法
        MySQLTools(db=db,user=user,*)
        :param db: 数据库名  --> str   str类型
        :param user: 用户名 --> str
        :param password: 密码 --> str
        :param host: 主机IP --> str
        :param port: 端口号 --> int
        :param charset: 字符编码 --> str
        '''
        self.__db=db
        self.__user=user
        self.__password=password
        self.__host=host
        self.__port=port
        self.__charset=charset

    # 连接数据库
    def _conntion(self):  # 希望在当前文件下使用（可以被其他类使用），不希望其他的模块使用  _a  受保护的
        '''
        内部使用的创建数据库连接
        :return:
        '''
        self.conn = MySQLdb.connect(db=self.__db, user=self.__user, password=self.__password,
                                    host=self.__host, port=self.__port, charset=self.__charset)
        # 创建游标
        self.cursor = self.conn.cursor()

    # 释放资源
    def _close(self):
        '''
        内部使用的释放资源
        :return:
        '''
        self.cursor.close()
        self.conn.close()

    #  增加
    # @staticmethod
    # def add_one_data():  # PEP8:规定了Python的书写规范           PEP:python开发增强建议书
    #     conn = MySQLdb.connect
    #     print(conn)
    def add(self,table,data): # 'insert into TABLE (C1,C2...) values （V1，V2...）'
        '''
        1. 文字： 给table表 添加 data数据
        2. 用法： MySqlTools().add(table,data)
        :param table:  表名 --> str
        :param data: 插入的数据--->dict
        :return:
        '''

        # 连接数据库
        self._conntion()

        # # 构建sql语句 --- 字典：无序 无法下标对应
        # key=','.join(data.keys())
        # print(key)
        # values=','.join(data.values())

        keys=[]
        values=[]
        try:
            for i in data.items():
                keys.append(i[0])
                values.append(self._deal_data(i[1]))

            sql='insert into {table} ({key}) values ({value})'.format(table=table,
                                                                  key=','.join(keys),
                                                                  value=','.join(values))
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            self._close()

    # 创建处理数据的方法：
    def _deal_data(self,data):

        'insert into student (name,age,sex) values （"xiaoxiaobo",1,1）'
        if isinstance(data,str):
            return "'{data}'".format(data=data)

        elif isinstance(data,dict):
            temp=[]
            for key,value in data.items():
                value=self._deal_data(value) # 只要涉及sql语句中的值，必须进行处理
                res='{key}={value}'.format(key=key,value=value)
                temp.append(res)
            return temp
        else:
            return str(data)
    # 删除
    def delete(self,table,condition):
        '''

        :param table: --> str
        :param condition: --->dict
        :return:
        '''
        # sql" 'delete from TABLE where （KEY=VALUE and KEY=VALUE）'
        # 连接数据库
        self._conntion()
        # 构建sql
        # condition： {key:value,key:value} --- KEY=VALUE and KEY=VALUE
        try:
            # 条件格式化
            condition=' and '.join(self._deal_data(condition))
            sql='delete from {table} where ({condition})'.format(table=table,condition=condition)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print('错了')
        finally:
            self._close()

    # 修改
    def modify(self,table,data,condition=None):
        '''

        :param table: str
        :param data:  dict
        :param condition:  dict
        :return:
        '''
        'update Table set (key1=value1,key2=value2...) where (kk1=vv1 and kk2=vv2) '
        self._conntion()

        try:
            # 处理数据
            data=','.join(self._deal_data(data))  # ['k=v','k=v']
            if condition:
                # 处理condition
                condition=' and '.join(self._deal_data(condition))
                sql='update {table} set {data} where ({condition})'.format(table=table,
                                                                            data=data,
                                                                            condition=condition)
            else:
                sql='update {table} set {data}'.format(table=table,data=data)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print('错了')
        finally:
            self._close()

    # 查询
    def get(self,table,data,condition=None,get_one=False):
        '''

        :param table: str
        :param data: list
        :param condition: dict
        :param get_flag: 1 | 0
        :return:
        '''
        'select k1,k2...  from Table where CONDITION'
        self._conntion()
        try:
            data=','.join(data)
            if condition:
                # 处理condition
                condition = ' and '.join(self._deal_data(condition))
                sql = 'select {data} from {table} where {condition}'.format(table=table,
                                                                             data=data,
                                                                             condition=condition)
            else:
                sql = 'select {data} from {table}'.format(table=table, data=data)
            self.cursor.execute(sql)
            if get_one:
                r=self.cursor.fetchone()
            else:
                r=self.cursor.fetchall()
        except:
            print('出错了')
        finally:
            self._close()
        return r

    # 利用工厂函数： 使用方法或函数创建对象  节省资源
    @classmethod
    def get_tool(cls):
        #
        # def fun(**kwargs):
        #     kwargs: {'a':1,'b':2,'c':3}
        #     **kwargs:a=1,b=2,c=3
        # fun(a=1,b=2,c=3)
        #
        #
        cp=loader.CPTools()
        data={
            'db' : cp.get_config('DATA','db'),
            'user' : cp.get_config('DATA','user'),
            'password' : cp.get_config('DATA','password'),
            'host' : cp.get_config('DATA','host'),
            'port' : int(cp.get_config('DATA','port')),
            'charset' : cp.get_config('DATA','charset')}
        def check_connection():
            try:
                conn=MySQLdb.connect(**data)
                #连接成功
            except Exception as e:
                print(e)
                return False
            else:
                # 创建工具对象
                conn.close()
                return True

        if check_connection():
            return cls(**data)
        else:
            print('连接失败')


if __name__ == '__main__':
    # tool=MySqlTools(db='test123',user='root',password='123456',host='localhost',port=3306,charset='utf8')
    # # print(tool.get('select * from student where name="zhang3" '))
    # # tool.add('hehe',{'name':'hehe','age':18,'sex':'1'})
    # del tool
    tool=MySqlTools.get_tool()
    print(tool.get('movie', ['*']))