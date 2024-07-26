from starlette.requests import Request
from starlette.responses import JSONResponse

from fastapi_base.log.log import log
from fastapi_base.models.exception.base_error import BaseError


# 异常处理器
async def sys_exception_handler(request: Request, e: Exception):
    log.error(f"系统异常:{type(e).__name__} {str(e)}")
    if isinstance(e, BaseError):
        return JSONResponse(
            status_code=200,
            content=e.to_dict,
        )
    else:
        return JSONResponse(
            status_code=200,
            # content=exc.to_dict,
            content={
                "code": 501,
                "type": type(e).__name__,  # 异常类型名称
                "message": str(e),         # 异常消息
                "traceback": None,         # 在这个简单示例中不包括traceback，但可以在更复杂的情况下添加
            }
        )
