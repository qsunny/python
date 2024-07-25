# -*- coding: utf-8 -*-
"""
Created on 2023-09-22 18:14
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
from fastapi_base.env import Setting
setting = Setting()

TORTOISE_ORM = {
    "connections": {"default": setting.MYSQL_DB_URL},
    "apps": {
        "models": {
            "models": [setting.MODELS_PATH],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
}