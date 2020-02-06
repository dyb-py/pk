from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from redisapp.models import User
# Create your views here.
# @cache_page(timeout=100,key_prefix='1119')
def query(request):
    users = User.objects.all()
    request.session['panpan'] = 'xiaomianbao'
    return render(request,'redisapp/query.html',{'users':users})


# 数据 更新
def update(request):
    age = request.GET.get('age')
    user1 = User.objects.get(pk=2)
    user1.age = age
    user1.save()
    # 删除缓存
    # keys = cache.keys("*1119*")
    # print(keys)
    # 方式一
    # for key in keys:
    #     cache.delete(key)
    # 方式二：
    # cache.delete_many(keys)
    # 方式三：
    # cache.delete_pattern('*1119*')
    # 方式四：
    # cache.clear()
    return HttpResponse('修改成功')


# 获取 读session
def getsession(request):
    print(request.session.get('login'))
    return HttpResponse('读取session')