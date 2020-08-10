# _*_ encoding:utf-8 _*_
"""
pip install you-get
https://you-get.org/
"""
__author__ = "aaron.qiu"

from you_get.common import any_download
from you_get.__main__ import main_dev

if __name__ == '__main__':
    any_download(url="https://www.youtube.com/watch?v=QuPiZ86EFhQ", output_dir="E:\\", merge="E:\\")
    # any_download(url="https://www.youtube.com/watch?v=jNQXAC9IVRw", output_dir="E:\\", merge="E:\\")
