#!/usr/bin/python3
"""cities by states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd="", db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    res = cur.fetchall()
    lst = list(name[0] for name in res)
    print(*lst, sep=", ")
    cur.close()
    db.close()
