from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import app
import config
app.config.from_object(config)

db=SQLAlchemy(app)
class User(db.Model):           #用户表
    __tablename__='users'
    id=['db',
        'email',
        'submit',
        'solved',
        'defunct',
        'ip',
        'accesstime',
        'volume',
        'language',
        'password',
        'reg_times',
        'nicks',
        'school'
    ]
    id=db.Column(db.String(20),primary_key=True)#id，主键
    email=db.Column(db.String(100,unique=True))#邮箱，必须唯一
    submit=db.Column(db.Integer)#用户提交次数
    solved=db.Column(db.Integer)#成功次数
    defunct=db.Column(db.String(1))#是否屏蔽用户（Y/N）
    ip=db.Column(db.String(20))#用户注册ip
    accesstime=db.Column(db.Date)#用户注册时间
    volume=db.Column(db.Integer)#未知
    language=db.Column(db.Integer)#用户语言
    password=db.Column(db.String(32))#密码
    reg_time=db.Column(db.Data)#注册时间
    nick=db.Column(db.String(100))#昵称
    school=db.Column(db.String(100))#学校
    def __init__(self,*s):
        id=db.s[0]
        email=s[1]
        submit=s[2]
        solved=s[3]
        defunct=s[4]
        ip=s[5]
        accesstime=s[6]
        volume=s[7]
        language=s[8]
        password=s[9]
        reg_times[10]
        nicks[11]
        school=s[12]

    def __repr__(self):
        return '<User %r>' %self.id
        



