# -*- coding: utf-8 -*-

from flask import render_template
from app import app
from config import SECRET_KEY



'''
reference doc:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
https://www.cnblogs.com/jsben/p/4909964.html
'''


@app.route('/')
@app.route('/index')
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

@app.route('/config')
@app.route('/testConfig')
def testConfig():
    secret_key = app.config['SECRET_KEY']
    print(secret_key)
    return secret_key +"====="+ SECRET_KEY

