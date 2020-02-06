from django.urls import path, re_path
from dangdang import views
urlpatterns = [
    path('tushu/',views.tushu),
    # path('dang/<id>/',views.dang),
    # re_path('dang/(\w{1})/',views.dang)
    path('dang/',views.dang)
]