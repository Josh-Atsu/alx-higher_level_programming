#!/usr/bin/python3
"""List all states in databas and select according to user input"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd="", db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
                .format(sys.argv[4]))
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
