# -*- coding:utf-8 -*-
"""
参考 https://docs.pytest.org/en/latest/getting-started.html

pip install -U pytest
pytest -q test_sysexit.py
pytest --version
pytest -k TestClassDemoInstance -q
pytest -q test_tmp_path.py
pytest --fixtures   # shows builtin and custom fixtures
"""
__author__ = "aaron.qiu"

import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1


# content of test_tmp_path.py
# Request a unique temporary directory for functional tests
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0
