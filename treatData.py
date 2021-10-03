from sgp4.api import Satrec
import sqlite3
from sgp4.functions import jday
from query import insert_debri
from Debris import Debris

import astropy.time
from astropy.coordinates import TEME, CartesianDifferential, CartesianRepresentation, ITRS
from astropy import units as u
import numpy as np

def importDebris(time2):
    try:
        con = sqlite3.connect('database.db')
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
        year = int(time2.split(',')[0])
        month = int(time2.split(',')[1])
        day = int(time2.split(',')[2])
        hour = int(time2.split(',')[3])
        minute = int(time2.split(',')[4])
        second = int(time2.split(',')[5])

        jd, fr = jday(year, month, day, hour, minute, second)

        time3 = astropy.time.Time(jd + fr, format = 'jd')
        for row in records:
            # row[0] -> name_ID
            # row[1] -> s
            # row[2] -> t

            satellite = Satrec.twoline2rv(row[1], row[2])
            e, r, v = satellite.sgp4(jd, fr)
            if e == 0:
                debris_count += 1

                copyr = np.copy(r)
                r = CartesianRepresentation(r*u.km)
                copyv = np.copy(v)
                v = CartesianDifferential(v*u.km/u.s)
                teme = TEME(r.with_differentials(v), obstime=time3)
                itrs = teme.transform_to(ITRS(obstime=time3))
                location = itrs.earth_location

                longitude = int(str(location.geodetic.lon).split('d')[0])
                latitude = int(str(location.geodetic.lat).split('d')[0])
                height = float(str(location.geodetic.height).split('km')[0])

                r = [longitude, latitude, height]
                new_debri = Debris(row[0],r,copyv)
                insert_debri(new_debri)
        print("From", len(records), "tle objects,", debris_count,"debris were added into the database.")
    except:
        print("Probelma nos dados")

importDebris('2021,10,03,17,37,23')