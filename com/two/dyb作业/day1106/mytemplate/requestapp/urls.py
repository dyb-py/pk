from django.urls import path


from requestapp import  views

app_name = 'requestapp'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('sub1/',views.sub1,name='sub1'),
    path('sub2/',views.sub2,name='sub2'),
]