# -*- coding: utf-8 -*-
"""
Created on 2023-07-04 16:36
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
from datetime import timedelta, datetime
from fastapi import HTTPException, Request
from pydantic import ValidationError
from jwt import PyJWTError
from fastapi_base.env import Setting
import jwt

setting = Setting()

def create_access_token(data: dict):
    """
    创建token
    :param data: 加密数据
    :return: jwt
    """
    token_data = data.copy()
    # token超时时间
    expire = datetime.utcnow() + timedelta(seconds=30)  # minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    # 向jwt加入超时时间
    token_data.update({"exp": expire})
    # jwt加密
    jwt_token = jwt.encode(token_data, setting.JWT_SECRET_KEY, algorithm=setting.JWT_ALGORITHM)

    return jwt_token


async def check_permissions(request: Request):
    """
    权限验证
    @param request:
    """
    # ----------------------------------------验证JWT token------------------------------------------------------------
    try:
        # token解密
        request.state.detail = ""
        token = request.headers.get("authorization")
        payload = jwt.decode(
            token,
            setting.JWT_SECRET_KEY,
            algorithms=[setting.JWT_ALGORITHM]
        )
        if payload:
            user_id = payload.get("user_id", None)
            user_type = payload.get("user_type", None)
            username = payload.get("username", None)
            # 无效用户信息
            if user_id is None or user_type is None or username is None:
                raise HTTPException(status_code=400, detail="无效凭证")
            else:
                # 缓存用户ID
                request.state.user_id = user_id
                # 缓存用户类型
                request.state.user_type = user_type
                # 缓存用户类型
                request.state.username = username

        else:
            raise HTTPException(status_code=400, detail="无效凭证")

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="凭证已过期")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="无效凭证")

    except (PyJWTError, ValidationError):
        raise HTTPException(status_code=400, detail="无效凭证")

# print(create_access_token({"user_id": 1, "user_type": 1, "username": 1}))
