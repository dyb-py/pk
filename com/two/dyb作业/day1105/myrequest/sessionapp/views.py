from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 设置session
def setsession(request):
    # 设置 session 字典
    request.session['name'] = 'liuzong'
    request.session['pwd'] = '123'
    return HttpResponse('设置session')


# 读取session
def getsession(request):
    rst = request.session.get('name')
    print(rst)
    return HttpResponse('获取session')


# 删除session
def delesession(request):
    return HttpResponse('删除session')