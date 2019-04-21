# -*- coding: utf-8 -*-
'''
Created on 2019-04-20
@FileName: base_dao.py
@Description: 基础dao
@author: 'Aaron.Qiu'
@version V1.0.0
'''

from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

'''
# default
engine = create_engine('mysql://scott:tiger@localhost/foo')
# mysql-python
engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')
engine = create_engine("mysql+mysqldb://weiyz:123@localhost:3306/test")
# MySQL-connector-python
engine = create_engine('mysql+mysqlconnector://scott:tiger@localhost/foo')
# OurSQL
engine = create_engine('mysql+oursql://scott:tiger@localhost/foo')
'''

Base = declarative_base()

# 定义Component对象:
class Component(Base):
    # 表的名字:
    __tablename__ = 't_component'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    category1 = Column(String(256))
    category2 = Column(String(256))
    category3 = Column(String(256))
    category4 = Column(String(256))
    category_type_num = Column(String(64))

    def __repr__(self):
        return "id:%d,category1:%s,category2:%s,category3:%s,category4:%s,categoryTypeNum:%s" % (self.id, self.category1, self.category2,self.category3,self.category4,self.category_type_num)

# 定义Component对象:
class ComponentProps(Base):
    # 表的名字:
    __tablename__ = 't_component_prop'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    prop_name = Column(String(512))
    prop_value = Column(String(1024))
    category_type_num = Column(String(64))
    # category_type_num = Column(String(64), ForeignKey('t_component.category_type_num'))
    # 请注意，设置外键的时候用的是表名.字段名。其实在表和表类的抉择中，只要参数是字符串，往往是表名；如果是对象则是表类对象。
    component_id = Column(Integer, ForeignKey('t_component.id'))
    component = relationship('Component', backref="ComponentProps")
    # component = relationship('Component', foreign_keys=category_type_num)
    # componentFollow = relationship('Component', foreign_keys=component_id)





engine = create_engine('sqlite:///app.db?check_same_thread=False', echo=True)
Session = sessionmaker(bind=engine)

def create_db():
    # 创建数据表
    Base.metadata.create_all(engine)

def drop_db():
    # 删除数据表
    Base.metadata.drop_all(engine)



