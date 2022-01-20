# -*- coding:utf-8 -*-
"""
参考 https://tox.wiki/en/latest/

# content of: tox.ini , put in same dir as setup.py
[tox]
envlist = py27,py36

[testenv]
# install pytest in the virtualenv where commands will be executed
deps = pytest
commands =
    # NOTE: you can run any command line tool here - not just tests
    pytest



tox
tox -e py36
"""
__author__ = "aaron.qiu"

import pytest
import time

from tox_example.src.app import math_fabs, math_ceil,increate


def test_math_fabs():
    assert math_fabs(-1.2) == 1.2
    assert math_fabs(0) == 0
    assert math_fabs(2.4) == 2.4


def test_math_ceil():
    assert math_ceil(-1.2) == -1
    assert math_ceil(0) == 0
    assert math_ceil(2.4) == 3


def test_answer():
    assert increate(4) == 5



