# -*- codiing:utf-8 -*-
"""
scan port example
pip install port-scanner
"""
__author__="aaron.qiu"

import os
import portscanner

if __name__=='__main__':
    my_target = portscanner.Target("example.com")
    my_target.scan(min=1, max=100, timeout=0.01)
    my_target.report(all=True)