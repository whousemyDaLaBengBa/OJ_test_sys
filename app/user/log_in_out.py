from app import app as mainapp
from flask import render_template
from flask import request, session, redirect

@mainapp.route('/user/login', methods=['GET','POST'])
def login():
    try:
        username = request.values.get('username')
        password = request.values.get('password')
    except:
        return 'Access Violation'
    else:
        str = username + password
        return(str)
        #这里写验证登录的内容并返回登录后看到的界面

@mainapp.route('/user/logout', methods=['GET','POST'])
def logout():
    try:
        username = request.values.get('username')
        password = request.values.get('password')
    except:
        return 'Access Violation'
    else:
        str = username + password
        return(str)
        #这里写注销的内容并返回主页