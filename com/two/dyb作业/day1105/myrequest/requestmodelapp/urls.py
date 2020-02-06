
from django.urls import path
from requestmodelapp import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('registerlogic/',views.register_logic),
    path('loginlogic/',views.login_logic),
    path('welcome/',views.welcome),
]