# -*- coding:utf-8 -*-

"""write showcase"""
__author__ = "aaron.qiu"

import sys
import pprint

def write_file():
    """
    r	Open file for reading
    w	Open file for writing (will truncate file)
    b	binary more
    r+	open file for reading and writing
    a+	open file for reading and writing (appends to end)
    w+	open file for reading and writing (truncates files)
    """
    # Filename to write
    filename = "test.txt"

    # Open the file with writing permission
    myfile = open(filename, 'w')

    # Write a line to the file
    myfile.write('Written with Python\n')

    # Close the file
    myfile.close()


def append_file():
    # Filename to append
    filename = "test.txt"

    # The 'a' flag tells Python to keep the file contents
    # and append (add line) at the end of the file.
    myfile = open(filename, 'a')

    # Add the line
    myfile.write('Written with Python\n')

    # Close the file
    myfile.close()
    # Filename to append
    filename = "test.txt"

    # The 'a' flag tells Python to keep the file contents
    # and append (add line) at the end of the file.
    myfile = open(filename, 'a')

    # Add the line
    myfile.write('Written with Python\n')

    # Close the file
    myfile.close()


if __name__ == "__main__":
    write_file()
    append_file()
