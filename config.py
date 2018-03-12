class app_config:
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME='228744592@qq.com'
    MAIL_PASSWORD='iiyopczqdflpbghe' #qq邮箱为验证码
    MAIL_DEFAULT_SENDER='228744592@qq.com' #此处出现不明bug,MAIL_USERNAME，MAIL_DEFAULT_SENDER,以及message中sender必须相同
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:qq228744592@localhost/test'
    SQLAlCHEMY_COMMIT_TEARDOWN=True #自动提交更改
config={
    'app':app_config,
    'test':app_config,
    'default':app_config
}
    