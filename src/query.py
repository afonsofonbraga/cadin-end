import sqlite3
from Debris import Debris
from Tle import Tle

def reset_debri():
    con = sqlite3.connect('../data/database.db')
    cur = con.cursor()
    try:
        cur.execute('''DROP TABLE debris''')
    except:
        print("Table not available.")
    cur.execute('''CREATE TABLE debris (name text, pos1 real, pos2 real, pos3 real, vel1 real, vel2 real, vel3 real)''')
    con.commit()

    con.close()

def reset_tle():
    con = sqlite3.connect('../data/database.db')
    cur = con.cursor()
    try:
        cur.execute('''DROP TABLE tle''')
    except:
        print("Table not available.")

    cur.execute('''CREATE TABLE tle (name text, s text, t text)''')
    con.commit()

    con.close()

def insert_debri(debri):
    try:
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()
    except:
        reset_debri()
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()
    try:
        cur.execute(f"INSERT INTO debris VALUES ('{debri.name}','{debri.pos1}','{debri.pos2}','{debri.pos3}','{debri.vel1}','{debri.vel2}','{debri.vel3}')")
        con.commit()
    except:
            print("ERROR INSERTING VALUE!!!!!!")
    con.close()

def insert_tle(tle):
    try:
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()
    except:
        reset_tle()
        con = sqlite3.connect('../data/database.db')
        cur = con.cursor()
    try:
        cur.execute(f"INSERT INTO tle VALUES ('{tle.name}','{tle.s}','{tle.t}')")
        con.commit()
    except:
            print("ERROR INSERTING VALUE!!!!!!")
    con.close()