

# 定义model类
from sqlalchemy import UniqueConstraint, Index

from app import db


# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(20),nullable=True)
#     age = db.Column(db.SmallInteger)

class Employee(db.Model):
    # __tablename__ = 't_employee'
    id = db.Column('identifier',db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=True)
    age = db.Column(db.SmallInteger,index=True)
    salary = db.Column(db.Numeric(7,2))
    gender = db.Column(db.Boolean)
    birthday = db.Column(db.DateTime)
    dept = db.Column(db.Integer,default=1)
    # server_default参数值必须是字符串类型
    dept1 = db.Column(db.Integer,server_default='1')
    # 表 相关参数设置
    __table_args__ = (
        UniqueConstraint('name','birthday'),
        Index('salary','gender'),
    )


# 搭建 一对多 关联关系
class Department(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    # 主表中的 relationship用于搭建关联关系
    employees = db.relationship('Emp',backref='dept',lazy='dynamic')

class Emp(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    # 在从表中，定义外键，并指定主键的位置（数据库表中的字段）
    dept_id = db.Column(db.Integer,db.ForeignKey('department.id'))

# 第三方表
tags = db.Table(
    'student_course',
    db.Column('student_id',db.Integer,db.ForeignKey('student.id'),primary_key=True),
    db.Column('course_id',db.Integer,db.ForeignKey('course.id'),primary_key=True)
)

# 创建多对多
class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    # 建立 关联关系 设置 不会作用于 数据库表
    courses = db.relationship('Course',secondary=tags,backref=db.backref('stu',lazy='dynamic'),lazy='dynamic')

# 课程
class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    expire = db.Column(db.SmallInteger)


# 人 护照
class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    port = db.relationship('Passport',uselist=False,backref='per')

class Passport(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    per_id = db.Column(db.Integer,db.ForeignKey('person.id'))

