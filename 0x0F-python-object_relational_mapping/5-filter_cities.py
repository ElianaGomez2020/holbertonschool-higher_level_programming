#!/usr/bin/python3
"""takes in the name of a state """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id \
                WHERE states.name=%s ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    dat = []
    for c in rows:
        dat.append(c[0])
    print(', '.join(dat))

    cur.close()
    db.close()
