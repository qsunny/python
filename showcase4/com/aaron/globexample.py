# -*- codiing:utf-8 -*-
"""
glob example
glob 模块提供了方便的文件模式匹配方法
"""
__author__="aaron.qiu"

import pprint
from glob import glob

def glob_showcase():
    result = glob("../*.py")
    pprint.pprint(result)
    glob("../[0-9]*")
    glob("../09*/*.ipynb")

if __name__=="__main__":
    glob_showcase()
