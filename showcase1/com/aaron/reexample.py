# -*- codiing:utf-8 -*-
"""regular expressions example"""
__author__="aaron.qiu"

import re

def matchShowcase():
    pattern = re.compile(r'hello',re.I)
    word = "hello,world,Hello,Express reguration"

    result1 = re.match(pattern,word)
    result2 = re.match(pattern, 'helloo CQC!')
    result3 = re.match(pattern, 'helo CQC!')
    result4 = re.match(pattern, 'hello CQC!')
    print(result1)
    if result1:
        print(result1.group())
    else:
        print("result1匹配失败")

    # 如果2匹配成功
    if result2:
        # 使用Match获得分组信息
        print(result2.group())
    else:
        print('2匹配失败！')

    # 如果3匹配成功
    if result3:
        # 使用Match获得分组信息
        print(result3.group())
    else:
        print('3匹配失败！')

    # 如果4匹配成功
    if result4:
        # 使用Match获得分组信息
        print(result4.group())
    else:
        print('4匹配失败！')

def searchShowcase():
    # 将正则表达式编译成Pattern对象
    pattern = re.compile(r'world')
    match = re.search(pattern, 'hello world!')
    if match:
        # 使用Match获得分组信息
        print(match.group())

def splitShowcase():
    pattern = re.compile(r'\d+')
    print(re.split(pattern, 'one1two2three3four4'))

def findallShowcase():
    pattern = re.compile(r'\d+')
    print(re.findall(pattern, 'one1two2three3four4'))

def finditerShowcase():
    pattern = re.compile(r'\d+')
    for m in re.finditer(pattern, 'one1two2three3four4'):
        print(m.group())

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

def subShowcase():
    pattern = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world!'
    print(re.sub(pattern, r'\2 \1', s))
    print(re.sub(pattern, func, s))

if __name__=="__main__":
    #matchShowcase()
    #searchShowcase()
    #splitShowcase()
    #findallShowcase()
    #finditerShowcase()
    subShowcase()

