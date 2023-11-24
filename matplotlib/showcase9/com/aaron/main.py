# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 显示网格-grid"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    x = 'a', 'b', 'c', 'd'
    y = [15, 30, 45, 10]
    plt.grid()
    # 也可以设置颜色、线条宽度、线条样式
    # plt.grid(color='g',linewidth='1',linestyle='-.')
    plt.plot(x, y)
    plt.show()