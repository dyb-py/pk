import MySQLdb
conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='user',
    charset='utf8'
)
cur=conn.cursor()
sql='select * from shop_user'
p=cur.execute(sql)
# print(p)
# print(cur.fetchone())
# print(cur.fetchmany(2))
# print(cur.fetchall())

# conn.begin()
# cur=conn.cursor()
# np=[['a1','22222'],['a2','333333'],['a3','333334444']]
# for i in np:
#     print(i[0],i[1])
#     sql="insert into shop_user(name,password)values('%s','%s')"%(i[0],i[1])
#     cur.execute(sql)
# conn.commit()

# cur=conn.cursor(MySQLdb.cursors.DictCursor)
# sql='select * from shop_user where id<1001'
# cur.execute(sql)
# print(cur.fetchall())

# cur=conn.cursor()
# sql='select * from shop_user'
# cur.execute(sql)
# print(cur.fetchmany(2))
# print(cur.fetchall())
# cur.scroll(2,mode='absolute')
# print(cur.fetchall())
# cur.scroll(-1,mode='relative')
# print(cur.fetchall())

# cur=conn.cursor()
# username='asasasa'
# # password='12221'
# password="' or '1'='1"
# sql="select * from shop_user where username='%s' and password='%s'"%(username,password)
# cur.execute(sql)
# print(cur.fetchall())

# cur=conn.cursor()
username='dd'
password='12221'
# password="' or '1'='1"
# sql="select * from shop_user where username=%s and password=%s"
# cur.execute(sql,[username,password])
# print(cur.fetchall())

# sql="select * from shop_user where username=%(username)s and password=%(password)s"
# cur.execute(sql,{'username':username,'password':password})
# print(cur.fetchall())

d={'username':username,'password':password}
s='heeeee a%(username)s ass'%d
print(s)
s='heeeee a{0[username]} ass'.format(d)
print(s)
