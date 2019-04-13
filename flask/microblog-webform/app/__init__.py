from flask import Flask
from config import config
from .main import main as main_blueprint


# app.config['SECRET_KEY'] = '666666'
# ... add more variables here as needed
# app.config.from_object('config') # 载入配置文件
# app.config.from_object(config[config_name])
# config[config_name].init_app(app)

def create_app(config_name):
    app = Flask(__name__)  # , static_url_path='/app/static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    app.register_blueprint(main_blueprint)

    # from .admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app


# from app.front import routes