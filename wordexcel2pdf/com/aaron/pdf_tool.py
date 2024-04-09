import pdfplumber

"""PDF 内容抽取"""
__author__ = "aaron.qiu"

"""
pip install pdfplumber

pdfplumber < background-checks.pdf > background-checks.csv

https://github.com/jsvine/pdfplumber?tab=readme-ov-file#visual-debugging
https://blog.csdn.net/fuhanghang/article/details/122579548
https://github.com/jsvine/pdfplumber/blob/stable/examples/notebooks/extract-table-ca-warn-report.ipynb
"""


def extract_content():
    with pdfplumber.open("background-checks.pdf") as pdf:
        first_page = pdf.pages[0]
        print(first_page.chars[0])
        print(first_page.extract_table())
        print(first_page.extract_text())


if __name__ == "__main__":
    extract_content()