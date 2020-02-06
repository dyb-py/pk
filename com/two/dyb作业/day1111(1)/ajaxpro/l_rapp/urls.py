from django.urls import path

from l_rapp import views

app_name = 'l_rapp'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('registerlogic/',views.register_logic,name='registerlogic'),
    path('login/',views.login,name='login'),
    path('loginlogic/',views.login_logic,name='loginlogic'),
    path('checkname/',views.check_name,name='checkname'),
    path('query/',views.query,name='query'),
    path('querylogic/',views.query_logic,name='querylogic'),
    path('demo1/',views.demo1,name='demo1'),
    path('demo2/',views.demo2,name='demo2'),
    path('demo3/',views.demo3,name='demo3'),
]