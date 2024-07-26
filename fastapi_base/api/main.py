# -*- coding: utf-8 -*-
"""
Created on 2023-07-04 10:42
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
from pprint import pprint

from fastapi import APIRouter, Security
from fastapi_base.core.auth import check_permissions
from fastapi_base.models.response import *
from fastapi_base.log.log import log


router = APIRouter()


@router.get("/ping", name="ping")
async def ping() -> Any:
    resp = OkResp(data="pong", message="ok")
    pprint(resp)

    return resp
    # return {"message": "Hello World"}


@router.get("/health", name="health")
async def health() -> Any:
    resp = OkResp(data="health", message="跳过认证")
    log.info(resp)
    log.debug("debug========")
    log.error("error========")


    return resp


# 定义Pydantic模型
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# 路径操作函数，接收JSON数据
@router.post("/items")
async def create_item(item: Item):
    # return item
    return OkResp(data=item)


@router.get("/auth", dependencies=[Security(check_permissions, scopes=["auto"])])
async def auth() -> Any:
    return OkResp(data="pong")
