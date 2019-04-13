# -*- coding: utf-8 -*-
'''
Created on 2019-04-13
@FileName: manage.py
@Description: 修饰器使用示例 functools模板作用在于修改被修改的函数,函数名称 、文档名称、模板名称是原名称
@author: 'Aaron.Qiu'
@version V1.0.0
'''

from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name


if __name__ == '__main__':
    print(get_text.__name__) # get_text
    print( get_text.__doc__) # returns some text
    print (get_text.__module__) # __main__