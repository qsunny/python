# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 添加标题"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    # 显示中文
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = np.arange(0, 10)
    plt.title('这是一个示例标题')
    plt.plot(x, x * x)
    plt.show()