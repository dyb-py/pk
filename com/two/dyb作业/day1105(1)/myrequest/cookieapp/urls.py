from django.urls import path

from cookieapp import views

app_name = 'cookieapp'
urlpatterns = [
    path('setcookie/',views.setcookie,name='set'),
    path('getcookie/',views.getcookie),
]