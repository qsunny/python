# -*- coding: utf-8 -*-
"""
Created on 2023-09-13 16:00
---------
@summary: jwt工具
---------
@author: aaron.qiu
"""
import jwt
import datetime
from fastapi_base.models.exception.base_error import BaseError

SECRET_KEY = 'abcdde'

def generate_access_token(user_id, user_name):
    """
    @summary: 生成token
    """

    expire_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=1000)
    play_load = {'user_id': user_id, 'user_name': user_name, 'exp': expire_time}
    token = jwt.encode(play_load, SECRET_KEY, algorithm='HS256')

    return token


def verify_access_token(token: str):
    """
    @summary: 校验token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if payload:
            return payload
        else:
            raise BaseError("无效凭证", 102)
    except jwt.ExpiredSignatureError:
        raise BaseError("token已失效", 102)
    except jwt.InvalidTokenError:
        raise BaseError("Invalid token", 105)
