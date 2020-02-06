
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytemplate.settings")
django.setup()


from requestapp.models import User
import datetime


# 添加数据
# User.objects.create(name='sunge',age=18,salary=1234,birthday='2010-1-1')
# User.objects.create(name='sunjie',age=19,salary=12346,birthday='2010-1-1')
# User.objects.create(name='liuzong',age=20,salary=1235,birthday='2010-1-1')
# User.objects.create(name='luzong',age=21,salary=12345,birthday='2010-1-1')
# User.objects.create(name='xinxin',age=22,salary=12345,birthday='2010-1-1')
# User.objects.create(name='xiaolinlin',age=20,salary=1000,birthday='2010-1-1')