from django.shortcuts import render
# Create your views here.
import MySQLdb
def login(request):
    return render(request,'login.html')

def regist(request):
    return render(request,'regist.html')

def reg(request):
    conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='user',
        charset='utf8'
    )
    cur=conn.cursor()
    user=request.GET.get('username')
    pwd=request.GET.get('pwd')
    conpwd=request.GET.get('conpwd')
    sql='select username from user where username=%s'
    cur.execute(sql,[user])
    if (cur.fetchone()):
        return render(request, 'reg1.html')
    elif(pwd!=conpwd):
        return render(request, 'reg2.html')
    elif(user==None or pwd==None):
        return render(request, 'reg3.html')
    else:
        sql1='insert into user(username,password) value (%s,%s)'
        cur.execute(sql1,[user,pwd])
        conn.commit()
        cur.close()
        conn.close()
        return render(request,'reg.html')

def log(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='user',
        charset='utf8'
    )
    user = request.GET.get('username')
    pwd = request.GET.get('pwd')
    # print(user,pwd)
    cur = conn.cursor()
    sql='select username ,password from user where username=%s and password=%s'
    cur.execute(sql,[user,pwd])
    if(cur.fetchone()):
        cur.close()
        conn.close()
        return render(request,'log.html')
    else:
        cur.close()
        conn.close()
        return render(request, 'log1.html')