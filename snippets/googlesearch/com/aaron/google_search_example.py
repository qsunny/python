# -*- codiing:utf-8 -*-
"""
测试你的 Internet 速度
pip install google
"""

__author__ = "aaron.qiu"

from pprint import pprint
from googlesearch import search

if __name__ == "__main__":
    query = "Medium.com"

    for url in search(query):
        print(url)
