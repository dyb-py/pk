from django.urls import path

from uploadapp import views

app_name = 'uploadapp'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('formlogic/',views.form_logic,name='formlogic'),
    path('query/',views.query,name='query'),

]