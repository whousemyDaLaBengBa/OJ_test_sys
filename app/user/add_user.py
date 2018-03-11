from app import app as mainapp
from flask import render_template

@mainapp.route('/user/adduser')
def adduser():
    return render_template('register.html')