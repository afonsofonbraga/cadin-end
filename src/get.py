from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import sqlite3
from query import get_debris_name

db_connect = create_engine('sqlite:///../data/database.db')
app = Flask(__name__)
api = Api(app)

def createJson():
    try:
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()

        sqlite_select_query = """SELECT * FROM debris"""

        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        con.close()

        print("Imported", len(records), "tle objects from database.")
    except:
        print("Could not fetch data from tle database.")
    try:
        Dict = {}
        for row in records:
            name = get_debris_name(row[0])
            alt = row[1]
            lat = row[2]
            lon = row[3]
            a= {
                'debris_name': name,
                'altitude': alt,
                'latitude': lat,
                'longitude': lon
            }
            Dict.append(a)
        json2 = dumps(Dict)
        return json2
    except:
        print("error")
teste = createJson()
print(teste)