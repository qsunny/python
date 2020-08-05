# _*_ encoding:utf-8 _*_
"""
read package data test
"""
__author__="aaron.qiu"

import pkgutil
from io import StringIO



class PackageTest:
    """包测试对象"""

    def read_data(self):
        data = pkgutil.get_data('com.aaron.pkg', 'test.dat')
        print(f"读取到包的数据:{data}")


if __name__ == "__main__":
    pkg_test = PackageTest()
    pkg_test.read_data()
