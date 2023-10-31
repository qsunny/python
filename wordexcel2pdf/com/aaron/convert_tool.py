# -*- codiing:utf-8 -*-
import os

import comtypes
from docx2pdf import convert
from pdfkit import from_file
from win32com.client import DispatchEx
from spire.xls import *
from spire.common import *
from win32com import client
import pandas as pd
import pandas as pd
import pdfkit

"""word、excel 转换 PDF"""
__author__ = "aaron.qiu"

"""
pip install docx2pdf
pip install pywin32
pip install comtypes

pip install Spire.XLS-for-Python
pip install plum-dispatch==1.7.4

pip install pandas
pip install pdfkit openpyxl

"""


def word2pdf(word_path='word_path', word_to_pdf='word_to_pdf'):
    """word 转 pdf"""
    for i, j, name in os.walk(word_path):
        for word_name in name:
            convert(word_path + "/" + word_name, word_to_pdf + "/" + word_name.replace("docx", "pdf"))


def excel2pdf(excel_path='excel_path', execl_pdf_path='excel_to_pdf'):
    """ excel 转 pdf
    excel_path = "D:/公众号/0626/Python研究者.xls"
    excel_pdf_path = "D:/公众号/0626/Python研究者.pdf"

    """
    xl_app = DispatchEx("Excel.Application")
    xl_app.Visible = False
    xl_app.DisplayAlerts = 0
    books = xl_app.Workbooks.Open(excel_path, False)
    books.ExportAsFixedFormat(0, execl_pdf_path)
    # books.Close(False)
    xl_app.Quit()


def excel2pdf_v2(excel_path='excel_path', execl_pdf_path='excel_to_pdf'):
    """ excel 转 pdf
    excel_path = "D:/公众号/0626/Python研究者.xls"
    excel_pdf_path = "D:/公众号/0626/Python研究者.pdf"

    """

    # Create a Workbook object
    workbook = Workbook()

    # Load an Excel document
    workbook.LoadFromFile(excel_path)

    # Iterate through the worksheets in the file
    # for sheet in workbook.Worksheets:
    #     FileName = sheet.Name + ".pdf"
    #     # Save each sheet to a separate PDF
    #     sheet.SaveToPdf(FileName)
    # workbook.Dispose()

    # Iterate through the worksheets in the workbook
    for sheet in workbook.Worksheets:
        # Get the PageSetup object
        pageSetup = sheet.PageSetup

        # Set page margins
        pageSetup.TopMargin = 0.3
        pageSetup.BottomMargin = 0.3
        pageSetup.LeftMargin = 0.3
        pageSetup.RightMargin = 0.3

    # Set worksheet to fit to page when converting
    workbook.ConverterSetting.SheetFitToPage = True

    # Convert to PDF file
    workbook.SaveToFile(execl_pdf_path, FileFormat.PDF)
    workbook.Dispose()


def excel2pdf_v3(excel_path='excel_path', execl_pdf_path='excel_to_pdf'):
    """ excel 转 pdf
    excel_path = "D:/公众号/0626/Python研究者.xls"
    excel_pdf_path = "D:/公众号/0626/Python研究者.pdf"

    """
    # 读取Excel文件
    df = pd.read_excel(excel_path)  # input
    df.to_html("file.html")  # to html
    # https://wkhtmltopdf.org/downloads.html 需要安装 wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    # pdfkit.from_string(html, 'MyPDF.pdf', configuration=config)
    pdfkit.from_file("file.html", execl_pdf_path, configuration=config)  # to pdf



def ppt2pdf(ppt_path='ppt_path', ppt_pdf_path='ppt_to_pdf'):
    """ excel 转 pdf """
    #设置路径
    # input_file_path=os.path.abspath("Python学习规划路线.pptx")
    # output_file_path=os.path.abspath("Python学习规划路线.pdf")
    #创建PDF
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    slides = powerpoint.Presentations.Open(ppt_path)
    #保存PDF
    slides.SaveAs(ppt_pdf_path, 32)
    slides.Close()


if __name__ == "__main__":
    # word_path = "D:\\temp\\word"
    # word_to_pdf = "D:\\temp\\pdf"
    # word2pdf(word_path, word_to_pdf)

    excel_path = "D:\\temp\\excel\\南港新需求V2_1010.xlsx"
    execl_pdf_path = "D:\\temp\\pdf\\南港新需求V2_1010.pdf"
    # excel2pdf(excel_path, execl_pdf_path)
    # excel2pdf_v2(excel_path, execl_pdf_path)
    excel2pdf_v3(excel_path, execl_pdf_path)

    # ppt_path = "D:\\temp\\ppt\\默予科技_20220702.pptx"
    # ppt_pdf_path = "D:\\temp\\pdf\\默予科技_20220702.pdf"
    # ppt2pdf(ppt_path, ppt_pdf_path)


