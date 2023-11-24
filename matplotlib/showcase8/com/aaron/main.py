# -*- codiing:utf-8 -*-
import os

import numpy as np
import matplotlib.pyplot as plt

"""Matplotlib绘图实用的小技巧 显示数学公式-mathtext"""
__author__ = "aaron.qiu"


"""
pip install matplotlib
"""

if __name__ == "__main__":
    plt.title('chenqionghe')
    plt.xlim([1, 8])
    plt.ylim([1, 5])
    plt.text(2, 4, r'$ \alpha \beta \pi \lambda \omega $', size=25)
    plt.text(4, 4, r'$ \sin(0)=\cos(\frac{\pi}{2}) $', size=25)
    plt.text(2, 2, r'$ \lim_{x \rightarrow y} \frac{1}{x^3} $', size=25)
    plt.text(4, 2, r'$ \sqrt[4]{x}=\sqrt{y} $', size=25)
    plt.show()