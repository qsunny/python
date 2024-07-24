# # _*_ coding: utf-8 _*_
# """
# @File    : server.py
# @State   :
# @Datetime: 2023/1/13 17:49
# @Author  : 离小镜
# """
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import FastAPI, Request, Response
# from component import mysql
# from timer import scheduler
# from router import v1
#
#
# def create_app():
#     """
#     @return: app
#     """
#     app = FastAPI()
#     # 设置跨域中间件
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
#     # --- 路由 --- #
#     register_router(app)
#
#     # --- 拦截 --- #
#     register_middlewares(app)
#
#     # --- 挂载 --- #
#     event_init(app)
#
#     # --- 跨域 --- #
#     register_middlewares(app)
#
#     return app
#
#
# def register_router(app: FastAPI) -> None:
#     """
#     注册路由
#     :param app:
#     :return:
#     """
#     # 项目API
#     app.include_router(
#         v1.ApiRouter(),
#     )
#
#
# def register_middlewares(app: FastAPI) -> None:
#     """
#     """
#
#     @app.middleware("http")
#     async def logger_request(request: Request, call_next) -> Response:
#         # logger.info(f"记录:{request.method} --- url:{request.url.path} --- IP:{request.client.host}")
#         response = await call_next(request)
#         return response
#
#
# def event_init(app: FastAPI) -> None:
#     """
#     初始化连接
#     :param app:
#     :return:
#     """
#
#     @app.on_event("startup")
#     async def startup():
#         await mysql.init_mysql(app)  # 数据库
#         scheduler.start()  # 定时任务
#         pass
#
#     @app.on_event('shutdown')
#     async def shutdown():
#         """
#         关闭
#         :return:
#         """
#         scheduler.shutdown()
#
#
# class InitializeApp(object):
#     def __new__(cls, *args, **kwargs):
#         app = FastAPI()
#         app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
#                            allow_headers=["*"],
#                            )
#
#     def register_router(self) -> None:
#         """
#         注册路由
#         :param app:
#         :return:
#         """
#         # 项目API
#         self.app.include_router(
#             v1.ApiRouter(),
#         )
#
#     def register_middlewares(self) -> None:
#         """
#         """
#
#         @self.app.middleware("http")
#         async def logger_request(request: Request, call_next) -> Response:
#             # logger.info(f"记录:{request.method} --- url:{request.url.path} --- IP:{request.client.host}")
#             response = await call_next(request)
#             return response
#
#     def event_init(self) -> None:
#         """
#         初始化连接
#         :param app:
#         :return:
#         """
#
#         @self.app.on_event("startup")
#         async def startup():
#             await mysql.init_mysql(self.app)  # 数据库
#             scheduler.start()  # 定时任务
#             pass
#
#         @self.app.on_event('shutdown')
#         async def shutdown():
#             """
#             关闭
#             :return:
#             """
#             scheduler.shutdown()