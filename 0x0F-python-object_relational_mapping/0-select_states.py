#!/usr/bin/python3
"""List all states in database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd="", db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
