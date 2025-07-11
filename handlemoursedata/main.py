# -*- coding: utf-8 -*-
'''
Created on 2019-04-19
@FileName: main_deepseek.py
@Description: 项目入口
@author: 'Aaron.Qiu'
@version V1.0.0
'''
from com.aaron.load_mouse_data import load_excel
from com.aaron.dao.base_dao import create_db,drop_db

if __name__ == "__main__":
    # create_db()
    # drop_db()
    load_excel()