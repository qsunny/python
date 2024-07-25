# 自定义异常类 BaseError，继承自 Exception
class BaseError(Exception):
    def __init__(self, message="错误", code=501):
        # 调用基类的构造函数
        super().__init__(message)
        self.code = code
        # 你可以添加自定义的方法或属性





