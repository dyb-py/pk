from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
# 配置mysql数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/flask_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
# 针对当前app，还需要去初始化 sqlalchemy对象，才能使用orm机制
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
