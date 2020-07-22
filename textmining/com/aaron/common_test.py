import logging
import traceback
import sys


# 重写对象的 repr
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __repr__(self):
        return f"Rectangle({self.x}, {self.y}, {self.radius})"


c = Circle(100, 80, 30)
print(c)
# Circle(100, 80, 30)


# 重写字典类的 missing 方法
class MyDict(dict):
    def __missing__(self, key):
        message = f'{key} not present in the dictionary!'
        logging.warning(message)
        return message  # Or raise some error instead



def func():
    try:
        raise TypeError("Something went wrong...")
    except:
        traceback.print_exc(file=sys.stderr)


func()
