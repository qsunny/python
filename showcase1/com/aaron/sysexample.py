# -*- coding: utf-8 -*-
from sys import argv

def printCommandParam():
    """打印命令行参数"""
    print(type(argv))
    for commandParam in argv:
        print(commandParam)



if __name__=="__main__" :
    printCommandParam()











