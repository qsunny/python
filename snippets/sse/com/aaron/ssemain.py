from flask import Flask, Response
import time
from flask import Flask
from flask_cors import CORS

"""
pip install flask-cors
"""

app = Flask(__name__)
CORS(app)  # 允许所有域名访问所有路由
# CORS(app, resources={
#     r"/api/*": {
#         "origins": ["http://127.0.0.1:5000", "https://your-domain.com"],  # Allowed domains
#         "methods": ["GET", "POST"],  # Permitted HTTP methods
#         "allow_headers": ["Content-Type", "Authorization"],  # Allowed headers
#         "supports_credentials": True  # Enable cookies/auth [14,15](@ref)
#     }
# })


def generate_data():
    for i in range(10):
        time.sleep(1)
        # 发送JSON格式数据
        yield f"data: {{'count': {i}, 'time': '{time.ctime()}'}}\n\n"


@app.route('/stream')
def stream():
    return Response(generate_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)