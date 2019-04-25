# -*- codiing:utf-8 -*-
"""
pysnooper example
reference https://github.com/cool-RR/pysnooper
"""
__author__="aaron.qiu"

import pysnooper

@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]

@pysnooper.snoop('file.log')
def debug2log():
    a = 10
    b = 100
    i = a/b
    print(i)


if __name__ == "__main__":
    number_to_bits(6)
    debug2log()