# -*- coding: utf-8 -*-
'''
Created on 2019-04-13
@FileName: forms.py
@Description: forms.py
@author: 'Aaron.Qiu'
@version V1.0.0
'''


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')