# -*- coding: utf-8 -*-
'''
Created on 2019-04-13
@FileName: manage.py
@Description: (描述)
@author: 'Aaron.Qiu'
@version V1.0.0
'''

import os
from app import db,create_app
from flask_script import Manager, Shell,Server,Command
from flask_migrate import Migrate, MigrateCommand
from migrate.versioning import api
from config import config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.debug = True
app.host = '0.0.0.0'
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	return dict(app = app, db = db)
manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command("runserver" ,Server(use_debugger=True, host='0.0.0.0', port=5000))
manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    db.create_all()
    SQLALCHEMY_DATABASE_URI = app.config.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_MIGRATE_REPO = app.config.get('SQLALCHEMY_MIGRATE_REPO')
    print("============="+SQLALCHEMY_MIGRATE_REPO)
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

if __name__ == '__main__':

    manager.run()
