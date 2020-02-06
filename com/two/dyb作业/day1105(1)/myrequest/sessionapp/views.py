from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

# 设置session
def setsession(request):
    # 设置 session 字典
    request.session['name'] = '刘总'
    request.session['pwd'] = '123'
    return HttpResponse('设置session')


# 读取session
def getsession(request):
    10/0
    rst = request.session.get('name')
    print('name',rst)
    rst1 = request.session.get('pwd')
    print('pwd',rst1)
    # return HttpResponse('获取session')
    return redirect('set')


# 删除session
def delesession(request):
    # request.session.flush()  直接 强刷 删除
    # clear() 清除数据 session数据记录存在
    # request.session.clear()
    del request.session['name']
    return HttpResponse('删除session')


'''
强登 
    用户初次进行登录之后，记录登录状态 session 
    session 生命周期 会话 
    当前站点 退出 登录状态消失 即便没有关闭浏览器，当前站点 我的个人中心 我的订单 -登录

'''