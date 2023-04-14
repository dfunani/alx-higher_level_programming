#!/usr/bin/python3
"""*.py
Application for running sql scripts either using
ORM or DDL"""
import sys
import MySQLdb

localhost = 'localhost'
port = 3306
charset = 'utf8'

def main(username, password, name):
    """Project-Entry
    Description: runs a sql query

    username: __str__
    password: __str__
    name: __str__

    return: None
    """
    db = MySQLdb(host=localhost, port=port, user=username, passwd=password,\
                 db=name, charset=charset)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {name}.states ORDER BY states.id")
    result = cursor.fetchall()
    for i, elem in enumerate(result, 1):
        print((i, elem))
    return


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()