import day12_mysql的封装.mysqltool01 as  t
import day12_mysql的封装.mysqltool02 as t2
import day12_mysql的封装.mysqltool03 as t3

# 查询数据库所有学生数据
# tools=t.MySqlTools(db='test123',user='root',password='123456',host='localhost',port=3306,charset='utf8')
# print(tools.get('select * from student'))
#
# tools=t2.MySqlTools(db='test123',user='root',password='123456',host='localhost',port=3306,charset='utf8')
# print(tools.get('select * from student'))

# tools=t3.MySqlTools(db='test123',user='root',password='123456',host='localhost',port=3306,charset='utf8')
# # tools.add('student',{'name':'xiaoxiaobo','age':1,'sex':'1'})
# # tools.delete('student',{'name':'xiaoxiaobo','age':1})s
# # tools.modify('student',{'sex':'0'},{'name':'xiaobo'})
# print(tools.get('student', ['*']))

import day12_mysql的封装.settings as s

print(s.hehe)
