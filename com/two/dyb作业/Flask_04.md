# Flask_04

### 一、强制登录

```python
@myblue.before_request  #只对当前蓝图中的route有效
def xxx():
    print("before requst")
    print(request.path) #获取请求路径
    if "login" in request.path: #登录，注册，验证码，检测用户名重复
        print("logining....")
        return None #不拦截，放行
    if not session.get("login"): #登录中会在session中存入login   session['login']
        return redirect(url_for("xxxx")) #返回登录
    
@app.before_request  #对所有route有效
def xxx():
    print("before requst")
    print(request.path)
    if "login" in request.path:
        print("logining....")
        return None
    if not session.get("login"):#登录中会在session中存入login
        return redirect(url_for("xxxx")) #返回登录
```


### 二、文件上传

```python
#config.py  在配置中，设置文件上传的路径
import os
class Config:
    ...
MEDIA_DIR=os.path.join(os.path.abspath(os.path.dirname(__file__)),"app/static/media")
```

```python
<form action="{{ url_for('user.upup') }}" method="post" enctype="multipart/form-data">
	<input type="text" name="username">
	<input type="file" name="source">
	<input type="submit" value="上传">
</form>
```

```python
@myblue.route("/up/",methods=['post'])
def upup():
    username = request.form.get("username")
    file = request.files.get("source")
    unique_name = str(uuid.uuid4())  # 唯一文件名
    # abc.png  [abc,png]   png
    ext = os.path.splitext(file.filename)[1] #文件后缀，file.filename=文件名
    uniquefilename = unique_name+ext #拼接文件名
    path="media/"+uniquefilename #存入数据库的文件路径
    
    user = User(name=username,pic=path)
    db.session.add(user)#将数据存入数据库，其中包含文件的路径信息
    
    file.save(os.path.join(config.MEDIA_DIR, uniquefilename))  # 将文件存入指定目录位置
    
    db.session.commit()
    return render_template("xx.html",path=path)#path用户回显图片
	#return '{"path":url_for("static",filename=path)}'
```

```python
#xx.html
<img src="{{url_for('static',filename=path)}}">
```

### 三、验证码

```python
import random,string,os

@myblue.route("/cap/")
def getcaptcha():
    #从image.py中导入ImageCaptchar类
    from app.captcha.image import ImageCaptcha
    
    #为验证码设置字体 获取当前目录下的xxx目录下的segoesc.ttf文件
    image = ImageCaptcha(fonts=[os.path.abspath("xxx/segoesc.ttf")])
    
    #随机码
    #大小写英文字母+数字，随机抽取5位作为验证码 ['x','x','x','x','x']
    code = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,5)
    #将验证码存入session，以备后续验证
    session['code']=code
   
   #将生成的随机字符拼接成字符串，作为验证码图片中的文本
    data = image.generate("".join(code))
   
   #写出验证图片 给客户端
    response = make_response(data.getvalue()) # !!return HttpResponse(data,"image/png")!!
    response.headers['Content-Type'] = 'image/png' # text/html   application/json   image/png
    return response
```