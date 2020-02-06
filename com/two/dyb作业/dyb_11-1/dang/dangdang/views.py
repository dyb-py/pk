from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def tushu(request):
    return render(request,'dangdang.html')

# def dang(request,id):
#     if id=='1':
#         print(id)
#         return HttpResponse('第一本书')
#     if id=='2':
#         print(id)
#         return HttpResponse('第二本书')
def dang(request):
    id=request.GET.get('id')
    if id == '1':
        return HttpResponse('第一本书')
    if id=='2':
        return HttpResponse('第二本书')