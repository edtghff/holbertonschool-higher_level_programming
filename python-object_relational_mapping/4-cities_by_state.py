#!/usr/bin/python3
"""Module that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )

    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    cursor = db.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
