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
from fastapi_base.component.db.mysqldb import MysqlDB
from fastapi_base.component.db.redisdb import RedisDB

# app = server.InitializeApp()


if __name__ == "__main__":
    # token = generate_access_token(1000, 'aaron')
    # print(token)
    # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMDAwLCJ1c2VyX25hbWUiOiJhYXJvbiIsImV4cCI6MTcyMTg5NTA5Nn0.QdZgU4jh_DrSAMGpbsDkHpbrIWuxBC4LD52MtpGAFJc'
    # varified_token = verify_access_token(token)
    # print(varified_token)

    # data = {'user_id': 1000, 'username': 'aaron.qiu'}
    # token = create_access_token(data)
    # print(token)

    # db = MysqlDB()
    # sql = 'select * from t_sys_user limit 30'
    # result = db.find(sql, limit=0, to_json=True)
    # print(result)

    # redis = RedisDB()
    # redisObj = redis.getkeys("job:test:202402271441")
    # redisObj = redis.sadd("test:a", "22222")
    # redis.hset("test:b", "a", "2222222222")
    # redis.hdel("test:b","a")
    # print(redisObj)

    print("d")
