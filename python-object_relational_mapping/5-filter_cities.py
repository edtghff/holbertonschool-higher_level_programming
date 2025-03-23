#!/usr/bin/python3
"""Module that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )

    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = '{}' ORDER BY cities.id ASC".format(state_name)

    cursor = db.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()