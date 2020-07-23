from loguru import logger
logger.add('D:/logs/z_project.log',
           level='DEBUG',
           format='{time:YYYY-MM-DD HH:mm:ss} - {level} - {file} - {line} - {message}',
           rotation="10 MB")
logger.info('可以写日志了')


@logger.catch
def test():
    'a' + 1


if __name__ == '__main__':
    test()
    logger.info('可以用了')
