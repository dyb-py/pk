from django.shortcuts import render
import MySQLdb
# Create your views here.

def baizhi(request):
    return render(request,'3.html')

def aa(request):
    name=request.GET.get('name')
    school=request.GET.get('school')
    sex=request.GET.get('sex')
    xl=request.GET.get('s')
    tel=request.GET.get('tel')
    qq=request.GET.get('qq')
    cu=request.GET.getlist('cur')
    cu=' '.join(cu)
    t=request.GET.get('t')
    conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='user',
        charset='utf8'
    )
    cur=conn.cursor()
    conn.begin()
    sql='insert into baizhi value (%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql,[name,school,sex,xl,tel,qq,cu,t])
    conn.commit()
    cur.close()
    conn.close()
    return render(request,'2.html')