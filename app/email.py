from flask import render_template
from flask_mail import Mail,Message
from config import config
from threading import Thread
from . import app

mail=Mail(app)

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to,subject,template,**kwargs)：
    msg=Message(subject,\
    sender=config[default].MAIL_DEFAULT_SENDER,\
    recipientd=[to])
    msg.body=render_template(template+'.txt',**kwargs)
    msg.html=render_template(template+'.html',**kwargs)
    thr=Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr