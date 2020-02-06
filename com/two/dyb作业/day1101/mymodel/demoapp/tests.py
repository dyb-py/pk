import os,django

from django.db.models import Min, Max, Count, Sum, Avg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mymodel.settings")
django.setup()

from demoapp.models import User,Employee

# all()
# 返回值：queryset对象 集合  所有model对象
# emps = Employee.objects.all()
# print(emps)

# get()
# 返回值： model对象
# 注意：查询结果只能有一个对象，则正常查询；如果查询不到，或者查到多个，都报错
# emp =  Employee.objects.get(age=18)
# print(emp)

# filter()
# 返回值：queryset  元素 - model对象
# emp = Employee.objects.filter(id__gte=1,age=18)
# print(emp)

# count()
# rst = Employee.objects.count()
# rst = Employee.objects.all().count()
# rst = Employee.objects.filter(id__gte=2).count()
# print(rst)

# exclude()
# rst = Employee.objects.exclude(id=1)
# print(rst)

# first() last
# rst1 = Employee.objects.first()
# rst2 = Employee.objects.last()
# print(rst1,rst2)


# order_by()
# rst = Employee.objects.order_by('age','-name')
# print(rst)

# 模糊查询
# contains() icontains()
# startswith() istartswith endswith()
# rst = Employee.objects.filter(name__icontains='xin')
# rst = Employee.objects.filter(name__istartswith='x')
# print(rst)


# 范围查询
# rst = Employee.objects.filter(age__in=(18,20,37))
# rst = Employee.objects.filter(age__range=(18,29))
# # print(rst)

# 判断是否为空值
# rst = Employee.objects.filter(salary1__isnull=True)
# print(rst)

# values()
# 返回值：queryset  元素-字典
# rst = Employee.objects.values()
# rst = Employee.objects.filter(id__lte=5).values('name','age')
# print(rst)

# 聚合函数
# aggregate() 返回值 字典  键值对
# rst = Employee.objects.filter(id__lte=5).aggregate(Max('age'),Min('age'),Avg('age'),Sum('id'),Count('id'))
# rst = Employee.objects.filter(id__lte=5).aggregate(Min('age'),Avg('age'),Sum('id'),Count('id'),max1=Max('age'))
# print(rst)

# 分组查询
# rst1 = Employee.objects.filter(id__lte=6).values('department')
# rst2 = Employee.objects.filter(id__lte=6).values('department').annotate(Max("salary1"))
# print(rst1)
# print(rst2)

#
# rst1 = Employee.objects.values("age").annotate(Min('salary1') ,p = Max('id'))
# rst2 = Employee.objects.values("age").annotate(Min('salary1') ,p = Max('id')).filter(p__gt=3)
# print(rst1)
# print(rst2)

# annotate() 返回值 queryset  元素-字典  键值对 分组字段，分组统计聚合函数
# print(User.objects.values('age').annotate(Count('age')))
# print(Employee.objects.values('age').annotate(Count('age')))