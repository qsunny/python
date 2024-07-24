# -*- coding: utf-8 -*-
"""
Created on 2023-09-22 18:09
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
from tortoise import fields, models


class Items(models.Model):
    """
    @summary: Orm抽象基类
    """
    id = fields.IntField(pk=True, index=True)
    is_delete = fields.IntField(description="0=未删, 1=已删")
    create_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_at = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        abstract = True
