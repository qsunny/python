# -*- coding: utf-8 -*-
'''
Created on 2019-04-19
@FileName: component_property.py
@Description: 处理行业参数数据
@author: 'Aaron.Qiu'
@version V1.0.0
'''

class  ComponentProperty:
    '组件属性类'
    __category1 = ''
    __category2 = ''
    __category3 = ''
    __category4 = ''
    __propList = None

    @property
    def category1(self):
        return self.__category1

    @category1.setter
    def category1(self, category1):
        self.__category1 = category1

    @property
    def category1(self):
        return self.__category1

    @category1.setter
    def category1(self, category1):
        self.__category1 = category1

    @property
    def category2(self):
        return self.__category2

    @category2.setter
    def category2(self, category2):
        self.__category2 = category2

    @property
    def category3(self):
        return self.__category3

    @category3.setter
    def category3(self, category3):
        self.__category3 = category3

    @property
    def category4(self):
        return self.__category4

    @category4.setter
    def category4(self, category4):
        self.__category4 = category4

    def getPropList(self):
        return self.__propList

    def setPropList(self, propList,default=[]):
        self.__propList = propList

    def __str__(self):
        # print('分类:1' + self.__category1+'--2'+self.__category2+'--3'+self.__category3+'--4'+self.__category4)
        return '分类1:'+ self.__category1 + '--2:' + self.__category2 + '--3:' + self.__category3 + '--4:' + self.__category4

