# -*- coding:utf-8 -*-
"""
seft define override dict
"""
__author__="aaron.qiu"

from enum import Enum,unique


def printEnum(Month):
    for name,member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

class Gender(Enum):
    Male = 0
    Female = 1

if __name__=='__main__':
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    printEnum(Month);
    print("=======print weekday enum==========")
    printEnum(Weekday);
    print("=======print Gender enum==========")
    printEnum(Gender);
