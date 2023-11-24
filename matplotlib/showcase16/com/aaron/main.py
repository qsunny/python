# -*- codiing:utf-8 -*-
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mptaches

"""Matplotlib绘图实用的小技巧 画一个填充好的形状-matplotlib.patche"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    xy1 = np.array([0.2, 0.2])
    xy2 = np.array([0.2, 0.8])
    xy3 = np.array([0.8, 0.2])
    xy4 = np.array([0.8, 0.8])
    fig, ax = plt.subplots()
    # 圆形,指定坐标和半径
    circle = mptaches.Circle(xy1, 0.15)
    ax.add_patch(circle)
    # 长方形
    rect = mptaches.Rectangle(xy2, 0.2, 0.1, color='r')
    ax.add_patch(rect)
    # 多边形
    polygon = mptaches.RegularPolygon(xy3, 6, radius=0.2, color='g')
    ax.add_patch(polygon)
    # 椭圆
    ellipse = mptaches.Ellipse(xy4, 0.4, 0.2, color='c')
    ax.add_patch(ellipse)
    ax.axis('equal')
    plt.show()