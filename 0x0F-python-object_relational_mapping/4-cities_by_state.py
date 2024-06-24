#!/usr/bin/python3
"""cities by states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd="", db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON states.id=cities.state_id""")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
