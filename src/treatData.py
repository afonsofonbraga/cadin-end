from sgp4.api import Satrec,jday
import sqlite3
from sgp4.functions import jday
from query import insert_debri
from Debris import Debris

def importDebris(time):
    try:
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()

        sqlite_select_query = """SELECT * FROM tle"""

        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        con.close()

        debris_count = 0
        print("Imported", len(records), "tle objects from database.")
    except:
        print("Could not fetch data from tle database.")
    try:
        for row in records:
            # row[0] -> name_ID
            # row[1] -> s
            # row[2] -> t
            satellite = Satrec.twoline2rv(row[1], row[2])

            year = int(time.split(',')[0])
            month = int(time.split(',')[1])
            day = int(time.split(',')[2])
            hour = int(time.split(',')[3])
            minute = int(time.split(',')[4])
            second = int(time.split(',')[5])
            jd, fr = jday(year, month, day, hour, minute, second)
            e, r, v = satellite.sgp4(jd, fr)
            if e == 0:
                debris_count += 1
                new_debri = Debris(row[0],r,v)
                insert_debri(new_debri)
        print("From", len(records), "tle objects,", debris_count,"debris were added into the database.")
    except:
        print("Probelma nos dados")