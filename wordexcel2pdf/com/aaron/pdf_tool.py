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
"""

import pdfplumber
import pandas as pd


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


if __name__ == "__main__":
    # extract_content()

    # 使用示例
    pdf_file = "C:/Users/Administrator/Documents/155首古诗词艾宾浩斯记忆表.pdf"
    excel_file = "C:/Users/Administrator/Documents/古诗词艾宾浩斯记忆表.xlsx"  #
    pdf_tables_to_excel(pdf_file, excel_file)