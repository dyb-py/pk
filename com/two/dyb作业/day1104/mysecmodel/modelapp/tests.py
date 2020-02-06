import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysecmodel.settings")
django.setup()

from modelapp.models import Employee,Department,Student,Course,Person,Passport


# 查询 一对一

# 1.只查一方数据   与 查询单表 一样
# 查询 护照为 中国的 护照信息
# p1 = Passport.objects.get(name='中国')
# print(p1.name,p1.id)
# 查询 名字 liuzong 的人 的信息
# p1 = Person.objects.get(name='liuzong')
# print(p1.name,p1.id,p1.age)


# 2.先查到一方，再查另一方
# 查询 护照为中国的护照信息
# p1 = Passport.objects.get(name='中国')
# # 对应的人的信息 年龄 姓名
# print(p1.per.age)
# print(p1.per.name)
# print(p1.per.id)

# 查询 liuzong 对应的 护照信息
# p1 = Person.objects.get(name='liuzong')
# print(p1.passport)  # passport对象
# print(p1.passport.name)
# print(p1.passport.id)


# 3.查询一方，同时以另一方作为查询条件
# 查询 护照为中国的 人的信息
# p1 = Person.objects.filter(passport__name='中国').values()
# print(p1)
# #  查询 liuzong 对应的 护照信息
# per1 = Passport.objects.filter(per__name='liuzong').values()
# print(per1)

# 4.查询 保留双方数据
# 查询 护照为中国的 人的信息以及护照信息
# p1 = Person.objects.filter(passport__name='中国').values('name','age','passport__name','passport__id')
# print(p1)
# #  查询 liuzong 对应的 护照信息 人
# pa1 = Passport.objects.filter(per__name='liuzong').values('name','per__name','per__age','per_id')
# print(pa1)

# ---------------------------------华丽丽的分割线-----------------------------------------

# 一对多查询 部门表 员工表

# 只查询一方数据
# 查询 员工表 huihui 员工信息
# emp = Employee.objects.filter(name='huihui').values()
# emp = Employee.objects.get(name='huihui')
# print(emp)

# 查询 部门 id=1 信息
# dep = Department.objects.filter(id=1)
# print(dep)

# 2.查询一方，然后再查另一方
# 查询 名字huihui
# emp = Employee.objects.get(name='huihui')
# # huihui对应的部门信息
# print(emp.dept) # 对应的 部门对象
# print(emp.dept.name) # 对应的 部门对象
# print(emp.dept.note) # 对应的 部门对象

# 查询 部门id=1  对应的 员工信息
# dep = Department.objects.get(id=1)
# print(dep.employee_set.all())  # model2 6
# print(dep.employee_set.values())  #

# 3.查询一方 以另一方为 查询条件
# 查询 员工表中名字huihui 的 部门信息
# dept = Department.objects.filter(employee__name='huihui').values()
# print(dept)
#
# # 查询 部门id=1  对应的 员工信息
# emp = Employee.objects.filter(dept__id=1).values()
# print(emp)

# 4.查询 保留双方数据
# 查询 名字为huihui的 部门信息  以及 员工信息
# dept = Department.objects.filter(employee__name='huihui').values('name','note','employee__name','employee__age')
# print(dept)
#
# # 查询 部门id=1  对应的 员工信息 以及 部门信息
# emp = Employee.objects.filter(dept__id=1).values('name','age','dept__name','dept__note')
# print(emp)

# 联合查询  会出现 重复
# depts = list(set(Department.objects.filter(employee__id__gt=2)))
# print(depts)


# -----------------------------------华丽丽的分割线-------------------------------------------------

# 多对多关系

# 1.只查询一方
# 查询 id =1 学生信息
# stu = Student.objects.filter(id=1)
# print(stu)
# # 查询 课程 mysql 课程的信息
# course1 = Course.objects.filter(name='mysql')
# print(course1)


# 2.查询一方 然后再查询另一方
# 查询 学生xuhao 学生
# stu = Student.objects.get(name='xuhao')
# # 课程信息
# # print(stu.course_set.all())
# print(stu.course_set)
#
# # 查询 wajueji 课程
# course1 = Course.objects.get(name='wajueji')
# # 对应的 学生
# # stu属性 角色  集合
# print(course1.stu.all())


# 3.查询一方 以另一方为 条件
# 查询 学生xuhao 学生 对应的 课程信息
# cour = Course.objects.filter(stu__name='xuhao').values()
# print(cour)
# # 查询 课程wajueji 的 学生信息
# stus = Student.objects.filter(course__name='wajueji').values()
# print(stus)


# 4.查询 保留双方数据
# cour = Course.objects.filter(stu__name='xuhao').values('name','stu__name','stu__id')
# print(cour)
# # 查询 课程wajueji 的 学生信息
# stus = Student.objects.filter(course__name='wajueji').values('name','course__name','course__id')
# print(stus)


# -------------------------------华丽丽的分割线----------------------------------------------

# 添加数据

# 一对一关系
# 1.添加 主表数据  与 操作 单表 一样
# 先创建对象 再添加  、   直接 create()
# Person.objects.create(name='wenjie',age=27)

# 2.为 已存在的 主表数据 添加从表数据  Passport表
# 方式一：
# p1 = Person.objects.get(name='jiarong')
# Passport.objects.create(name='叙利亚',per=p1)
# 方式二：
# p1.passport 一对一关系 不适用
# 部门表 员工表
# dept = Department.objects.get(id=1)
# dept.employee_set.create(name='haihan',age=3)

# 同时添加 主从数据
# 创建 两个对象 主 从
# dept = Department(name='睡觉部',note='休息')
# emp = Employee(name='wangjinghui',age=20)
# dept.save()
# emp.save()
# # 主 绑定 从数据  对于1:1不适用
# dept.employee_set.add(emp)

# 方式二： 普遍方式
# dept = Department(name='访谈部',note='秘密访谈')
# dept.save()
# emp = Employee(name='xiaoqiqi',age=200,dept=dept)
# emp.save()


# -------------------------------华丽丽的分割线-------------------------------------------------

# 删除
# 主表
# dept = Department.objects.get(id=1)
# dept.delete()

# -------------------------------华丽丽的分割线-------------------------------------------------

# 修改
# Department.objects.all()[0].name='baguabu'
# print(Department.objects.all()[0].name)
# Department.objects.all()[0].save()


# 查询
rst = Department.objects.all()
print(rst)