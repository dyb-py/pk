from django.http import HttpResponse
from django.shortcuts import render
from demoapp.models import User
# Create your views here.
# 视图函数 v 控制器
def queryfn(request):
    # 查询数据库表 user  连接数据库 Connect() cursor() excute()
    rst = User.objects.all()
    # print(rst)
    for obj in rst:
        print(obj.name)
    return HttpResponse('查询数据成功')


