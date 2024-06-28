#!/usr/bin/python3

""" This code list all the states from a given database
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states INNER JOIN cities ON\
                states.id=cities.state_id WHERE states.name='{}'".
                format(sys.argv[4]))

    result = cur.fetchall()

    for i in range(len(result)):
        print(result[i][0], end="")
        if i + 1 < len(result):
            print("", end=', ')
