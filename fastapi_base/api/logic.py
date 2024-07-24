# -*- coding: utf-8 -*-
"""
Created on 2023-07-18 15:09
---------
@summary: 机构数据
---------
@author: pepsi
"""
from fastapi import APIRouter, Query, Response
from fastapi_base.models.response import *

router = APIRouter()


# --- 抖音主页 --- #
@router.get("/author", name="机构达人数据")
async def douyin_user(
        company_id: str = Query(description="机构ID")
) -> Any:
    return OkResp(data="")


