# _*_ encoding:utf-8 _*_
"""
panadas read excel test
"""
__author__="aaron.qiu"

import json
import pandas as pd


def read_excel():
    """读取excel file"""
    # keep_default_na=False
    df = pd.read_excel(r"C:\\Users\\Administrator\\Desktop\\pandas_test.xlsx", usecols=[1, 2],  nrows=3, header=None,  keep_default_na=False)
    # 获取总和、得出行数和列数
    ss_count = df.shape
    print(df)
    line = ss_count[0]
    row = ss_count[1]

    df.to_excel(r"C:\\Users\\Administrator\\Desktop\\pandas_test_result.xlsx")


if __name__ == "__main__":
    read_excel()

