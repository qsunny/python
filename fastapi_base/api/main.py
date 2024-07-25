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

router = APIRouter()


@router.get("/ping", name="ping")
async def ping() -> Any:
    resp = OkResp(data="pong", message="ok")
    pprint(resp)

    return resp
    # return {"message": "Hello World"}


@router.get("/auth", dependencies=[Security(check_permissions, scopes=["auto"])])
async def auth() -> Any:
    return OkResp(data="pong")
