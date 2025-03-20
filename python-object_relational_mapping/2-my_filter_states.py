#!/usr/bin/python3
"""Module that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor = db.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
