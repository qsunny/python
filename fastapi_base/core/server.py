# _*_ coding: utf-8 _*_
"""
@File    : server.py
@State   :
@Datetime: 2023/1/13 17:49
@Author  : 离小镜

pip install tortoise-orm[asyncpg] fastapi
"""
from tortoise.contrib.fastapi import register_tortoise
from fastapi_base.core.middleware import middleware
from fastapi_base.component.db.ormdb import TORTOISE_ORM
from fastapi import FastAPI
from fastapi_base.timer import scheduler
from fastapi_base.router import v1


class InitializeApp(object):
    """
    注册App
    """

    def __new__(cls, *args, **kwargs):
        app = FastAPI(middleware=middleware)
        cls.event_init(app)
        cls.register_router(app)
        return app

    @staticmethod
    def register_router(app: FastAPI) -> None:
        """
        注册路由
        :param app:
        :return:
        """
        # 项目API
        app.include_router(
            v1.ApiRouter(),
        )

    @staticmethod
    def event_init(app: FastAPI) -> None:
        """
        事件初始化
        :param app:
        :return:
        """

        @app.on_event("startup")
        async def startup():
            # await mysql.init_mysql()
            register_tortoise(
                app,
                config=TORTOISE_ORM,
                generate_schemas=False,  # 重启服务时自动生成数据库表；关闭，改为使用aerich
                add_exception_handlers=True,
            )
            scheduler.start()  # 定时任务
            pass

        @app.on_event('shutdown')
        async def shutdown():
            """
            关闭
            :return:
            """
            # await mysql.close_mysql()
            scheduler.shutdown()
