# -*- coding: utf-8 -*-
'''
Created on 2019-04-20
@FileName: component_prop.py
@Description: 处理行业参数数据
@author: 'Aaron.Qiu'
@version V1.0.0
'''

class ComponentProp:
    __prop_name = ''
    __prop_value = ''
    def __init__(self,prop_name,prop_value):
        self.__prop_name = prop_name
        self.__prop_value = prop_value


    @property
    def propName(self):
        return self.__prop_name

    @propName.setter
    def propName(self, propName):
        self.__prop_name = propName

    @property
    def propValue(self):
        return self.__prop_value

    @propValue.setter
    def propValue(self, propValue):
        self.__prop_value = propValue

    def __str__(self):
        return self.__prop_name + ":" + self.__prop_value