from datetime import datetime

from django.shortcuts import render
from requestapp.models import User

# Create your views here.

def index(request):
    name = '孙哥'
    now = datetime.now()
    list1 = [10,20,30,40]
    list2 = [[1,2,3],[4,5,6],[7,8,9]]
    list3 = []
    dict1 = {'name':'孙哥','age':18}
    users = User.objects.all()
    return render(request, 'requestapp/index.html',{'name':name,'time':now,'list':list1,'dict':dict1,'users':users,'list1':list2,'list2':list3})

def base(request):
    return render(request,'requestapp/base.html')


def sub1(request):
    return render(request,'requestapp/sub1.html')

def sub2(request):
    return render(request,'requestapp/sub2.html')