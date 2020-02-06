from django.urls import path

from sessionapp import views

# 命名空间 给每个app设置自己单独的名字 标识当前app
app_name = 'sessionapp'
urlpatterns = [
    path('setsession/',views.setsession,name='set'),
    path('getsession/',views.getsession),
    path('delesession/',views.delesession),
]