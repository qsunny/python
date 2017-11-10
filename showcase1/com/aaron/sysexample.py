# -*- coding: utf-8 -*-
#from sys import argv,path,modules,exec_prefix
from sys import *

def printCommandParam():
    """打印命令行参数"""
    print(type(argv))
    for commandParam in argv:
        print(commandParam)

def printModuleSearchPath():
    """打印模块搜索路径"""
    print(type(path))
    for subpath in path:
        print(subpath)

def printModuleDictionary():
    """打印模块dictionary"""
    for module in modules:
        print(module)

def printStaticObjectInfo():
    """sys模块静态对象信息"""
    #print(copyright)
    print(exec_prefix)
    print(executable)
    print(hash_info)
    print(implementation)
    print(platform)
    print(prefix)
    print(thread_info)
    print(version)
    print(version_info)
    # exit(2)
    displayhook('a')

def printHello():
    print("export")


if __name__=="__main__" :
    printCommandParam()
    printModuleSearchPath()
    printModuleDictionary()
    #print(printCommandParam.__doc__)
    printStaticObjectInfo()











