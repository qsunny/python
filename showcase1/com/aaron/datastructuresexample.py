# -*- codiing:utf-8 -*-
"""os example"""
__author__="aaron.qiu"

import os
from collections import deque
from math import pi

def dictShowcase():
    """dict example"""
    tel = {'jack': 4098, 'sape': 4139}
    print(tel['jack'])
    print(tel)
    del tel['sape']
    print(tel)
    dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(dict1)
    print({x: x**2 for x in (2, 4, 6)})
    print(dict(sape=4139, guido=4127, jack=4098))
    #loop
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)

    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    #多个队列循环
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

    #反转队列
    for i in reversed(range(1, 10, 2)):
        print(i)

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    #排序
    for f in sorted(set(basket)):
        print(f)


def listShowcase():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    #统计
    print(fruits.count('apple'))
    print(fruits.index('banana'))
    print(fruits.index('banana', 4))
    fruits.reverse()
    print(fruits)
    fruits.sort()
    print(fruits)
    print(fruits.pop())

    #Using Lists as Stacks
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)
    print(stack.pop())

    #Using Lists as Queues first-in, first-out
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")  # Terry arrives
    queue.append("Graham")  # Graham arrives
    print(queue.popleft())  # The first to arrive now leaves
    print(queue)

    squares = []
    for x in range(10):
        squares.append(x ** 2)
        print(squares)

    print("===================")
    squares = list(map(lambda x: x ** 2, range(10)))   #equivalently: squares = [x**2 for x in range(10)]
    print(squares)

    condictionList = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(condictionList)

    print([str(round(pi, i)) for i in range(1, 6)])

    #Nested List Comprehensions
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
    print([[row[i] for row in matrix] for i in range(4)])

def tupleShowcase():
    """A tuple consists of a number of values separated by commas"""
    t = 12345, 54321, 'hello!'
    print(t[0])
    print(t)

    # Tuples may be nested:
    u = t, (1, 2, 3, 4, 5)
    print(u)

def setShowcase():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    # fast membership testing
    print('orange' in basket)
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(b)
    print("============================")
    print(a-b) # letters in a but not in b
    print(a|b)  # letters in a or b or both
    print(a&b)  # letters in both a and b
    print(a^b)  # letters in a or b but not both

    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)

if __name__ == "__main__":
    #dictShowcase()
    #listShowcase()
    #tupleShowcase()
    setShowcase()