# _*_ encoding:utf-8 _*_

"""a test module"""
__author__ = 'Aaron.qiu'

import threading
from threading import Timer
import time

#custom thread
class MyThread(threading.Thread):
    def __init__(self,x):
        self.__x = x;
        threading.Thread.__init__(self)

    def run(self):
        print(str(self.__x))


def hello():
    print("hello, world")


def handleClient1():
    while (True):
        print("Waiting for client 1...")
        time.sleep(5)  # wait 5 seconds


def handleClient2():
    while (True):
        print("Waiting for client 2...")
        time.sleep(5)  # wait 5 seconds

if __name__=='__main__':
    # Start 10 threads.
    for x in range(10):
        MyThread(x).start()

    # create thread
    t = Timer(10.0, hello)
    # start thread after 10 seconds
    t.start()

    # create threads
    t = Timer(5.0, handleClient1)
    t2 = Timer(3.0, handleClient2)
    # start threads
    t.start()
    t2.start()