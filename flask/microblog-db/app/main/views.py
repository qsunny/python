# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, request, make_response, flash
from app.main.forms import LoginForm
from flask import current_app

from config import config
from . import main
from .. import db
from ..models import User,Post

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

@main.route('/addUser/<username>/<email>',methods=['GET','POST'])
def addUser(username,email):
    '''http://127.0.0.1:5000/addUser/hello/hello@example.com '''
    u = User(username=username, email=email)
    try:
        db.session.add(u)
        db.session.commit()
        return 'add successful'
    except Exception as e:
        print(e)
        return 'something go wrong'
    return "add user error"

@main.route('/getUser/<username>',methods=['GET','POST'])
def getUser(username):
    '''http://127.0.0.1:5000/getUser/aaron'''
    try:
        user = db.session.query(User).filter_by(username=username).first()
        return user.username +'<========>'+user.email
    except Exception as e:
        print(e)
        return 'something go wrong'
    return 'error query'

@main.route('/config', methods=['GET','POST'])
def testConfig():
    # secret_key = app.config['SECRET_KEY']
    dict = config.items()
    print(dict)
    for k,v in dict:
        print(k)
        print(v)
    repo = current_app.config.get('SQLALCHEMY_MIGRATE_REPO') or "default";
    print("test test")
    return  "hello test blueprint=="+repo

