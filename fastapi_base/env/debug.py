# -*- coding: utf-8 -*-
"""
Created on 2023-09-22 17:11
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
import os
from typing import List
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    # __pydantic_extra__ = "ignore"
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
    SECRET_KEY: str = "session"
    SESSION_COOKIE: str = "session_id"
    SESSION_MAX_AGE: int = 14 * 24 * 60 * 60
    # Jwt
    JWT_SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 24 * 60

    SWAGGER_UI_OAUTH2_REDIRECT_URL: str = "/api/v1/test/oath2"

    # 二维码过期时间
    QRCODE_EXPIRE: int = 60 * 1
    # 日志配置
    LOG_FORMAT: str = "%(threadName)s|%(asctime)s|%(filename)s|%(funcName)s|line:%(lineno)d|%(levelname)s| %(message)s"
    LOG_NAME: str = os.path.basename(os.getcwd())
    LOG_PATH: str = "log/%s.log" % LOG_NAME  # log存储路径
    LOG_LEVEL: str = "DEBUG"
    LOG_COLOR: bool = True  # 是否带有颜色
    LOG_IS_WRITE_TO_CONSOLE: bool = True  # 是否打印到控制台
    LOG_IS_WRITE_TO_FILE: bool = True  # 是否写文件
    LOG_MODE: str = "w"  # 写文件的模式
    LOG_MAX_BYTES: int = 10 * 1024 * 1024  # 每个日志文件的最大字节数
    LOG_BACKUP_COUNT: int = 20  # 日志文件保留数量
    LOG_ENCODING: str = "utf8"  # 日志文件编码
    OTHERS_LOG_LEVAL: str = "ERROR"  # 第三方库的log等级
    # 是否详细的打印异常
    PRINT_EXCEPTION_DETAILS: bool = True
    # 设置带有颜色的日志格式
    os.environ["LOGURU_FORMAT"] = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>line:{line}</cyan> | <level>{message}</level>"
    )
    # 数据库
    MYSQL_IP: str = "47.115.41.15"
    MYSQL_PORT: int = 3308
    MYSQL_DB: str = "temp_test"
    MYSQL_USER_NAME: str = "root"
    MYSQL_USER_PASS: str = "password"
    MYSQL_DB_URL: str = "mysql://root:password@127.0.1.15:3308/temp_test"
    MODELS_PATH: str = "models.items"
    # 代理
    IP_AGENTS: list = [""]

    # REDIS
    # ip:port 多个可写为列表或者逗号隔开 如 ip1:port1,ip2:port2 或 ["ip1:port1", "ip2:port2"]
    REDISDB_IP_PORTS: str = "127.0.1.15:7379"
    REDISDB_USER_PASS: str = "password"
    REDISDB_DB: int = 0
    # 连接redis时携带的其他参数，如ssl=True
    REDISDB_KWARGS: dict = dict()
    # 适用于redis哨兵模式
    REDISDB_SERVICE_NAME: str = "test-redis"