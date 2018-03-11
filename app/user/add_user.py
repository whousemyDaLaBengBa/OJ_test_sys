from app import app as mainapp
from flask import render_template
from flask import request, session, redirect

@mainapp.route('/user/adduser',methods=['GET','POST'])
def adduser():
    try:
        username = request.values.get('username')
        password = request.values.get('password')
    except:
        return render_template('register.html')
    else:
        if (username==None and password==None):
            return render_template('register.html')
        else:
            str = username + password
            return(str)
            #这里写注册的内容
    