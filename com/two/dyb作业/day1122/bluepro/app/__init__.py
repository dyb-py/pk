
# 完成Flask初始化工作
# 初始化 Flask对象  SQLAlchemy对象 配置mysql参数
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)
# 配置mysql
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.admin.views import admin_blue
from app.emp.views import emp_blueprint

app.register_blueprint(admin_blue)
app.register_blueprint(emp_blueprint)