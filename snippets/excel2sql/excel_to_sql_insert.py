# -*- codiing:utf-8 -*-
"""
pip install pandas openpyxl
读取excel中字段、拼接sql语句
"""

__author__ = "aaron.qiu"

import pandas as pd

# Function to read Excel file and generate SQL insert statements
def excel_to_sql_insert(excel_file, sheet_name, table_name):
    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Assuming the first row contains column names, if not, adjust accordingly
    columns = df.columns.tolist()

    # Generate SQL insert statements
    sql_inserts = []
    for i, row in df.iterrows():
        values = ", ".join([f"'{str(value)}'" for value in row])
        sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values});"
        sql_inserts.append(sql)

    return sql_inserts

# Example usage
if __name__ == "__main__":
    excel_file = "C:\\Users\\Administrator\\Desktop\\万泓五金商品.xlsx"  # Replace with your Excel file path
    sheet_name = "Sheet2"     # Replace with your sheet name
    table_name = "t_retail_product" # Replace with your SQL table name

    sql_inserts = excel_to_sql_insert(excel_file, sheet_name, table_name)

    # Print out the SQL insert statements
    for sql in sql_inserts:
        print(sql)

    # Optionally, you can write these SQL insert statements to a file
    with open("insert_statements.sql", "w", encoding="utf-8") as f:
        for sql in sql_inserts:
            f.write(sql + "\n")
