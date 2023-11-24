# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 添加图例-legend"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    # 显示中文
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = np.arange(2.5, 20, 1)
    plt.plot(x, x)
    plt.plot(x, x * 2)
    plt.plot(x, x * 3)
    plt.plot(x, x * 4)
    # 直接传入legend
    plt.legend(['生活', '颜值', '工作', '金钱'])
    plt.show()