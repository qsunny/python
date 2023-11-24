# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 添加注释"""
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
    plt.title('这是一个示例标题')
    plt.plot(x, y)
    # 添加注释
    # xy 参数：备注的坐标点
    # xytext  参数：备注文字的坐标(默认为xy的位置)
    # arrowprops 参数：在xy和xytext之间绘制一个箭头。
    plt.annotate('这是一个示例注释', xy=(0, 1), xytext=(-2, 22), arrowprops={'headwidth': 10, 'facecolor': 'r'})
    plt.show()