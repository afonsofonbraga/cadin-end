import sqlite3
import numpy as np
from Debris import Debris


def importData():
    con = sqlite3.connect('../data/database.db')
    cur = con.cursor()

    sqlite_select_query = """SELECT * FROM debris"""

    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
        print("name: ", row[0])
        print("t: ", row[1])
        print("s: ", row[2])
        print("\n")
    con.commit()
    con.close()

importData()