# -*- codiing:utf-8 -*-
"""
pdf添加水印
pip install PyPDF2
参考 https://cloud.tencent.com/developer/article/1778801
"""

__author__ = "aaron.qiu"

from PyPDF2 import PdfReader, PdfWriter


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = len(pdf_input.pages)

    # 读入水印pdf文件
    pdf_watermark = PdfReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.pages[i]
        page.merge_page(pdf_watermark.pages[0])
        page.compress_content_streams()  # 压缩内容
        pdf_output.add_page(page)
    pdf_output.write(open(pdf_file_out, 'wb'))


if __name__ == "__main__":
    # 使用函数添加水印
    input_pdf_path = "C:\\Users\\Administrator\\Desktop\\TWS\\TWS产品目录通用版202410.pdf"
    output_pdf_path = "C:\\Users\\Administrator\\Desktop\\TWS\\TWS产品目录通用版-mark202410.pdf"
    pdf_file_mark = "C:\\Users\\Administrator\\Desktop\\TWS\\watermark.pdf"
    add_watermark(input_pdf_path, pdf_file_mark, output_pdf_path)
