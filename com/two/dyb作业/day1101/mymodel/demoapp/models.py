from django.db import models

# Create your models here.

# 创建model类
class User(models.Model):
    # 内部创建 属性  充当角色 表中 字段
    # id =
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    birtday = models.DateTimeField()


# 创建model类 员工类
class Employee(models.Model):
    name = models.CharField(max_length=20,default='xinxin') # default默认参数 django添加数据时起效
    age = models.SmallIntegerField(db_index=True)
    sex = models.BooleanField(db_index=True)  # 接收参数值 TrueFalse
    salary1 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    department = models.SmallIntegerField(db_column='dept',default=2)
    worktime = models.DateField(null=True,unique=True)

    class Meta:
        db_table = 'employee'
        ordering = ['age','name']