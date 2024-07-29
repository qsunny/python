# -*- codiing:utf-8 -*-
"""
Faker-用于创建假数据
pip install Faker

"""

__author__ = "aaron.qiu"

from faker import Faker


if  __name__ == "__main__":

    fake = Faker()
    print(fake.name())
    print(fake.address())
    print(fake.text())
    print(fake.bank_country())