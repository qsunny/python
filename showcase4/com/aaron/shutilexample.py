# -*- codiing:utf-8 -*-
"""
shutil example
shutil 是 Python 中的高级文件操作模块。
"""
__author__="aaron.qiu"

import pprint
import os,shutil

def shutil_showcase():
    with open("test.file", "w") as f:
        pass
    print("test.file" in os.listdir(os.curdir))

def shutil_copy_showcase():
    """
    shutil.copy(knowledge, dst) 将源文件复制到目标地址
    shutil.copyfile(knowledge, dst) 与 shutil.copy 使用方法一致，
    不过只是简单复制文件的内容，并不会复制文件本身的读写可执行权限，而 shutil.copy 则是完全复制。
    """
    shutil.copy("test.file", "test.copy.file")
    print("test.file" in os.listdir(os.curdir))
    print("test.copy.file" in os.listdir(os.curdir))
    try:
        shutil.copy("test.file", "my_test_dir/test.copy.file")
    except IOError as msg:
        print(msg)

def shutil_move_folder():
    """
    shutil.move 可以整体移动文件夹，与 os.rename 功能差不多
    """
    os.renames("test.file", "test_dir/test.file")
    os.renames("test.copy.file", "test_dir/test.copy.file")

def shutil_copy_folder():
    """复制文件夹"""
    shutil.copytree("test_dir/", "test_dir_copy/")
    "test_dir_copy" in os.listdir(os.curdir)

def shutil_del_folder():
    """
    os.removedirs 不能删除非空文件夹
    使用 shutil.rmtree 来删除非空文件夹：
    """
    try:
        os.removedirs("test_dir_copy")

    except Exception as msg:
        print(msg)

    shutil.rmtree("test_dir_copy")
    shutil.rmtree("test_dir")

def shutil_make_archive():
    """
        产生压缩文件
    """
    # 支持压缩的类型
    archive_formats = shutil.get_archive_formats()
    print(archive_formats)
    shutil.make_archive("test_archive", "zip", "test_dir/")

if __name__=="__main__":
    #shutil_del_folder()
    shutil_showcase()
    shutil_copy_showcase()
    shutil_move_folder()
    shutil_copy_folder()
    shutil_make_archive()
    os.remove("test_archive.zip")
    shutil.rmtree("test_dir/")
    shutil.rmtree("test_dir_copy/")

