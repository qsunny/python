"""
Created on 2023-09-22 17:11
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
import os
from typing import List
from pydantic import BaseSettings


class Setting(BaseSettings):
    # APP信息
    APP_TITLE: str = "always"
    APP_MODE: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 10161
    APP_VERSION: str = "/v1"
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]
    # Session
    SECRET_KEY = "session"
    SESSION_COOKIE = "session_id"
    SESSION_MAX_AGE = 14 * 24 * 60 * 60
    # Jwt
    JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60

    SWAGGER_UI_OAUTH2_REDIRECT_URL = "/api/v1/test/oath2"

    # 二维码过期时间
    QRCODE_EXPIRE = 60 * 1
    # 日志配置
    LOG_NAME = os.path.basename(os.getcwd())
    LOG_PATH = "log/%s.log" % LOG_NAME  # log存储路径
    LOG_LEVEL = "DEBUG"
    LOG_COLOR = True  # 是否带有颜色
    LOG_IS_WRITE_TO_CONSOLE = True  # 是否打印到控制台
    LOG_IS_WRITE_TO_FILE = True  # 是否写文件
    LOG_MODE = "w"  # 写文件的模式
    LOG_MAX_BYTES = 10 * 1024 * 1024  # 每个日志文件的最大字节数
    LOG_BACKUP_COUNT = 20  # 日志文件保留数量
    LOG_ENCODING = "utf8"  # 日志文件编码
    OTHERS_LOG_LEVAL = "ERROR"  # 第三方库的log等级
    # 数据库
    MYSQL_IP = "127.0.0.1"
    MYSQL_PORT = 4396
    MYSQL_DB = "spider_interface"
    MYSQL_USER_NAME = "root"
    MYSQL_USER_PASS = "123456"
    MYSQL_DB_URL = "mysql://root:123456@127.0.0.1:4396/spider_interface"
    MODELS_PATH: str = "models.items"
    # 代理
    IP_AGENTS = [""]
