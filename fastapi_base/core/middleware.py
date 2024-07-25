# -*- coding: utf-8 -*-
"""
Created on 2023-07-03 16:06
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
import time
from fastapi_base.log.log import log as logger
from fastapi import Request
from fastapi_base.core.auth import check_permissions
from fastapi_base.models.response import ErrResp
from fastapi.middleware import Middleware
from starlette.responses import Response, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi_base.util.jwt_tool import *

class LoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = int(time.time() * 1000)
        response = await call_next(request)
        end_time = int(time.time() * 1000)
        logger.info(
            f"请求:{request.method} | {request.url.path} | {request.client.host} | 响应:{response.status_code} | "
            f"耗时: {(end_time - start_time) / 1000}s")
        return response


class SimpleAuthorizationMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if not request.headers.get("Authorization") != "10086":
            return JSONResponse(status_code=200, content=ErrResp(data="认证失败").to_dict)
        response = await call_next(request)
        return response



class AuthorizationMiddleware(BaseHTTPMiddleware):

    # 排除列表，包含不需要认证的 URL 路径
    excluded_urls = {"/api/health", "/public"}

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        token = request.headers.get("token")
        if not token:
            return JSONResponse(status_code=200, content=ErrResp(message="未登录").to_dict)
        # await check_permissions(request=request)
        # if request.state.detail != "":
        #     return JSONResponse(status_code=200, content=ErrResp(message=request.state.detail).to_dict)

        if request.url.path in self.excluded_urls:
            return await call_next(request)  # 直接继续处理请求

        try:
            varify_token = verify_access_token(token)
        except BaseError as e:
            return JSONResponse(status_code=200, content=ErrResp(message=str(e), err_no=e.code).to_dict)

        response = await call_next(request)
        return response


middleware = [
    # 跨域中间件
    Middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
               allow_headers=["*"]),
    # 日志中间件
    Middleware(LoggerMiddleware),

    # 认证中间件
    Middleware(AuthorizationMiddleware)
]
