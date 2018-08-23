# -*- codiing:utf-8 -*-
"""
process use example
"""
__author__="aaron.qiu"

import os

def printProcessId():
    '子进程永远返回0，而父进程返回子进程的ID'
    print("Process (%s) start..." % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


