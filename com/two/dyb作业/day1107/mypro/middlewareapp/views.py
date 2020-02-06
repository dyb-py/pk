from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

# 登录
def login(request):
    print('正在登陆',datetime.now())
    return render(request,'middlewareapp/login.html')


# 登录业务逻辑
def login_logic(request):
    print('login_logic 业务逻辑处理函数',datetime.now())
    name = request.POST.get('username')
    pwd = request.POST.get('userpwd')
    if name == 'liuzong' and pwd == '123':
        # 保存登录状态
        request.session['login'] = 'ok'
        print('login_logic视图函数',datetime.now())
        return HttpResponse('登录成功')
    return HttpResponse('登录失败')

# 欢迎
def welcome(request):
    print('这是welcome视图函数',datetime.now())
    # 登录状态验证

    return render(request,'middlewareapp/welcome.html')



'''
京东
我的个人中心 我的京豆  我的订单 我的购物车 。。。。。。 登录状态验证？？？？？？
'''