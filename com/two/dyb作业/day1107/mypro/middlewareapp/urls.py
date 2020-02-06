from django.urls import path

from middlewareapp import views
app_name = 'middlewareapp'


urlpatterns = [
    path('login/',views.login,name='login'),
    path('loginlogic/',views.login_logic,name='loginlogic'),
    path('welcome/',views.welcome,name='welcome'),
]