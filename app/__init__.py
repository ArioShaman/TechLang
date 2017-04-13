from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
#from config import basedir
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

from app import views, models,admin