from datetime import datetime

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        print("init1")

    # view处理请求前执行
    def process_request(self, request):  # 某一个view
        # 进行 登录状态验证 工作
        # 之前是否有登录过，如果有，直接进入welcome，否则的话 重定向到 登录页面
        print("request:", request,datetime.now())
    #     request.path 监听请求路径  login   http://127.0.0,1:8000/loginlogic
        if 'login' not in request.path:  # True  False
            if request.session.get('login'):
                print('已经登陆',datetime.now())
            else:
                return redirect('middlewareapp:login')

    # view执行之后，响应之前执行
    def process_response(self, request, response):
        print("response:", request, response,datetime.now())
        return response  # 必须返回response
