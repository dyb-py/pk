from django.http import HttpResponse
from django.shortcuts import render, redirect
from requestmodelapp.models import User
# Create your views here.

# 视图函数

# 注册 函数
def register(request):
    return render(request,'register.html')

# 注册 逻辑函数
def register_logic(request):
    print(request) # WSGIRequest cookies
    print(request.path) # /requestmodelapp/registerlogic/  请求路径
    print(request.method) # POST 请求方式  post get
#     接收数据 注册到数据库表
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
    elif request.method == 'GET':
        username = request.GET.get('username')
        userpwd = request.GET.get('userpwd')
#     注册到数据库表
    rst = User.objects.create(name=username,pwd=userpwd)
    if rst:
        # return HttpResponse('注册成功')
        # return render(request,'login.html')
        return redirect('/requestmodelapp/login/')
    else:
        return HttpResponse('注册失败')


# 登录函数
def login(request):
    # 调用login文件 记住我
    # 获取 cookie
    name = request.COOKIES.get('name')
    pwd = request.COOKIES.get('pwd')
    rst = User.objects.filter(name=name,pwd=pwd)
    if rst:
        request.session['login'] = 'ok'
        return redirect('/requestmodelapp/welcome/')
    else:
        return render(request,'login.html')

#
# 登录 逻辑函数
def login_logic(request):
#     接收数据
    username = request.POST.get('username')
    userpwd = request.POST.get('userpwd')
    # 通过 复选框 按钮 是否选中，来进行 记住我 业务操作
    # 如果 按钮为 选中，需要 记住我 业务操作
    # 业务：记住我，下次进行登录时，免登陆，直接进入到 系统首页
    # cookie设置  读取
    rem = request.POST.get('remember')
    print(rem)  # 选中 rem有值
#   登录验证
    rst = User.objects.filter(name=username,pwd=userpwd)
    if rst:
        # 保存登录状态
        # 设置 session、
        request.session['login'] = 'ok'
        res = redirect('/requestmodelapp/welcome/')
        # 设置cookie response对象生成
        if rem:
            res.set_cookie('name',username,max_age=7*24*60*60)
            res.set_cookie('pwd',userpwd,max_age=7*24*60*60)
        # return HttpResponse('登录成功')
        return res
    else:
        return HttpResponse('登录失败')


# 首页页面
# 发送首页请求时候，京东场景，首先判断，判断之前是否有登录状态，如果有直接进入首页，如果没有，强制登录
def welcome(request):
    rst = request.session.get('login')
    if rst:
        return render(request,'welcome.html')
    return redirect('/requestmodelapp/login/')