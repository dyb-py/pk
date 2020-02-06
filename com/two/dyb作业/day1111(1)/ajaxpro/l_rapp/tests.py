import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ajaxpro.settings")
django.setup()


from l_rapp.models import User

# 测试
import json

# 序列化工作  python 数据类型
# list1 = [10,20,30,40]
# dict1 = {'name':'liuzong','age':18}
# boo1 = True  true
# specialT = None
# rst = json.dumps(specialT)
# print(rst, type(rst))

# model对象
users = User.objects.all()
# 序列化工作 返回 序列化之后对象
# def mydefault(u):
#     print(u)
#     if isinstance(u,User):
#         return {'id':u.id,'name':u.name,'pwd':u.pwd}
# rst = json.dumps(list(users),default=mydefault)
# print(rst,type(rst))

