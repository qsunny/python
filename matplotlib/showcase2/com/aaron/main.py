# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 添加文字"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    # 显示中文
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x = np.arange(-10, 11, 1)
    y = x * x
    plt.plot(x, y)
    plt.title('这是一个示例标题')
    # 添加文字
    plt.text(-2.5, 30, 'function y=x*x')
    plt.show()