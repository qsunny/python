# -*- codiing:utf-8 -*-
"""
pdf添加水印
pip install PyPDF2
pip install reportlab
参考 https://cloud.tencent.com/developer/article/1778801
"""

__author__ = "aaron.qiu"

from PyPDF2 import PdfReader, PdfWriter

from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create_watermark(content):
    # 注册自定义字体（确保字体文件路径正确）
    # 例如，这里我们使用 SimHei（黑体）字体，文件名为 simhei.ttf
    pdfmetrics.registerFont(TTFont('SimHei', 'C:\\Users\\Administrator\\Desktop\\TWS\\simhei.ttf'))

    """水印信息"""
    # 默认大小为21cm*29.7cm
    file_name = "mark.pdf"
    c = canvas.Canvas(file_name, pagesize=(30*cm, 30*cm))
    # 移动坐标原点(坐标系左下为(0,0))
    c.translate(10*cm, 5*cm)

    # 设置字体
    print(c.getAvailableFonts())
    # c.setFont("Helvetica", 30)
    c.setFont("SimHei", 50)
    # 指定描边的颜色
    c.setStrokeColorRGB(0, 1, 0)
    # 指定填充颜色
    c.setFillColorRGB(0, 1, 0)
    # 旋转45度,坐标系被旋转
    c.rotate(30)
    # 指定填充颜色
    c.setFillColorRGB(0, 0, 0, 0.1)
    # 设置透明度,1为不透明
    # c.setFillAlpha(0.1)
    # 画几个文本,注意坐标系旋转的影响
    for i in range(5):
        for j in range(10):
            a=10*(i-1)
            b=5*(j-2)
            c.drawString(a*cm, b*cm, content)
            c.setFillAlpha(0.1)
    # 关闭并保存pdf文件
    c.save()
    return file_name


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
    input_pdf_path = "C:\\Users\\Administrator\\Desktop\\TWS\\TWS产品目录-定制款202410.pdf"
    output_pdf_path = "C:\\Users\\Administrator\\Desktop\\TWS\\TWS产品目录-定制款-mark202410.pdf"
    pdf_file_mark = create_watermark('TWS')
    add_watermark(input_pdf_path, pdf_file_mark, output_pdf_path)
