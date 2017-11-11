# -*- codiing:utf-8 -*-
"""os example"""
__author__="aaron.qiu"

"""connect mysql database test"""

# 导入MySQL驱动:
import mysql.connector
import logging

def queryDataTest():
    try:
        conn = mysql.connector.connect(host='192.168.1.112',user='root', password='root', database='mydb')
        #cursor = conn.cursor()
        #cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        #cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
        #print(cursor.rowcount)
        #conn.commit()
        #cursor.close()
        # 运行查询:
        cursor = conn.cursor()
        cursor.execute('select * from tbl_user where id = %s', ('1111111e',))
        values = cursor.fetchall()
        print(values)
    except Exception  as err:
        logging.error(err)
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    queryDataTest()