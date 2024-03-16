import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

"gzip示例"
'''
参考来源 https://zhuanlan.zhihu.com/p/667041110

cat text.txt | gzip > data.gz
dd if=/dev/zero bs=1M count=1000 | gzip > boom.gz
pip install fastapi

pip install "uvicorn[standard]"

uvicorn server:app启动这个服务
uvicorn main:app --reload

SwaggerUi风格文档:http://127.0.0.1:8000/docs
ReDoc风格文档：http://127.0.0.1:8000/redoc

整个项目的 API对应的JSON描述信息
http://127.0.0.1:8000/openapi.json
'''

app = FastAPI()

# docs_url=None: 代表关闭SwaggerUi
# redoc_url=None: 代表关闭redoc文档
# app = FastAPI(docs_url=None, redoc_url=None)

@app.get('/')
def index():
    resp = FileResponse('data.gz')
    resp.headers['Content-Encoding'] = 'gzip'  # 说明这是gzip压缩的数据
    return resp


@app.get("/hello")
async def hello():
    """
    注册一个根路径
    :return:
    """
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    """
    项目信息
    :return:
    """
    return {
        "app_name": "FastAPI框架学习",
        "app_version": "v0.0.1"
    }


if __name__ == "__main__":
    print("=========")
    uvicorn.run(app, host="0.0.0.0", port=8000)