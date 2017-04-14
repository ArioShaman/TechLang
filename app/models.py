from app import db
from flask_admin.contrib.sqlamodel import ModelView
from sqlalchemy import Column, Integer, String,Text
import datetime


ROLE_ADMIN = 1
ROLE_USER = 0


class Admin(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    Lastname = db.Column(db.String(24), unique=False)
    Firstname = db.Column(db.String(24), unique = False)
    email = db.Column(db.String(120), index = True, unique = True)
    town = db.Column(db.String(40), unique =  False)
    age = db.Column(db.Integer, unique = False)
    role = db.Column(db.SmallInteger, default = ROLE_ADMIN)
    password =db.Column(db.String(64),default = 'admin')
    interests = db.Column(db.Text, default = '')


    def __init__(self , nickname ,password,email):
        self.nickname = nickname
        self.password = password
        self.email = email

    def __repr__(self):
        return '<Admin %r>' % (self.nickname)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.uid
    def is_authenticated(self):
        return True
    def __unicode__(self):
        return self.nickname

class VocFolder(db.Model):
    uid = db.Column(Integer, primary_key = True)
    autor = db.Column(String(24), unique=False)
    name_folder =db.Column(String(24), unique=False)

class VocWord(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    folder_id = db.Column(db.String(24), unique=False)
    eng = db.Column(db.String(24), unique=False)
    rus = db.Column(db.String(24), unique=False)
    desc = db.Column(db.String(124), unique=False)
    link_cover = db.Column(db.String(64), unique=False)


class Message(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    room_id = db.Column(db.Integer)
    autor_id = db.Column(db.Integer)
    message = db.Column(db.Text)
    data = db.Column(db.DateTime,default=datetime.datetime.utcnow)

class RoomDialog(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    r_id = db.Column(db.Integer, unique = False)
    user_id = db.Column(db.Integer, unique = False)

class Videos(db.Model):
    uid = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, unique = False)
    desc = db.Column(db.String(124))
    link_video = db.Column(db.String(124))
    cover = db.Column(db.String(564))

class Post(db.Model):
    uid = db.Column(db.Integer,primary_key = True)
    autor = db.Column(db.String(24))
    title = db.Column(db.String(24))
    desk = db.Column(db.String(124))
    cover = db.Column(db.String(564))
    article = db.Column(db.String(560))
    #data = db.Column(db.DateTime,default=datetime.datetime.utcnow)

class Events(db.Model):
    uid = db.Column(db.Integer,primary_key = True)
    autor_id = db.Column(db.Integer)
    description = db.Column(db.String(64))

class Partipiant(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    event_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

class Interests(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text)
    max_user_count = db.Column(db.Integer)
    curent_user_count = db.Column(db.Integer)

class UserInterest(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    interest_id = db.Column(db.Integer)

class check_unit_user(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    check_unit = db.Column(db.Integer)