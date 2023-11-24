# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 调整坐标轴刻度-locator_params"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
坐标图的刻度我们可以使用 locator_params 接口来调整显示颗粒。
同时调整 x 轴和 y 轴：plt.locator_params(nbins=20)
只调整 x 轴：plt.locator_params(‘'x',nbins=20)
只调整 y 轴：plt.locator_params(‘'y',nbins=20)
"""

if __name__ == "__main__":
    x = np.arange(0, 30, 1)
    plt.plot(x, x)
    # x轴和y轴分别显示20个
    plt.locator_params(nbins=20)
    plt.show()