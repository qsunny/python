# -*- codiing:utf-8 -*-
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 填充区域-fill/fill_beween"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
fill_beween填充函数交叉区域
"""

if __name__ == "__main__":
    # 显示中文
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('这是一个示例标题')
    x = np.linspace(0, 5 * np.pi, 1000)
    y1 = np.sin(x)
    y2 = np.sin(2 * x)
    plt.plot(x, y1)
    plt.plot(x, y2)
    # 填充
    plt.fill_between(x, y1, y2, where=y1 > y2, interpolate=True)
    plt.show()