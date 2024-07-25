# -*- coding: utf-8 -*-
"""
Created on 2023-03-20 9:37
---------
@summary: 服务入口
---------
@author: pepsi
"""
from core import server
from fastapi_base.util.jwt_tool import *
from fastapi_base.core.auth import *

# app = server.InitializeApp()


if __name__ == "__main__":
    token = generate_access_token(1000, 'aaron')
    print(token)
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMDAwLCJ1c2VyX25hbWUiOiJhYXJvbiIsImV4cCI6MTcyMTg5NTA5Nn0.QdZgU4jh_DrSAMGpbsDkHpbrIWuxBC4LD52MtpGAFJc'
    varified_token = verify_access_token(token)
    print(varified_token)

    # data = {'user_id': 1000, 'username': 'aaron.qiu'}
    # token = create_access_token(data)
    # print(token)
