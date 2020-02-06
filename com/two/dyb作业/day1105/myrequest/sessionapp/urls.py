from django.urls import path

from sessionapp import views
urlpatterns = [
    path('setsession/',views.setsession),
    path('getsession/',views.getsession),
    path('delesession/',views.delesession),
]