#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    #connecting to mysql-db
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd="", db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states""")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
