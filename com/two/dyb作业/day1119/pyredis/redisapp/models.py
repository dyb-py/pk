from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    birthday = models.DateTimeField()

'''
添加数据
    - 1.直接在数据库操作
    - 2.User.objects.create() User() save()
    - 3.前端页面 传递数据
'''