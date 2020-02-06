from django.urls import path

from demoapp import views

urlpatterns = [
    path('query/',views.queryfn),
]