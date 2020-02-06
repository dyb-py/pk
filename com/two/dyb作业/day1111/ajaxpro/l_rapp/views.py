import time

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from l_rapp.models import User
# Create your views here.

# 创建视图函数
# login
# register
def register(request):
    # rst = request.GET.get('msg')
    # print(rst)  # 验证是否能接受到
    return render(request,'l_rapp/register.html')

# 注册到数据库表中
def register_logic(request):
    name = request.POST.get('username')
    pwd = request.POST.get('userpwd')
    # 添加到数据表中  该用户名已存在？？
    try:
        with transaction.atomic():
            User.objects.create(name=name,pwd=pwd)
            return HttpResponse('注册成功')
    except:
        return HttpResponse('注册失败')




def login(request):


    return render(request,'l_rapp/login.html')


def login_logic(request):
    name = request.POST.get('username')
    pwd = request.POST.get('userpwd')

    rst = User.objects.filter(name=name,pwd=pwd)
    print(rst)
    return HttpResponse('登录成功')



# 验证 用户名 视图函数
def check_name(request):
    # print('验证用户名')
    name = request.GET.get('name')
    print(name)
    # time.sleep(100)
    # 连接数据库 进行验证
    if name == 'sunge':
        return HttpResponse('用户名已存在')
    else:
        return HttpResponse('用户名可用')