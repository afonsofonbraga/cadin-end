import sqlite3

def reset_table():
    con = sqlite3.connect('/database.db')
    cur = con.cursor()
    try:
        cur.execute('''DROP TABLE debris''')
    except: pass

    cur.execute('''CREATE TABLE debris (name text, s text, t text)''')

    con.commit()

    con.close()

reset_table()