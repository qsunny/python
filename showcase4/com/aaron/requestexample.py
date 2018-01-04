# -*- codiing:utf-8 -*-
"""
request example
pip install requests
requests 模块号称 HTTP for Human
"""
__author__="aaron.qiu"

import requests
from pprint import pprint

def custom_op():
    r = requests.get("http://httpbin.org/get")
    r = requests.post('http://httpbin.org/post', data={'key': 'value'})
    r = requests.put("http://httpbin.org/put")
    r = requests.delete("http://httpbin.org/delete")
    r = requests.head("http://httpbin.org/get")
    r = requests.options("http://httpbin.org/get")
    print(r)

def payload_op():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)
    pprint(r)
    print(r.url)

def read_json():
    r = requests.get('https://github.com/timeline.json')
    print(r.text)
    print(r.encoding)
    print(r.json())

def get_http_status_code():
    r = requests.get('http://httpbin.org/get')
    print(r.status_code)
    pprint(r.headers['Content-Type'])

if __name__=="__main__":
    custom_op()
    payload_op()
    read_json()
    get_http_status_code()


