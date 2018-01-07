# -*- coding:utf-8 -*-
"""zip usage example"""
__author__="Aaron.Qiu"

def make_iterator():
    """做迭代器"""
    colors = ['red','green','blue']
    indexs = [34,45,22,67]
    for col,index in zip(colors,indexs):
        print(col,index)

def puts(arg1,arg2):
    print(arg1)
    print(arg2)

def split_list(dots):
    x_lst,y_lst = zip(*dots)
    print(x_lst)
    print(y_lst)

def make_dict():
    keys = ['spam', 'eggs']
    vals = [42, 1729]
    d = dict(zip(keys, vals))
    print(d)
    inv_d = dict(zip(d.values(), d.keys()))
    print(inv_d)


if __name__=="__main__":
    make_iterator()
    args = ['apple','eggs']
    puts(*args)
    dots = [(1,2),(3,6),(9,6)]
    split_list(dots)
    mtx = [(1, 2),(3, 4),(5, 6)]
    print(zip(*mtx))
    print(zip(*mtx[::-1]))
    seq = range(1, 10)
    print(zip(*[iter(seq)] * 3))

    x = iter(range(1, 10))
    print(zip(x, x, x))

    make_dict()
