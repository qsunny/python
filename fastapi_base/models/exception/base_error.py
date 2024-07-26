# 自定义异常类 BaseError，继承自 Exception
class BaseError(Exception):
    def __init__(self, message="错误", code=501):
        # 调用基类的构造函数
        super().__init__(message)
        self.code = code
        self.message = message
        # 你可以添加自定义的方法或属性

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



