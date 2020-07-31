# _*_ encoding:utf-8 _*_
"""
es query test
pip install requests
requests 模块号称 HTTP for Human
"""
__author__="aaron.qiu"

import requests
from pprint import pprint
import json
import pandas as pd

# ES_URL = 'http://192.168.1.105:9200/test_partnum_entity_alias/_search'
ES_URL = 'http://172.19.106.187:9200/partnum_entity_alias/_search'


def query_param():
    # keep_default_na=False
    df = pd.read_excel(r"C:\\Users\\Administrator\\Desktop\\连接器数据0731.xlsx", header=None, index=False, keep_default_na=False)
    # 获取总和、得出行数和列数
    ss_count = df.shape
    # df.to_csv(r"C:\\Users\\Administrator\\Desktop\\连接器11.csv")

    line = ss_count[0]
    row = ss_count[1]

    for j_line in range(line):  # j为行
        aa = ''

        for i in range(row):
            aa += str(df.loc[j_line].iloc[i]).replace('\n', '') + ' '  # 同时去除换行符
        # print(aa)
        query(aa)


def query(line_content):
    if not line_content:
        return
    json_param = {
      "_source": ["paramDesc", "partDesc", "partNumber", "categoryNameParticiple", "categoryNameSeparate"],
      "from": 0,
      "size": 10,
      "query": {
        "query_string": {
          "default_field": "partDesc.keyword",
            "default_operator": "and",
            "query": line_content
        }
      }
    }
    try:
        r = requests.post(ES_URL, json=json_param, timeout=5)
        if r.status_code == 200:
            result = json.loads(r.content)
            # pprint(result)
            # print("查询结果:{}".format(result['hits']['total']))
            if result['hits']['total']['value'] > 0:
                print(f"查询条件:{line_content}")
                print(result['hits']['hits'])
        else:
            pprint(r.reason)
    except Exception as e:
        pprint(e)


if __name__ == "__main__":
    query_param()

