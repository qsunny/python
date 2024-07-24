# -*- coding: utf-8 -*-
"""
Created on 2023-07-04 10:42
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
from fastapi import APIRouter, Security
from fastapi_base.core.auth import check_permissions
from fastapi_base.models.response import *

router = APIRouter()


@router.get("/ping", name="ping")
async def ping() -> Any:
    return OkResp(data="pong")


@router.get("/auth", dependencies=[Security(check_permissions, scopes=["auto"])])
async def auth() -> Any:
    return OkResp(data="pong")
