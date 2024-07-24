# -*- coding: utf-8 -*-
"""
Created on 2023-07-04 14:29
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
from typing import Any
from typing import Dict, ClassVar, Optional
from pydantic import Field, BaseModel, ConfigDict
from fastapi.encoders import jsonable_encoder


class Response(BaseModel):

    def __init__(
            self,
            data: Any = None,
            message: str = ""
    ):
        self.data: str = data
        self.message: str = message

    @property
    def to_dict(self):
        properties = {}
        for key, value in self.__dict__.items():
            if key not in (
                    "__name__",
            ):
                if key.startswith(f"_{self.__class__.__name__}"):
                    key = key.replace(f"_{self.__class__.__name__}", "")
                properties[key] = value

        return properties


class OkResp(Response):

    def __init__(
            self,
            data: Any = None,
            message: str = ""
    ):
        super().__init__(data=data, message=message)
        self.data = data
        self.err_no = 0
        self.message = message


class ErrResp(Response):

    def __init__(
            self,
            data: Any = None,
            message: str = ""
    ):
        super().__init__(data=data, message=message)
        self.data = data
        self.err_no = 1
        self.message = message
