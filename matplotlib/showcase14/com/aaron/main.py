# -*- codiing:utf-8 -*-
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 填充区域-fill/fill_beween"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    # fill 填充函数区域
    # 显示中文
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = np.linspace(0, 5 * np.pi, 1000)
    y1 = np.sin(x)
    y2 = np.sin(2 * x)
    plt.plot(x, y1)
    plt.plot(x, y2)
    # 填充
    plt.fill(x, y1, 'g')
    plt.fill(x, y2, 'r')
    plt.title('这是一个示例标题')
    plt.show()