# -*- coding: utf-8 -*-

from . import db

from datetime import datetime

class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    mobile = db.Column(db.String(255), index=True)
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    __tablename__ = 't_post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('t_user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)