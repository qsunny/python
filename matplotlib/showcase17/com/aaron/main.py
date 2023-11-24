# -*- codiing:utf-8 -*-
import os

from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mptaches

"""Matplotlib绘图实用的小技巧 切换样式-plt.style.use"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
matplotlib支持多种样式，可以通过plt.style.use切换样式，例如：
plt.style.use('ggplot')输入plt.style.available 可以查看所有的样式:
"""

if __name__ == "__main__":
    pprint(plt.style.available)
    plt.style.use('ggplot')
    # 新建4个子图
    fig, axes = plt.subplots(2, 2)
    ax1, ax2, ax3, ax4 = axes.ravel()
    # 第一个图
    x, y = np.random.normal(size=(2, 100))
    ax1.plot(x, y, 'o')
    # 第二个图
    x = np.arange(0, 10)
    y = np.arange(0, 10)
    colors = plt.rcParams['axes.prop_cycle']
    length = np.linspace(0, 10, len(colors))
    for s in length:
        ax2.plot(x, y + s, '-')
    # 第三个图
    x = np.arange(5)
    y1, y2, y3 = np.random.randint(1, 25, size=(3, 5))
    width = 0.25
    ax3.bar(x, y1, width)
    ax3.bar(x + width, y2, width)
    ax3.bar(x + 2 * width, y3, width)
    # 第四个图
    for i, color in enumerate(colors):
        xy = np.random.normal(size=2)
    ax4.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
    ax4.axis('equal')
    plt.show()