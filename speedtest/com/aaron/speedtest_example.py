# -*- codiing:utf-8 -*-
"""
测试你的 Internet 速度
pip install pyspeedtest
pip install speedtest  暂不安装,异常找不到属性 pip uninstall speedtest
pip install speedtest-cli
"""

__author__ = "aaron.qiu"

from pprint import pprint
import speedtest

if __name__ == "__main__":

    test = speedtest.Speedtest()

    print("Loading server list...")
    test.get_servers()
    print("Choosing best server...")
    best = test.get_best_server()

    print(f"Found: {best['host']} located in {best['country']}")

    print("Performing download test...")
    download_result = test.download()
    print("Performing upload test...")
    upload_result = test.upload()
    ping_result = test.results.ping

    print(f"Download speed: {download_result / 1024 / 1024:.2f}Mbit/s")
    print(f"Upload speed: {upload_result / 1024 / 1024:.2f}Mbit/s")
    print(f"Ping: {ping_result}ms")
