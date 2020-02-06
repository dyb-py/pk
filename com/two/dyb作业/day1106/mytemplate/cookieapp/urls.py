from django.urls import path


from cookieapp import  views

app_name = 'cookieapp'

urlpatterns = [
    path('index/',views.index,name='index')
]