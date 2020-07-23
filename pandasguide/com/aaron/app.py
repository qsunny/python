import pandas as pd
import logging

logging.basicConfig(
    filename='application.log',
    level=logging.WARNING,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


if __name__ == '__main__':
    csv_file_path = 'C:/Users/Administrator/Desktop/F001_ware.csv'
    try:
        data = pd.read_csv(csv_file_path, dtype=object)
        print(data)
        logging.info(data)
        print("==========================")
        for index, row in data.iterrows():
            print(index, row["id"], row["thirdparty_part_number"], row['vendor_code'])
    except Exception as e:
        logging.error(e)

