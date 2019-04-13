# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, request, make_response, flash
from . import main
from app.main.forms import LoginForm

'''
reference doc:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
https://www.cnblogs.com/jsben/p/4909964.html
https://github.com/sugarguo/Flask_Blog/blob/master/app/__init__.py
'''


@main.route('/', methods=['GET'])
@main.route('/index', methods=['GET','POST'])
def index():

    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@main.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@main.route('/config', methods=['GET','POST'])
def testConfig():
    # secret_key = app.config['SECRET_KEY']
    print("test test")
    return  "hello test blueprint"

