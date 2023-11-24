# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 调整坐标轴范围-axis/xlim/ylim"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
axis：[0,5,0,10]，x从0到5，y从0到10
xlim：对应参数有xmin和xmax，分别能调整最大值最小值
ylim：同xlim用法
"""

if __name__ == "__main__":
    x = np.arange(0, 30, 1)
    plt.plot(x, x * x)
    # 显示坐标轴，plt.axis(),4个数字分别代表x轴和y轴的最小坐标，最大坐标
    # 调整x为10到25
    plt.xlim(xmin=10, xmax=25)
    plt.plot(x, x * x)
    plt.show()