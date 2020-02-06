import time

from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from l_rapp.models import User
# Create your views here.
import json

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


# query 模板文件 调度
def query(request):
    return render(request,'l_rapp/query.html')


def mydefault(u):
    print(u)
    if isinstance(u, User):
        return {'id': u.id, 'name': u.name, 'pwd': u.pwd}

# 调度 model 完成 数据获取工作
def query_logic(request):
    # 接收请求，返回响应 表中数据
    # 第一种：直接 返回响应 httpresponse() model对象 queryset对象 不可行
    # rst = User.objects.all()
    # print(rst)
    # return HttpResponse(rst[0])

    # 第二种 换格式  非官方
    # rst = User.objects.all()
    # s1 = ''
    # for user in rst:
    #     s1 += str(user.id) + ','
    #     s1 += user.name + ','
    #     s1 += user.pwd + ','
    # return HttpResponse(s1)

    # 第三种： render() 不推荐 大量冗余代码
    # rst = User.objects.all()
    # return render(request,'l_rapp/index.html',{'users':rst})

    # 第四种：xml 数据传输格式 <users><user><name>user.name<name><pwd>user.pwd<pwd><user></users>
    # < users > < user > < name > user.name < name > < pwd > user.pwd < pwd > < user > < / users >
    # return HttpResponse(rst)
    # 原生app开发  html css js 解析
    # 当前 最新数据传输格式  xml 很传统处理方式
    # json

    # 第五种：json 数据传输格式
    # dict1 = {'name': 'liuzong', 'age': 18}
    # rst = json.dumps(dict1)
    # print(rst)
    # users = User.objects.all()
    # rst = json.dumps(list(users), default=mydefault)
    # print(rst, type(rst))
    # return HttpResponse(rst)



    # jsonresponse对象
    users = User.objects.all()
    return JsonResponse({'users':list(users)},json_dumps_params={'default':mydefault})


'''
对比：
    Jsonresponse() 直接返回响应 无需使用HTTPRESPONSE()
    Jsonresponse() 同时具备json序列化 工作
    Jsonresponse() 传输 json对象
    
'''

# 分别对应 视图demo
def demo1(request):
    return render(request,'l_rapp/demo1.html')

def demo2(request):
    return render(request,'l_rapp/demo2.html')

def demo3(request):
    return render(request,'l_rapp/demo3.html')