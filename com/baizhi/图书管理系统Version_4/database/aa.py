import com.baizhi.图书管理系统Version_4.database.user_database
# import com.baizhi.图书管理系统Version_4.entity.user
import pickle
f=open(r'F:\pywork\com\baizhi\图书管理系统Version_4\database\user_db','rb')
userDB=pickle.load(f)  # 反序列化    将二进制文件转化成Python对象
f.close()
for i in userDB:
    print(i.name)