# -*- codiing:utf-8 -*-
"""
pip install pandas openpyxl
读取excel中字段、拼接sql语句
"""

__author__ = "aaron.qiu"

import datetime

import random
import string

import pandas as pd

import openpyxl

class ExcelReader:
    def __init__(self, filename):
        self.filename = filename
        self.workbook = None
        self.sheet = None

    def open_workbook(self):
        self.workbook = openpyxl.load_workbook(self.filename)

    def select_sheet(self, sheet_name):
        self.sheet = self.workbook[sheet_name]

    def read_content(self):
        content = []
        for row in self.sheet.iter_rows():
            row_data = []
            for cell in row:
                row_data.append(cell.value)
            content.append(row_data)
        return content

    def convert_to_string(self, content):
        content_string = ''
        for row in content:
            row_string = '\t'.join([str(cell) for cell in row])
            content_string += row_string + '\n'
        return content_string


def getProductNumber():
    now = datetime.datetime.now()
    # "%Y-%m-%d %H:%M:%S"
    formatted_time = now.strftime("%Y%m%d")
    # print(formatted_time)

    random_num_list = random.sample(string.digits, 6)
    random_num_str = ''.join(random_num_list)
    # co103711420240717816509
    product_number = 'co1037114{0}{1}'.format(formatted_time, random_num_str)

    return product_number


if  __name__ == "__main__":
    # 读取Excel文件
    # df = pd.read_excel('C:\\Users\\Administrator\\Desktop\\万泓五金商品.xlsx')

    # 显示数据框内容
    # print(df)

    # filename = 'C:\\Users\\Administrator\\Desktop\\万泓五金商品.xlsx'
    # reader = ExcelReader(filename)
    # reader.open_workbook()
    # reader.select_sheet('Sheet2')
    # content = reader.read_content()
    # content_string = reader.convert_to_string(content)
    # print(content_string)
    for x in range(100):
        product_number = getProductNumber()
        print(product_number)



