# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 设置坐标轴名称-xlabel/ylabel"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    # 显示中文
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = np.arange(1, 20)
    plt.xlabel('示例x轴')
    plt.ylabel('示例y轴')
    plt.plot(x, x * x)
    plt.show()