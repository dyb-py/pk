# 当前flask项目启动文件
from app import app

@app.route('/')
def hello_world():
    return 'Hello World!'




if __name__ == '__main__':
    app.run()
