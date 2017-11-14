# _*_ encoding:utf-8 _*_

"""a test module"""
__author__ = 'Aaron.qiu'

import json
import os
from pprint import pprint
from sysexample import print_hello

def load_json():
    info_string = """
    {
        "name": "echo",
        "age": 24,
        "coding skills": ["python", "matlab", "java", "c", "c++", "ruby", "scala"],
        "ages for school": { 
            "primary school": 6,
            "middle school": 9,
            "high school": 15,
            "university": 18
        },
        "hobby": ["sports", "reading"],
        "married": false
    }
    """
    info = json.loads(info_string)
    pprint(info)
    pprint(info['name'])
    pprint(type(info))
    json_info = json.dumps(info)
    pprint(json_info)
    pprint(type(json_info))

def write_jsonfile():
    info_string = """
    {
        "name": "echo",
        "age": 24,
        "coding skills": ["python", "matlab", "java", "c", "c++", "ruby", "scala"],
        "ages for school": { 
            "primary school": 6,
            "middle school": 9,
            "high school": 15,
            "university": 18
        },
        "hobby": ["sports", "reading"],
        "married": false
    }
    """
    with open("info.json", "w") as f:
        info = json.loads(info_string)
        json.dump(info, f)

def load_json_fromfile():
    with open("info.json") as f:
        pprint(f.read())

def load_json_fromfile2():
    with open("info.json") as f:
        info_from_file = json.load(f)
        pprint(info_from_file)

if __name__=="__main__" :
    print_hello()
    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
    #load_json()
    write_jsonfile()
    #load_json_fromfile()
    load_json_fromfile2()
    os.remove("info.json")