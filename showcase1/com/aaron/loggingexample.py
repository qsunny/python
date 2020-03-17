# -*- coding: utf-8 -*-
"""日志"""
__author__="Aaron.qiu"

import logging

def logging_showcase():
    """默认情况下，logging 的日志级别为 WARNING，只有不低于 WARNING 级别的日志才会显示在命令行。"""
    logging.critical('This is critical message')
    logging.error('This is error message')
    logging.warning('This is warning message')
    # 不会显示
    logging.info('This is info message')
    logging.debug('This is debug message')

    logging.root.setLevel(level=logging.INFO)
    logging.info('This is info message')

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')

    logger = logging.getLogger("this program")

    logger.critical('This is critical message')


if __name__=="__main__":
    logging_showcase()
