# -*- codiing:utf-8 -*-
"""
gzip zipfile tarfile example
"""
__author__="aaron.qiu"

import os, shutil, glob
from pprint import pprint
import zlib, gzip, bz2, zipfile, tarfile

def zlib_showcase():
    """
    zlib 提供了对字符串进行压缩和解压缩的功能
    """
    orginal = "this is a test string"
    compressed = zlib.compress(orginal.encode(encoding="utf-8"))
    depressed = zlib.decompress(compressed).decode()
    print(compressed)
    print(depressed)
    #校验
    print(zlib.adler32(orginal.encode(encoding="utf-8")) & 0xffffffff)
    print(zlib.crc32(orginal.encode(encoding="utf-8")) & 0xffffffff)

def gzip_showcase():
    content = "Lots of content here"
    with gzip.open('file.txt.gz', 'wb') as f:
        f.write(content.encode(encoding="utf-8"))

    with gzip.open('file.txt.gz', 'rb') as f:
        file_content = f.read()
        print(file_content.decode())

    with gzip.open('file.txt.gz', 'rb') as f_in, open('file.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

    with open("file.txt") as f:
        print(f.read())

    os.remove("file.txt.gz")
    os.remove("file.txt")


if __name__ == "__main__":
    zlib_showcase()
    gzip_showcase()









