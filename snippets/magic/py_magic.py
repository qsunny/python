# -*- codiing:utf-8 -*-
"""
pip install python-magic

file命令 依赖libmagic，
而libmagic 是一个用来根据文件头识别文件类型的开发库。于是就有了很多基于libmagic的封装，
这里介绍一个比较热门的python-magic python-magic 是 libmagic 文件类型识别库的 Python 接口
"""

__author__ = "aaron.qiu"

import magic

if  __name__ == "__main__":


    magic.from_file("C:\\Users\\Administrator\\Desktop\\万泓五金商品.xlsx")
    'PDF document, version 1.2'
    # recommend using at least the first 2048 bytes, as less can produce incorrect identification
    str = magic.from_buffer(open("C:\\Users\\Administrator\\Desktop\\万泓五金商品.xlsx", "rb").read(2048))
    print(str)
    str = magic.from_file("C:\\Users\\Administrator\\Desktop\\万泓五金商品.xlsx", mime=True)
    print(str)