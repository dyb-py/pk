import os
from django.core.mail import send_mail



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhongqixiangmu.settings")

if __name__ == '__main__':
    while True:
        send_mail(
            '我是大娃',
            '我是二娃<a href="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%A7%E5%A8%83&rsv_pq=ac1516650094e9c0&rsv_t=2f5aSykewEvAC%2Bnof2AkXC6gYjvGENVdqVnGrPEiTRCTXAmM6735UMoGp9c&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=5&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&inputT=1177&rsv_sug4=1177">点击查看大娃</a>',
            'a870575061@sina.com',
            ['596263242@qq.com']
        )
        import time
        time.sleep(2)
