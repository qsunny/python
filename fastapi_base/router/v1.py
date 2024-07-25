# _*_ coding: utf-8 _*_
"""
@File    : v1.py
@State   :
@Datetime: 2023/2/14 9:34
@Author  : 离小镜 
"""
from fastapi import APIRouter
from fastapi_base.api import logic, main


class ApiRouter(object):
    """
    注册路由
    """
    def __new__(cls, *args, **kwargs):
        router = APIRouter()
        router.include_router(main.router, prefix="/api", tags=["测试"])
        router.include_router(logic.router, prefix="/logic", tags=["业务逻辑"])

        return router
