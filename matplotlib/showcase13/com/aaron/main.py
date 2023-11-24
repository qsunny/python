# -*- codiing:utf-8 -*-
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 添加双坐标轴-twinx"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    x = np.arange(1, 20)
    y1 = x * x
    y2 = np.log(x)
    plt.plot(x, y1)
    # 添加一个坐标轴，默认0到1
    plt.twinx()
    plt.plot(x, y2, 'r')
    plt.show()