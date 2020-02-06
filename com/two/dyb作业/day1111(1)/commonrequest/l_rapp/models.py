from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)


'''
1.创建 model
2、生成迁移记录并应用到数据库
3.mysql数据库去做查询 表  
    - sqlite3 数据表 sqlite export 
'''