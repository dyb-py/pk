import MySQLdb

conn = MySQLdb.connect(
    db="spider",
    user="root",
    passwd="123456",
    host="localhost",
    port=3306,
    charset='utf8'
)
cursor = conn.cursor()
sql = "select count(ip) from ip_pool"
cursor.execute(sql)
print(cursor.fetchone()[0])