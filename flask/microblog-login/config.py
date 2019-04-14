# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))
# SECRET_KEY = 'you-will-never-guess'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lksfDsdf211SDF'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_MIGRATE_REPO = 'db_repository'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'db_flask_blog_dev.sqlite')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    # 'mysql://root:123456@127.0.0.1/db_flask_blog_dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_MIGRATE_REPO = 'db_repository'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'db_flask_blog_test.sqlite')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    # 'mysql://root:123456@127.0.0.1/db_flask_blog_test'


class ProductionConfig(Config):
    SQLALCHEMY_MIGRATE_REPO = 'db_repository'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'db_flask_blog.sqlite')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    # 'mysql://root:123456@127.0.0.1/db_flask_blog'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}