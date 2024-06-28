#!/usr/bin/python3
""" This code list all the states from a given database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s", (sys.argv[4],))
    for state in cur.fetchall():
        print(state)
