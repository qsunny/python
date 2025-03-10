# coding: utf-8

"""
pip install records[pandas]
"""

import json # https://docs.python.org/3/library/json.html
import requests # https://github.com/kennethreitz/requests
import records # https://github.com/kennethreitz/records

if  __name__ == "__main__":
    # randomuser.me generates random 'user' data (name, email, addr, phone number, etc)
    r = requests.get('http://api.randomuser.me/0.6/?nat=us&results=10')
    j = r.json()['results']
    print(j)

    # Valid SQLite URL forms are:
    #   sqlite:///:memory: (or, sqlite://)
    #   sqlite:///relative/path/to/file.db
    #   sqlite:////absolute/path/to/file.db

    # records will create this db on disk if 'users.db' doesn't exist already
    db = records.Database('sqlite:///users.db')

    db.query('DROP TABLE IF EXISTS persons')
    db.query('CREATE TABLE persons (key int PRIMARY KEY, fname text, lname text, email text)')

    for rec in j:
        user = rec['user']
        name = user['name']

        key = user['registered']
        fname = name['first']
        lname = name['last']
        email = user['email']
        db.query('INSERT INTO persons (key, fname, lname, email) VALUES(:key, :fname, :lname, :email)',
                key=key, fname=fname, lname=lname, email=email)

    rows = db.query('SELECT * FROM persons')
    print(rows.export('csv'))

