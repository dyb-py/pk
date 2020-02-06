from django.urls import path


from redisapp import views

app_name = 'redisapp'
urlpatterns = [
    path('query/',views.query,name='query'),
    path('update/',views.update,name='update'),
    path('getsession/',views.getsession,name='getsession'),
]