# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 调整颜色-color"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    x = np.arange(1, 5)
    # 颜色的几种方式
    plt.plot(x, color='g')
    plt.plot(x + 1, color='0.5')
    plt.plot(x + 2, color='#FF00FF')
    plt.plot(x + 3, color=(0.1, 0.2, 0.3))
    plt.show()