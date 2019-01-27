# -*- codiing:utf-8 -*-
"""os example"""
__author__="aaron.qiu"

class A(object):
    """"classmethod showcase"""
    bar=1
    def fun1(self):
        print("fun1")
    @classmethod
    def fun2(cls):
        print("fun2")
        print(cls.bar)
        cls().fun1()

if __name__=="__main__":
    a = A()
    a.fun2()
