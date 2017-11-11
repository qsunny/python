# -*- codiing:utf-8 -*-
"""os example"""
__author__="aaron.qiu"

import logging

def readfile():
    try:
        f = open('a.text', 'r')
        print(f.read())
    finally:
        if f:
            f.close()

def readfile2():
    try:
        with open('ab.text', 'r') as f:
            print(f.read())
    except Exception as e:
        logging.error("没有找到文件",e)
if __name__=="__main__":
    readfile()
    readfile2()


