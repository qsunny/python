# -*- codiing:utf-8 -*-
"""regular expressions example
十进制
to
八进制: oct()

十进制
to
十六进制: hex()

"""

__author__="aaron.qiu"

import re
import binascii
import struct
import string

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def hexStr2Byte(str):
    """从16进制字符串转byte"""
    return bytes.fromhex(str)

def bin2dec(string_num):
    """二进制 to 十进制 : int(str,n=10)"""
    return str(int(string_num, 2))

def hex2dec(string_num):
    """十六进制 to 十进制"""
    return str(int(string_num.upper(), 16))

def dec2bin(string_num):
    """十进制 to 二进制: bin() """
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))

def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

if __name__=="__main__":
    str1 = "4F390D0A"
    print(bytearray(hex(ord('9')), 'utf-8'))
    byte1 = bytearray([3, 4, 5]);
    byte2 = bytearray(3)
    print(byte1[0])

    #a1 = bytes(bytearray(hex(ord('O')), 'utf-8'));
    #a2 = bytes(bytearray(hex(ord('9')), 'utf-8'));
    #a3 = bytes(bytearray(hex(ord('\r')), 'utf-8'));
    #a4 = bytes(bytearray(hex(ord('\n')), 'utf-8'));

    a1 = bytearray('4F','utf-8')
    a2 = bytearray('39','utf-8')
    a3 = bytearray('0D','utf-8')
    a4 = bytearray('0A','utf-8')

    print( bytes(a1+a2+a3+a4))
    print(hexStr2Byte('0A'))

    print(hex(int(hex2dec('4F'))).encode("utf-8"))

    s = '0x4F'
    b = int(s, 16)
    print(b)
    print('{:#x}'.format(int('0x0A',16)))
    print('{:x}'.format(b))
    print('{:#x}'.format(b))
    print('{:#07x}'.format(b))
    print(eval('0x4F'))