from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import app
from config import config
app.config.from_object(config['app'])

db=SQLAlchemy(app)


