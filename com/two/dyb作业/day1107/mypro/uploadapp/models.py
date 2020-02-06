from django.db import models

# Create your models here.

# 创建model 用户上传信息 model
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    birthday = models.DateTimeField()
    headpic = models.ImageField(upload_to='imgs')
    # cssfile = models.FileField(upload_to='css')
#     如果之后 接收其他上传文件 css文件  upload_to 参数
