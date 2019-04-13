# -*- coding: utf-8 -*-
'''
Created on 2019-04-13
@FileName: manage.py
@Description: (描述)
@author: 'Aaron.Qiu'
@version V1.0.0
'''

import os
import sys

from app import create_app
from flask_script import Manager, Shell,Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.debug = True
app.host = '0.0.0.0'
manager = Manager(app)

def make_shell_context():
	return dict(app = app)
manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command("runserver" ,Server(use_debugger=True, host='0.0.0.0', port=5000))


if __name__ == '__main__':
    manager.run()
