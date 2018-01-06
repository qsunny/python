# -*- codiing:utf-8 -*-
"""
request example
pip install requests
requests 模块号称 HTTP for Human
"""
__author__="aaron.qiu"

import requests

def show_url_ip():
    response = requests.get('https://httpbin.org/ip')
    print('Your IP is {0}'.format(response.json()['origin']))



if __name__=="__main__":
    show_url_ip()


