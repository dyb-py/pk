import random
import string

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 视图函数 生成验证码
from captchapp.captcha.image import ImageCaptcha


def getcaptcha(request):
    # 生成验证码captcha对象
    img = ImageCaptcha()
    # 生成 码 随机码
    rst = random.sample(string.ascii_letters+string.digits,5)
    print(rst) # ['L', '9', 'd', 'o', 'Y']
    code = ''.join(rst)
    print(code) # cK2BD
    # 设置session
    request.session['code'] = code
    data = img.generate(code)
    return HttpResponse(data,'image/png')


# 验证 逻辑函数
def check(request):
    # 获取前端数据
    rst = request.POST.get('captcha')
    print(rst)
    # 后端生成数据 获取
    code = request.session.get('code')
    print(code)
    # 比对
    if rst.lower() == code.lower():
        return HttpResponse('验证成功')
    return HttpResponse('失败')


# 调用 index文件
def index(request):
    return render(request,'captchapp/index.html')


#