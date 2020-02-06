from django.db import models

# Create your models here.

# 创建model创建
# 关联关系
'''
关系：
    - 一对多
    - 一对一
    - 多对多 
'''

# 一对多
# 员工表  部门表
class Department(models.Model):
    name = models.CharField(max_length=20)
    note = models.CharField(max_length=20)

    class Meta:
        db_table = 't_department'


# 员工表 从表
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # 部门id
    # protect 受保护 不允许删除
    # cascade 级联删除 主表删除 从表数据跟随删除
    # SET_NULL 主表删除 从表数据 外键 null
    # dept = models.ForeignKey(to=Department,on_delete=models.SET_DEFAULT,null=True,default=99)
    # SET()
    dept = models.ForeignKey(to=Department,on_delete=models.SET(99),null=True)

    class Meta:
        db_table = 't_employee'


# 一对一
# 人 护照
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = 't_person'


# 胡招标 从表
class Passport(models.Model):
    name = models.CharField(max_length=20)
    # duration =
    # 设置 关联关系 人 表
    per = models.OneToOneField(to=Person,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 't_passport'



# 多对多
# 一对多
# 学生  课程
class Student(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 't_student'


# 课程表 从表
class Course(models.Model):
    name = models.CharField(max_length=20)

    # 设置 关联关系
    stu = models.ManyToManyField(to=Student)

    class Meta:
        db_table = 't_course'