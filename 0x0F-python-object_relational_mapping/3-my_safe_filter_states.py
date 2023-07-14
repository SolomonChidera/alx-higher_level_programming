#!/usr/bin/python3
"""
a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from
MySQL injections!
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (arg,))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
