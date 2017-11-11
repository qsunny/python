# _*_ encoding:utf-8 _*_

"""a test module"""
__author__ = 'Aaron.qiu'

import json
from com.aaron.sysexample import printHello


if __name__=="__main__" :
    printHello()
    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
