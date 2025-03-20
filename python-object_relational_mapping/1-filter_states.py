#!/usr/bin/python3
""" Module that lists all states with a name starting with N from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states name ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()