import pandas as pd
import logging
import json


logging.basicConfig(
    filename='application.log',
    level=logging.WARNING,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


if __name__ == '__main__':
    # csv_file_path = 'C:/Users/Administrator/Desktop/F001_ware.csv'
    csv_file_path = 'C:/Users/Administrator/Desktop/brand20200724.csv'
    try:
        data = pd.read_csv(csv_file_path, dtype=object)
        print(data)
        logging.info(data)
        print("==========================")
        # file = open("C:/Users/Administrator/Desktop/brand20200724_1.csv", "a+")
        for index, row in data.iterrows():
            # print(index, row["id"], row["thirdparty_part_number"], row['vendor_code'])
            # print(index, row["cn_name"], row["brand_alias"])
            brand_alias = row["brand_alias"]
            cn_name = row["cn_name"]
            # file.write(cn_name + "\n")
            print(cn_name)
            json_arr = json.loads(brand_alias)
            # print(json_arr)
            # brand_list = []
            for obj in json_arr:
                # brand_list.append(obj['alias'])
                # file.write(obj['alias']+"\n")
                print(obj['alias'])
            # print("Python 原始数据：", repr(data))
            # pd.DataFrame(brand_list).to_csv("C:/Users/Administrator/Desktop/brand20200724_1.csv", columns=['品牌名称'], index=0)
        # file.close()
    except Exception as e:
        logging.error(e)


