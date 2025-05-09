#!/usr/bin/python3
""" Module that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306, user=mysql_username,
        passwd=mysql_password, db=database_name,
        charset="utf8"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()