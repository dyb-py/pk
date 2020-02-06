
# 查询工作
# Employee类
from sqlalchemy import and_, or_, desc, asc, func

from app import db
from models import Employee, Department, Emp, Student, Course, Person, Passport

# print(Employee.query)
# basequery 基础查询   django查询 queryset
# print(type(Employee.query))

# 1.all()  返回值 列表 所有的 model对象
# rst = Employee.query.all()
# print(rst)

# 2.get()  限制 只能为 主键查询 直接把主键值传入即可
# 返回值：model对象  如果没有查询到，None
# rst = Employee.query.get(7)
# print(rst)

# 3.filter_by() 只用来进行等值查询
# rst =  Employee.query.filter_by(id = 1).all()
# print(rst)

# 4.filter()
# rst = Employee.query.filter(Employee.id == 1).all()
# rst1 = Employee.query.filter(Employee.id >= 1).all()
# # rst2 = Employee.query.filter(Employee.id <= 1).all()
# # rst3 = Employee.query.filter(Employee.id != 1).all()
# # # print(type(rst))
# # print(rst1)
# # print(rst2)
# # print(rst3)

# and_() 表示 且  等同于 默认情况下逗号隔开
# rst = Employee.query.filter(Employee.id >= 1,Employee.age >= 19).all()
# rst = Employee.query.filter(and_(Employee.id >= 1,Employee.age >= 19)).all()
# not_()
# rst = Employee.query.filter(or_(Employee.id >= 3,Employee.age < 19)).all()
# ~ 表示 非 建议 把表达式 括号 括起来
# rst = Employee.query.filter(~(Employee.id >= 3)).all()
# print(rst)
# in_()
# rst = Employee.query.filter(Employee.age.in_((18,20,22,25),)).all()
# rst = Employee.query.filter(Employee.age.between(19,21)).all()
# rst = Employee.query.filter(Employee.age == None).all()
# rst = Employee.query.filter(Employee.age != None).all()
# print(rst)

# basequery 常用查询方法
# one() 只会查找到一个model对象。如果查找到多个，或者 是 没有，直接报错
# rst = Employee.query.filter(Employee.age == 30).one()
# print(rst)
# first() 获取到 basequery中第一个对象   如果没有，直接 None
# rst = Employee.query.filter(Employee.age == 30).first()
# print(rst)

# one_or_none()
# 返回值 None  获取某一个model对象
# rst = Employee.query.filter(Employee.age != None).one_or_none()
# print(rst)


# count() 数量
# print(Employee.query.count())

# 支持切片
# emps = Employee.query.all()[1:]
# emps = Employee.query[1:]
# print(emps)

# 查询 db
# Employee.query 属性 BASEquery对象
# query1 = db.session.query(Employee)
# print(query1)
# print(type(query1))
# 返回值：列表 all() 元素-元素（查询指定的字段）
# query1 = db.session.query(Employee.id,Employee.name)
# print(query1)


# 排序
# rst = db.session.query(Employee).order_by(Employee.age).all()
# rst = db.session.query(Employee).order_by(Employee.age,Employee.salary).all()
# rst = db.session.query(Employee).order_by(Employee.age,desc(Employee.salary)).all()
# print(rst)
#
# rst = db.session.query(Employee).order_by(asc(Employee.age),desc(Employee.salary)).all()
# print(rst)

# 聚合函数
# rst = db.session.query(
#     func.max(Employee.id),
#     func.min(Employee.id),
#     func.sum(Employee.id),
#     func.avg(Employee.id),
#     func.count(Employee.id),
# ).all()
# print(rst)

# 分组统计
# 以年龄分组，统计每组人数
# rst = db.session.query(func.count(Employee.id),Employee.age).group_by(Employee.age).all()
# print(rst)

# rst = db.session.query(func.count(Employee.id),Employee.age).group_by(Employee.age).having(func.min(Employee.id)<3).all()
# print(rst)

# 数据 更新 增加 删除
# emp1 = Employee.query.get(1)
# # 能获取到对象 first() one() one_or_none() get()
# emp1.age = 38
# db.session.commit()

# 增加
# emp = Employee(id=8,name='zhengjiahao',age=21)
# db.session.add(emp)
# db.session.commit()

# emp1 = Employee(id=9,name='tongzhongjie',age=22)
# emp2 = Employee(id=10,name='likaixuan',age=22)
# db.session.add_all([emp1,emp2])
# db.session.commit()

# 删除
# emp1 = Employee.query.get(10)
# db.session.delete(emp1)
# db.session.commit()

# 分页
# pag = db.session.query(Employee).paginate(page=3,per_page=2)
# print(pag)
# print(pag.query.all())

# print()
# rst = pag.iter_pages()
# for i in rst:
#     print(i)

# print(pag.has_next) # 是否有下一页 True True
# print(pag.has_prev) # 是否有上一页  False  True
# print(pag.next_num) # 下一页页号  2   3
# print(pag.prev_num) # 上一页页号 None  1
#
# print(pag.pages)  # 共有多少页  5
# print(pag.items)  # 当前页的数据  MODEL 3 4
# print(pag.total)  # 共有多少行 整个表中所有的数据行 9
# print(pag.per_page) # 每页几行

# 后端 查看属性
# 传给html文件 分页接收


# 一对多关系 进行 同时 主从 添加数据
# dept = Department(id=1,title='睡觉部')
# emp = Emp(id=1,name='刘锟')
# print(dept.employees)
# dept.employees.append(emp)
# db.session.add(dept)
# db.session.commit()

# 添加一方
# dept = Department.query.get(2)
# emp = Emp(id=2,name='玲玲')
# dept.employees.append(emp)
# db.session.commit()

#
# dept = Department.query.get(2)
# emp = Emp(id=3,name='孙哥')
# emp.dept = dept
# db.session.commit()

# 删除 主表
# dept = Department.query.get(4)
# db.session.delete(dept)
# db.session.commit()

# 主从查询
# dept = Department.query.get(2)
# # 部门5 对应的 员工信息
# print(dept.employees.all())
# 查询 玲玲 所在的部门
# emp = Emp.query.get(2)
# print(emp.dept) # dept model对象  emp.dept = dept

# 表链接查询
# print(Department.query.join(Emp).all())
# print(Emp.query.join(Department).all())
# 保留双方数据
# print(db.session.query(Department,Emp).join(Emp).all())


# lazy选项
# dept = Department.query
# print(dept)
# # print(dept[0])
# emps = dept[0].employees
# print(emps)  # sql语句
# # print(emps.all())


# 多对多关系
# 添加数据
#
# student = Student(id=1,name='李泽军')
# course = Course(id=1,title='FLASK',expire=4)
# # 给学生添加课程
# student.courses.append(course)
# # student对象添加
# db.session.add(student)
# db.session.commit()

# student = Student(id=2,name='张文婷')
# course = Course(id=2,title='MySQL',expire=4)
# # 给课程添学生
# course.stu.append(student)
# db.session.add(course)
# db.session.commit()

# 添加一方
# 学生 1 2  课程 1 2  1 -1 2-2
# 学生2 课程1
# student = Student.query.get(2)
# course = Course.query.get(1)
# student.courses.append(course)
# db.session.commit()

# 给 课程2 添加学生1
# student = Student.query.get(1)
# course = Course.query.get(2)
# course.stu.append(student)
# db.session.commit()

# 查询数据
# 通过一方 查另一方
# 学生1   所有课程
# student = Student.query.get(1)
# print(student.courses.all())
# 查询课程1 所选的学生
# course = Course.query.get(1)
# print(course.stu.all())

# 联合查询
#
# print(Student.query.join(Course.stu).all())
# # print(db.session.query(Student))
# print(db.session.query(Course).join(Student.courses).all())
# print(db.session.query(Course).join(Student.courses).all())
# 查询 学生1 的 课程信息 以及 该学生信息
# select s.id,s.name,c.title,c.expire from student as s join student_course as sc on s.id = sc.student_id join course as c on c.id=sc.course_id where s.id=1;
# rst = db.session.query(Student,Course).join(Course.stu).filter(Student.id==1).all()
# print(rst)

# 删除数据
# course = Course.query.get(1)
# db.session.delete(course)
# db.session.commit()

# 一对一 关系 添加数据
# person = Person(id=1,name='刘总')
# port = Passport(id=1,title='Austrilia')
# person.port = port
# db.session.add(person)
# db.session.commit()

# person = Person(id=2,name='路总')
# port = Passport(id=2,title='Africa')
# port.per = person
# db.session.add(port)
# db.session.commit()

# 添加一方数据
# 给 盼盼 添加 护照信息
# person = Person.query.get(3)
# port = Passport(id=4,title='Burma')
# person.port = port
# db.session.commit()

# # 给 护照 泰国 添加一个人 欣欣
# port1 = Passport.query.get(3)
# person = Person(id=4,name='欣欣')
# port1.per = person
# db.session.commit()

# 删除 主表
# person = Person.query.get(4)
# db.session.delete(person)
# db.session.commit()

# 查询 通过一方查另一方
# person = Person.query.get(1)
# print(person.port)
# p1 = Passport.query.get(1)
# print(p1.per)

# 联合查询
# print(db.session.query(Person,Passport).join(Passport).all())
# print(db.session.query(Person.name,Passport.title).join(Passport).filter(Person.id >= 2).all())
