import os.path as rp
path = rp.realpath(__file__)
path = path[0:-13] #app所在的路径的父文件夹
import sys
sys.path.append(path)
#将app加入为系统包，方便调用

from flask import render_template
from flask_script import Manager
#import 必要的包

import app.config as cf
from app import app as mainapp
import app.user
import app.Problems
#import网站内容


@mainapp.route('/')
def index():
    return render_template('index.html')


manager = Manager(mainapp)

if __name__ == '__main__':
    manager.run()