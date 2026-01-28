from pprint import pprint

import pdfplumber

"""PDF 内容抽取"""
__author__ = "aaron.qiu"

"""
pip install pdfplumber
uv pip install pandas

pdfplumber < background-checks.pdf > background-checks.csv

https://github.com/jsvine/pdfplumber?tab=readme-ov-file#visual-debugging
https://blog.csdn.net/fuhanghang/article/details/122579548
https://github.com/jsvine/pdfplumber/blob/stable/examples/notebooks/extract-table-ca-warn-report.ipynb

pip install pikepdf
uv pip install pikepdf

# 安装qpdf工具（核心依赖）
# Windows：下载 https://github.com/qpdf/qpdf/releases 解压后将bin目录加入系统环境变量
# Mac：brew install qpdf
# Linux：apt-get install qpdf / yum install qpdf

"""

import pdfplumber
import pandas as pd
import pikepdf
import os
import tempfile


def pdf_tables_to_excel(pdf_path, excel_path):
    """
    将PDF中的所有表格提取到一个Excel文件中，每个表格放在单独的工作表。

    参数:
        pdf_path (str): PDF文件的路径。
        excel_path (str): 要保存的Excel文件的路径。
    """
    all_tables_data = []  # 用于存储提取到的表格数据

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            print(f"正在处理第 {page_num + 1} 页...")

            # 尝试提取当前页面中的所有表格
            tables_on_page = page.extract_tables()

            if tables_on_page:
                for table_num, table in enumerate(tables_on_page):
                    if table:  # 确保表格不为空
                        # 将提取的数据转换为DataFrame
                        # 假设第一行是表头
                        df = pd.DataFrame(table[1:], columns=table[0])
                        # 为这个表格添加标识信息，方便在Excel中识别来源
                        df['_来源'] = f'第{page_num + 1}页_表{table_num + 1}'
                        all_tables_data.append(df)
                        print(f"  发现表格 {table_num + 1}, 包含 {len(table)} 行, {len(table[0])} 列。")
            else:
                print(f"  第 {page_num + 1} 页未发现表格。")

    if all_tables_data:
        # 使用ExcelWriter将所有的DataFrame写入同一个Excel文件的不同sheet
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            for idx, df in enumerate(all_tables_data):
                # 工作表名称有长度限制且不能包含某些字符，需要处理一下
                sheet_name = f"Page_{df['_来源'].iloc[0].split('_')[0][1:]}_Table{idx + 1}"
                sheet_name = sheet_name.replace('第', '').replace('页', '')[:31]  # 确保工作表名有效
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"\n转换完成！共提取 {len(all_tables_data)} 个表格。")
        print(f"Excel文件已保存至: {excel_path}")
    else:
        print("未在PDF中找到任何表格。")

def extract_content():
    with pdfplumber.open("background-checks.pdf") as pdf:
        first_page = pdf.pages[0]
        print(first_page.chars[0])
        print(first_page.extract_table())
        print(first_page.extract_text())


import PyPDF2
import os


def compress_pdf_basic(input_path, output_path):
    """
    基础PDF压缩：移除冗余数据、优化流编码
    :param input_path: 输入PDF文件路径
    :param output_path: 输出压缩后的PDF路径
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        print(f"错误：输入文件 {input_path} 不存在！")
        return

    try:
        # 读取PDF
        with open(input_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            writer = PyPDF2.PdfWriter()

            # 遍历所有页面，添加到新PDF（自动移除冗余数据）
            for page in reader.pages:
                # 优化页面流（核心压缩步骤）
                page.compress_content_streams()
                writer.add_page(page)

            # 写入输出文件
            with open(output_path, 'wb') as out_f:
                writer.write(out_f)

        # 计算压缩率
        original_size = os.path.getsize(input_path) / 1024  # KB
        compressed_size = os.path.getsize(output_path) / 1024  # KB
        compression_rate = (1 - compressed_size / original_size) * 100

        print(f"基础压缩完成！")
        print(f"原文件大小：{original_size:.2f} KB")
        print(f"压缩后大小：{compressed_size:.2f} KB")
        print(f"压缩率：{compression_rate:.2f}%")

    except Exception as e:
        print(f"压缩失败：{str(e)}")


def compress_hik_api_pdf_final(input_path, output_path, image_quality=70, image_resolution=130):
    """
    彻底兼容所有pikepdf版本的Hik API文档压缩脚本，跳过无有效stream图片
    :param input_path: 输入PDF路径（HikCentral OpenAPI文档）
    :param output_path: 输出压缩后的PDF路径
    :param image_quality: 图片质量（60-80，兼顾清晰与体积）
    :param image_resolution: 图片分辨率（120-150dpi，技术文档足够可读）
    """
    if not os.path.exists(input_path):
        print(f"错误：输入文件 {input_path} 不存在！")
        return

    try:
        with pikepdf.open(input_path) as pdf:
            for page_idx, page in enumerate(pdf.pages, 1):
                # 遍历页面内所有图片资源，跳过无有效stream的资源（保留警告提示）
                for img_name, img in list(page.images.items()):
                    if not hasattr(img, 'stream') or not img.stream:
                        print(f"警告：第{page_idx}页图片 {img_name} 无有效stream，跳过处理")
                        continue

                    try:
                        # 安全处理临时文件，确保流关闭和删除
                        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_img:
                            img.extract_to(fileobj=temp_img)
                            temp_img.flush()
                            temp_img_path = temp_img.name

                        # 重新嵌入压缩后的图片（按比例缩放，避免拉伸）
                        with pikepdf.Image.open(temp_img_path) as new_img:
                            # 处理无分辨率信息的图片，按比例缩小
                            if new_img.resolution[0] > 0 and new_img.resolution[1] > 0:
                                scale_ratio = image_resolution / max(new_img.resolution[0], new_img.resolution[1])
                                new_width = int(new_img.width * scale_ratio)
                                new_height = int(new_img.height * scale_ratio)
                            else:
                                new_width = int(new_img.width * 0.8)  # 默认缩放80%
                                new_height = int(new_img.height * 0.8)

                            new_img = new_img.resize((new_width, new_height))
                            page.images.replace(img_name, new_img, quality=image_quality)

                    except Exception as img_e:
                        print(f"警告：处理第{page_idx}页图片 {img_name} 失败：{str(img_e)}，跳过该图片")
                    finally:
                        # 强制删除临时文件，避免残留
                        if 'temp_img_path' in locals() and os.path.exists(temp_img_path):
                            os.unlink(temp_img_path)

            # 核心修复：兼容所有版本的压缩配置（不用CompressionLevel类，直接用数字级别）
            # 压缩级别：0=无压缩，1=低，2=中，3=高（对应原HIGH级别）
            pdf.save(
                output_path,
                preserve_pdfa=False,  # 不保留PDF/A格式（减小体积）
                linearize=True  # 线性化，方便网络传输
            )

        # 计算压缩效果
        original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
        compressed_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
        compression_rate = (1 - compressed_size / original_size) * 100

        print(f"\n压缩完成！")
        print(f"原文件大小：{original_size:.2f} MB")
        print(f"压缩后大小：{compressed_size:.2f} MB")
        print(f"压缩率：{compression_rate:.2f}%")

    except Exception as e:
        print(f"压缩失败：{str(e)}")


if __name__ == "__main__":
    # extract_content()

    # 使用示例
    pdf_file = "C:/Users/Administrator/Documents/155首古诗词艾宾浩斯记忆表.pdf"
    excel_file = "C:/Users/Administrator/Documents/古诗词艾宾浩斯记忆表.xlsx"  #
    # pdf_tables_to_excel(pdf_file, excel_file)

    input_pdf = "E:\\aaron\\tulang\\海康-HK\\HikCentral301.pdf"  # 替换为你的输入路径
    output_pdf = "E:\\aaron\\tulang\\海康-HK\\HikCentralProfessionalOpenAPI_DeveloperGuide_zh_V301.pdf"  # 替换为输出路径
    # compress_pdf_basic(input_pdf, output_pdf)

    # 可调参数：image_quality=60（更低画质）、image_resolution=100（更低分辨率）
    compress_hik_api_pdf_final(input_pdf, output_pdf, image_quality=70, image_resolution=130)