# -*- coding: utf-8 -*-
"""面向对象"""
__author__="Aaron.qiu"

class Person(object):
    birthday = "2017-10-11" # class variable shared by all instances static variable

    def __init__(self,name,age):
        """构造函数"""
        self.__name = name  # instance variable unique to each instance

        self.__age = age

    def printPersonInfo(self):
        print('%s的年龄是%d'%(self.__name,self.__age))

    def __str__(self):
        return 'Person object (name: %s)' % self.__name
    __repr__ = __str__

class Animal(object):
    def run(self):
        pass

class Dog(Animal):
    print('Dog is running...')

class Cat(Animal):
    print('Cat is running...')

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

if __name__=="__main__":
    person = Person("aaron",25)
    person.__age=23
    person.printPersonInfo()
    print(person)

    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()

    print(isinstance(cat, Animal))
    print(hasattr(cat, 'x')) # 有属性'x'吗？)
    print(getattr(person, '__age'))  # 获取属性'z'

    print(dir('ABC'))
    print(type(2))

    student = Student()
    student.set_score(100)
    print(student.get_score())
