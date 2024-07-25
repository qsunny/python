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

    data: Any
    message: str
    err_no: int

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
            message: str = "",
            err_no: int = 0
    ):
        super().__init__(data=data, message=message, err_no=err_no)
        self.data = data
        self.err_no: int = 0
        self.message: str = message


class ErrResp(Response):

    def __init__(
            self,
            data: Any = None,
            message: str = "",
            err_no: int = 1
    ):
        super().__init__(data=data, message=message, err_no=err_no)
        self.data = data
        self.err_no = 1
        self.message = message
