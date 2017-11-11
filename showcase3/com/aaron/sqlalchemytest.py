# -*- codiing:utf-8 -*-
"""os example"""
__author__="aaron.qiu"

"""
    connect mysql database test
    pre request :pip install sqlalchemy
"""

# 导入MySQL驱动:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER
import logging

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'tbl_user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    username = Column(String(20))
    password = Column(String(20))
    age = Column(INTEGER)

# 初始化数据库连接: '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@192.168.1.112:3306/mydb')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def add():
    try:
        # 创建session对象:
        session = DBSession()
        # 创建新User对象:
        new_user = User(id='4535545', username='Bob',password="888888",age=32)
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()

    except Exception  as err:
        logging.error(err)
    finally:
        # 关闭session:
        session.close()


def query():
    try:

        # 创建Session:
        session = DBSession()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = session.query(User).filter(User.id == '111111eee').one()
        # 打印类型和对象的name属性:
        print('type:', type(user))
        print('username:', user.username)

    except Exception  as err:
        logging.error(err)
    finally:
        # 关闭Session:
        session.close()

if __name__=="__main__":
    #add()
    query()