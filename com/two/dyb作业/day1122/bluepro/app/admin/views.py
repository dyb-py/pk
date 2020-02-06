from flask import Blueprint, render_template, redirect, url_for

# 给当前模块 设置 自己的路由 以及对应的视图函数
# 需要 使用 blueprint
# url_prefix 是当前蓝图的路径访问前缀
admin_blue = Blueprint('admin',__name__,url_prefix="/admin")

# 使用该 blueprint对象 设置 对应路由 以及函数
@admin_blue.route('/login/')
def login():
    return render_template('admin/login.html')


@admin_blue.route('/register/')
def register():
    return '这是一个注册页面'


@admin_blue.route('/loginlogic/')
def loginlogic():
    print('这是 登录逻辑业务处理函数')
    # return '登录成功测试'
    # url = url_for('admin.login')
    url = url_for('emp.welcome')
    return redirect(url)