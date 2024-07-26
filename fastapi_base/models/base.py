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
    deleted = fields.IntField(default=10, description="10=未删, 20=已删")
    create_user_id = fields.BigIntField(null=True, description="创建用户id")
    create_time = fields.DatetimeField(null=True, auto_now_add=False, description="创建时间")
    create_user_name = fields.CharField(null=True, max_length=64, description="创建用户")
    update_user_id = fields.BigIntField(null=True, description="修改用户id")
    update_user_name = fields.CharField(null=True, max_length=64, description="修改用户")
    update_time = fields.DatetimeField(null=True, auto_now=False, description="更新时间")

    class Meta:
        abstract = True
