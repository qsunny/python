# -*- coding:utf-8 -*-

"""sqlite showcase"""
__author__ = "aaron.qiu"

import sqlite3 as lite
import sys
import pprint


def test_conn():
    """test connection"""
    con = None

    try:
        con = lite.connect('test.db')
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print("SQLite version: %s" ,data)
    except lite.Error as e:
        print("Error %s:", e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


def create_user_table():
    """create user table"""
    con = None
    try:
        con = lite.connect('user.db')

        with con:
            cur = con.cursor()
            # if exist_table():
            #     cur.execute("drop table t_user")
            # cur.execute("CREATE TABLE t_user(Id INT, Name TEXT)")
            cur.execute("CREATE TABLE IF NOT EXISTS t_user(Id INT, Name TEXT)")
            cur.execute("INSERT INTO t_user VALUES(1,'Michelle')")
            cur.execute("INSERT INTO t_user VALUES(2,'Sonya')")
            cur.execute("INSERT INTO t_user VALUES(3,'Greg')")
    except lite.Error as e:
        print("Error %s:", e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


def query_user():
    """query user record"""
    con = None
    try:
        con = lite.connect('user.db')

        with con:
            cur = con.cursor()
            cur.execute("select * from t_user")
            rows = cur.fetchall()

            for row in rows:
                print(row)
    except lite.Error as e:
        pprint("Error %s:", e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


def exist_table():
    """exist user table"""
    con = None
    try:
        con = lite.connect('user.db')

        with con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(1) flag FROM sqlite_master where type='table' and name='t_user'")
            row = cur.fetchone()
            # print(row)
            if row is not None and row[0] == 1:
                return True
            else:
                return False
    except lite.Error as e:
        pprint("Error %s:", e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


if __name__ == "__main__":
    test_conn()
    create_user_table()
    query_user()
    # exist_flag = exist_table()
    # print(exist_flag)

