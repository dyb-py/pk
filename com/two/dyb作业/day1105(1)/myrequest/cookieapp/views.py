from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 视图函数 设置cookie
def setcookie(request):
    res = HttpResponse('设置cookie')
    # cookie 默认 存活时间是 session
    # 如果有需要，max_age进行 生命时间 设置
    name = '刘海涵'.encode('utf-8').decode('latin-1')
    res.set_cookie('name',name,max_age=60*60*24*10)
    return res


# 读取cookie
def getcookie(request):
    print(request.COOKIES)  #  request.POST /GET 接收参数数据  method  请求方式
    # print(request.COOKIES['name']) 键不存在，直接报错 不推荐
    print(request.COOKIES.get('name').encode('latin-1').decode('utf-8'))
    return HttpResponse('读取cookie')
