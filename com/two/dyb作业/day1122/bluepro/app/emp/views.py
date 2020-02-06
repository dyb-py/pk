from flask import Blueprint

emp_blueprint = Blueprint('emp',__name__,url_prefix='/emp')

@emp_blueprint.route('/welcome/')
def welcome():
    return '欢迎你来到**系统'