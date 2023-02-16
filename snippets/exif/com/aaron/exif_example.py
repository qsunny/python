# -*- codiing:utf-8 -*-
"""
测试你的 Internet 速度
pip install ExifRead
"""

__author__ = "aaron.qiu"

from pprint import pprint

import PIL.Image
import PIL.ExifTags
import exifread

def read_exIf_method1(img):

    img = PIL.Image.open("92710.png")
    exif_data = {
        PIL.ExifTags.TAGS[i]: j
            for i, j in img._getexif().items()
            if i in PIL.ExifTags.TAGS
    }
    print(exif_data)


def read_exIf_method2(path_name):
    filename = open(path_name, 'rb')
    tags = exifread.process_file(filename)
    print(tags)


if __name__ == "__main__":
    # Method 1
    read_exIf_method1(None)
    # Method 2


