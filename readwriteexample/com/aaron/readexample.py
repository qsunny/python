# -*- coding:utf-8 -*-

"""write showcase"""
__author__ = "aaron.qiu"

import os


def read_file():
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

    # Open the file as f.
    # The function readlines() reads the file.
    if not os.path.isfile(filename):
        print('File does not exist.')
    else:
        with open(filename) as f:
            content = f.readlines()

    # Show the file contents line by line.
    # We added the comma to print single newlines and not double newlines.
    # This is because the lines contain the newline character '\n'.
    for line in content:
        print(line)


def read_file2():
    # Filename to append
    filename = "test.txt"

    # Open the file as f.
    # The function readlines() reads the file.
    if not os.path.isfile(filename):
        print('File does not exist.')
    else:
        with open(filename) as f:
            content = f.read().splitlines()

    # Show the file contents line by line.
    # We added the comma to print single newlines and not double newlines.
    # This is because the lines contain the newline character '\n'.
    for line in content:
        print(line)


if __name__ == "__main__":
    # read_file()
    read_file2()
