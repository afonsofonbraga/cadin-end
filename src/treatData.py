from sgp4.api import Satrec
import sqlite3
from sgp4.functions import jday
from query import reset_debri, insert_debri
from Debris import Debris

def importData():
    try:
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()

        sqlite_select_query = """SELECT * FROM tle"""

        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        con.close()

        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            # row[0] -> name
            # row[1] -> s
            # row[2] -> t
            satellite = Satrec.twoline2rv(row[1], row[2])
            jd, fr = 2458827, 0.362605  #??????????
            e, r, v = satellite.sgp4(jd, fr)
            if (e == 0):
                new_debri = Debris(row[0],r,v)
                insert_debri(new_debri)
    except:
        print("Could not fetch data.")
importData()