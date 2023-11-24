# -*- codiing:utf-8 -*-
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 调整日期自适应-autofmt_xdate"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
非常不友好，调用plt.gcf().autofmt_xdate()，将自动调整角度。
"""

if __name__ == "__main__":
    x = pd.date_range('2020/01/01', periods=30)
    y = np.arange(0, 30, 1)
    plt.plot(x, y)
    plt.gcf().autofmt_xdate()
    plt.show()