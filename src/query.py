import sqlite3
import numpy as np

def create_tables():
    con = sqlite3.connect('../data/database.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE if not EXISTS debris_name (name_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
    cur.execute('''CREATE TABLE if not EXISTS debris (debris_name_id INTEGER PRIMARY KEY, pos1 REAL, pos2 REAL, pos3 REAL, vel1 REAL, vel2 REAL, vel3 REAL, FOREIGN KEY(debris_name_id) REFERENCES debris_name(name_id))''')
    cur.execute('''CREATE TABLE if not EXISTS tle (debris_name_id INTEGER PRIMARY KEY, s TEXT, t TEXT, FOREIGN KEY(debris_name_id) REFERENCES debris_name(name_id))''')
    con.commit()
    con.close()

def get_debris_id(debris_name):
    con = sqlite3.connect('../data/database.db')
    cur = con.cursor()
    try:
        sqlite_select_query = """SELECT * FROM debris_name WHERE name=?"""
        cur.execute(sqlite_select_query,(debris_name,))
    except:
        con.close()
        create_tables()
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()
        sqlite_select_query = """SELECT * FROM debris_name WHERE name=?"""
        cur.execute(sqlite_select_query,(debris_name,))

    records = cur.fetchall()
    if np.size(records) == 0:
        cur.execute('''INSERT INTO debris_name (name) VALUES (?)''',(debris_name,))
        con.commit()
        sqlite_select_query = """SELECT * FROM debris_name WHERE name=?"""
        cur.execute(sqlite_select_query,(debris_name,))
        records = cur.fetchall()
    con.close()
    return records[0][0]

def get_debris_name(debris_id):
    con = sqlite3.connect('../data/database.db')
    cur = con.cursor()
    try:
        sqlite_select_query = """SELECT * FROM debris_name WHERE name_id=?"""
        cur.execute(sqlite_select_query,(debris_id,))
        con.commit()
        records = cur.fetchall()
        con.close()
    except:
        con.close()
        print("Failed to get debris name.")
        return None
    if np.size(records) != 0:
        print("Found")
        return records[0][1]
    else:
        print("Empty debris name search.")
        return None

def insert_debri(debri):
    debris_id = debri.name
    try:
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()
        print(debris_id)
        cur.execute('''INSERT OR REPLACE INTO debris (debris_name_id, pos1, pos2, pos3, vel1, vel2, vel3) VALUES (?,?,?,?,?,?,?)''',(debris_id,debri.pos1,debri.pos2,debri.pos3,debri.vel1,debri.vel2,debri.vel3,))
        con.commit()
    except:
        print("ERROR INSERTING DEBRIS VALUE!!!!!!")
    con.close()

def insert_tle(tle):
    tle_id = 0
    try:
        tle_id = get_debris_id(tle.name[0])
    except:
        create_tables()
        tle_id = get_debris_id(tle.name[0])
    try:
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()
        cur.execute("""INSERT OR REPLACE INTO tle (debris_name_id,s,t) VALUES (?,?,?)""",(tle_id,tle.s,tle.t,))
        con.commit()
    except:
        print("ERROR INSERTING TLE VALUE!!!!!!")
    con.close()


def clear_tables():
    con = sqlite3.connect('../data/database.db')
    cur = con.cursor()
    try:
        cur.execute('''DROP TABLE debris_name''')
        cur.execute('''DROP TABLE debris''')
        cur.execute('''DROP TABLE tle''')
    except:
        print("Table not available.")
    con.close()