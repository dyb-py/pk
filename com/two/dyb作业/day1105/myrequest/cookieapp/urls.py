from django.urls import path

from cookieapp import views
urlpatterns = [
    path('setcookie/',views.setcookie),
    path('getcookie/',views.getcookie),
]