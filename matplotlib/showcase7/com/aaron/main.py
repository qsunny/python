# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 切换线条样式-marker"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
其中 marker 支持的类型：
‘.’：点(point marker)

‘,’：像素点(pixel marker)

‘o’：圆形(circle marker)

‘v’：朝下三角形(triangle_down marker)

‘^’：朝上三角形(triangle_up marker)

‘<‘：朝左三角形(triangle_left marker)

‘>’：朝右三角形(triangle_right marker)

‘1’：(tri_down marker)

‘2’：(tri_up marker)

‘3’：(tri_left marker)

‘4’：(tri_right marker)

‘s’：正方形(square marker)

‘p’：五边星(pentagon marker)

‘*’：星型(star marker)

‘h’：1号六角形(hexagon1 marker)

‘H’：2号六角形(hexagon2 marker)

‘+’：+号标记(plus marker)

‘x’：x号标记(x marker)

‘D’：菱形(diamond marker)

‘d’：小型菱形(thin_diamond marker)

‘|’：垂直线形(vline marker)

‘_’：水平线形(hline marker)
"""

if __name__ == "__main__":
    x = np.arange(1, 5)
    plt.plot(x, marker='o')
    plt.plot(x + 1, marker='>')
    plt.plot(x + 2, marker='d')
    plt.show()