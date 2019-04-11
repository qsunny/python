from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '666666'
# ... add more variables here as needed
app.config.from_object('config') # 载入配置文件


from app import routes