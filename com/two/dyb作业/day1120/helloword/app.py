from datetime import datetime

from flask import Flask, render_template, redirect, url_for, request  # 导包
from werkzeug.routing import BaseConverter

app = Flask(__name__)  # 创建一个flask实例对象 是当前项目工作 核心对象
# print(__name__)

'''
相当于 django中
    视图函数 对应 url路由设置        全局urls.py中
    views.py       urls.py  单独每个app下   配置每个app对应的路由前缀
'''
@app.route('/')
def hello_world():
    # 10/0
    return 'Hello World!'


@app.route('/index/a/b/c/')
def index():
    # 10/0
    return 'index'

# url中 变量名称 与 视图函数中参数名称 保持一致
@app.route('/index1/<name>/')
def index1(name):
    print(name)
    print(type(name))
    return 'index1'

# 命名路径  + 转换器 限制
# 默认数据类型：字符串
@app.route('/index2/<string:name>/')
def index2(name):
    print(name)
    print(type(name))
    return 'index2'

@app.route('/index3/<int:name>/')
def index3(name):
    print(name)
    print(type(name))
    return 'index3'

@app.route('/index4/<float:name>/')
def index4(name):
    print(name)
    print(type(name))
    return 'index4'
# path
@app.route('/index5/<path:name>/')
def index5(name):
    print(name)
    print(type(name))
    return 'index5'

# uuid
@app.route('/index6/<uuid:name>/')
def index6(name):
    print(name)
    print(type(name))
    return 'index6'
# any() 函数
@app.route('/index7/<any("liuzong","luzong","sunge"):name>/')
def index7(name):
    print(name)
    print(type(name))
    return 'index7'


# 自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self,map,*args):
        self.map = map
        self.regex = args[0]
# 自定义类 添加到 现有的 DEFAULT_CONVERTERS中
# print(app.url_map.converters)
app.url_map.converters['regex'] = RegexConverter


@app.route('/index8/<regex("\d{2}"):name>/')
def index8(name):
    print(name)
    print(type(name))
    return 'index8'

# 跳转
# 调模板文件
@app.route('/index9/',methods=['get','post'])
def index9():
    # print(name)
    # 接收重定向传入的参数
    # request.GET args
    # age = request.args.get('age')
    # print(age)
    # 接收 a标签 js location进行参数 form GET请求方式
    # name = request.args.get('username')
    # age = request.args.get('userpwd')
    # print(name,age)
    # form表单 post请求  form
    # name = request.form.get('username')
    # age = request.form.get('userpwd')
    # print(name, age)
    # print(request.args['username1'])
    if request.method == 'POST':
        name = request.form.get('username')
        age = request.form.get('userpwd')
        hobbys = request.form.getlist('hobbys')
        print(name, age,hobbys)
    elif request.method == 'GET':
        name = request.args.get('username')
        age = request.args.get('userpwd')

        print(name, age)
    print('index9')
    return render_template('index9.html')

# 跳转 重定向
# 重定向需要传参
# 方式一：url_for()
@app.route('/index10/')
def index10():
    print('index10')
    # 重定向 模板文件 路径使用 软编码
    # url = url_for('index9',age=18)
    url = url_for('index9') + '?age=20'
    # reverse() 反查路径
    print(url) # /index9/
    return redirect(url)
    # return redirect('/index9/')


# 调 index11模板文件
@app.route('/index11/')
def index11():
    return render_template('index11.html')


# 自定义 格式化 时间日期 功能函数
def myformat(value,format):
    return value.strftime(format)
# 添加到 现有的filter字典
print(app.jinja_env.filters)
app.jinja_env.filters['dateformat'] = myformat

# 模板文件渲染 传值

@app.route('/query/')
def query():
    return render_template('query.html',
                           name='  Liu zong  ',
                           age=18,
                           list1=[10,20,30,40,50],
                           dict1={'name':'孙总','age':36,'height':'178cm','weight':'140'},
                           other=None,
                           s='',
                           boo1 = False,
                           set1={"abc",10,True},
                           tuple1=(40,50,60),
                           time=datetime.now())




if __name__ == '__main__':
    app.run(host='localhost',port=8000,debug=True)
