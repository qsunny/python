# -*- coding: utf-8 -*-

from math import fabs, ceil

def math_fabs(x):
    return fabs(x)

def math_ceil(x):
    return ceil(x)

def increate(x):
    return x + 1

if __name__ == '__main__':
    print( math_fabs(-1.2))
    print( math_ceil(-2.3))