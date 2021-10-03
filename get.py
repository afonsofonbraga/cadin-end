from json import dumps
import sqlite3
from query import get_debris_name

def createJson():
    try:
        con = sqlite3.connect('database.db')
        cur = con.cursor()

        sqlite_select_query = """SELECT * FROM debris"""

        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        con.close()

        print("Imported", len(records), "tle objects from database.")
    except:
        print("Could not fetch data from tle database.")
    try:
        List = []
        for row in records:
            name = get_debris_name(row[0])
            lon = row[1]
            lat = row[2]
            alt = row[3] * 1000
            a= {
                'debris_name': name,
                'altitude': alt,
                'latitude': lat,
                'longitude': lon
            }
            List.append(a)
        json2 = dumps(List, indent=4)
        return json2
    except:
        print("error")
teste = createJson()
print(teste)