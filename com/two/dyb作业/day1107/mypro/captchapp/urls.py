from django.urls import path

from captchapp import views

app_name = 'captchapp'

urlpatterns = [
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('index/',views.index,name='index'),
    path('check/',views.check,name='check'),
]