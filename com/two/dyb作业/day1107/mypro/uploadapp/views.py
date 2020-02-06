import uuid

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from uploadapp.models import User
import os.path
# Create your views here.

# index 视图函数
def index(request):
    return render(request,'uploadapp/index.html')

# 提交 逻辑函数

def form_logic(request):
    name = request.POST.get('username')
    age = request.POST.get('userage')
    birth = request.POST.get('userdate')
    # 针对文件 接收方式
    file = request.FILES.get('userfile')
    # uuid universally unique identifier 全球唯一标识符
    rst = str(uuid.uuid4()) + os.path.splitext(file.name)[1]
    # print(str(rst))
    # 重命名
    # 当前 文件 1.jpg字符串 splitext()
    file.name = rst
    # print(os.path.splitext(file.name))  # ('2', '.jpg')
    print(name,age,birth,file)
    # 数据 添加到数据库表
    User.objects.create(name=name,age=age,birthday=birth,headpic=file)
    return HttpResponse('接收成功')


# query 视图函数
def query(request):
    # 回传 user表数据
    number = request.GET.get('page')
    if number is None:
        number = 1
    users = User.objects.all()
    pagntor = Paginator(users,per_page=3)
    # print(pagntor.count) # 7  当前数据总条目
    # print(pagntor.num_pages) # 3  分页 总页数
    # print(pagntor.page_range) # range(1,4)  1 2 3
    print(pagntor.page(number)) #返回值：当前某页对象
    pg = pagntor.page(number)
    print(pg.object_list) # 返回值： 当前页上所有的model对象 queryset
    # # <QuerySet [<User: User object (8)>, <User: User object (9)>, <User: User object (10)>]>
    # print(pg.number) # 1 当前页码
    # print(pg.paginator) # Paginator object

    # 方法
    # print(pg.has_next()) # True
    # print(pg.has_previous()) # True
    # print(pg.has_other_pages()) # True
    # print(pg.next_page_number()) # 3
    # print(pg.previous_page_number()) # 1

    print(pg.start_index()) # 1    3条数据  4      7
    print(pg.end_index())  # 3              6      7

    return render(request,'uploadapp/query.html',{'page':pg})