# -*- codiing:utf-8 -*-
"""pickle example"""
__author__="aaron.qiu"

import pprint
import os

try:
    import cPickle as pickle
except:
    import pickle

def pickle_showcase():
    """
        参考:https://github.com/lijin-THU/notes-python/blob/master/11-useful-tools/11.02-pickle-and-cPickle.ipynb
        pickle.dumps()将对象转化为字符串
        0：原始的 ASCII 编码格式
        1：二进制编码格式
        2：更有效的二进制编码格式
    """
    data = [{'a': 'A', 'b': 2, 'c': 3.0}]
    data_string = pickle.dumps(data,2)
    pprint.pprint(data)
    pprint.pprint(data_string)
    # 解码
    data_from_string = pickle.loads(data_string)
    pprint.pprint(data_from_string)

def pickle_writefile_showcase():
    with open("data.pkl", "wb") as f:
        data = [{'a': 'A', 'b': 2, 'c': 3.0}]
        pickle.dump(data,f,2)

def pickle_loadfile_showcase():
    with open("data.pkl","rb") as f:
        data_from_file = pickle.load(f)
        pprint.pprint(data_from_file)



if __name__=="__main__":
    pickle_showcase()
    pickle_writefile_showcase()
    pickle_loadfile_showcase()
    os.remove("data.pkl")
