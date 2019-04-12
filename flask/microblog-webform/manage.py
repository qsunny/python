# -*- coding: utf-8 -*-
'''
Created on 2016年04月15日
@FileName: manage.py
@Description: (描述)
@author: 'Aaron.Qiu'
@version V1.0.0
'''

import os
import sys

from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
	return dict(app = app)
manager.add_command("shell", Shell(make_context = make_shell_context))

if __name__ == '__main__':
    manager.run()
