#!/usr/bin/python3
"""List all states in database"""
import MySQLdb
import sys


if __name__ == "__main__":
    #connecting to mysql-db
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd="", db=sys.argv[3])
    #create cursor
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
