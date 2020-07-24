import pandas as pd
from pandas import DataFrame
import logging
import json


logging.basicConfig(
    filename='application.log',
    level=logging.WARNING,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


if __name__ == '__main__':
    csv_file_path = 'E:/aaron/document/db/product/prod/part_number/part_number20200724_25.csv'
    try:
        df = pd.read_csv(csv_file_path, dtype=object)
        print(df)
        print("==========================")
        # for index, row in df.iterrows():
        #     part_number = row["part_number"]
        #     print(index, part_number)
        df = df.groupby('part_number').sum()
        print(type(df))
        print(df)
        df.to_csv('D://part.csv')

    except Exception as e:
        logging.error(e)


