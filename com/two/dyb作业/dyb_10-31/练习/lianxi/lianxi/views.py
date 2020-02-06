from django.http import HttpResponse


# def login(request):
#     return HttpResponse('hello wowow')
from django.shortcuts import render


def login(request):
    return render(request,'login.html')


def regist(request):
    return render(request,'regist.html')