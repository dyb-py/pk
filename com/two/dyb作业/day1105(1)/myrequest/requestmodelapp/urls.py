
from django.urls import path
from requestmodelapp import views

app_name = 'requestmodelapp'
urlpatterns = [
    path('register/',views.register),
    path('login/',views.login,name='login'),
    path('registerlogic/',views.register_logic,name='registerlogic'),
    path('loginlogic/',views.login_logic,name='loginlogic'),
    path('welcome/',views.welcome,name='welcome'),
]