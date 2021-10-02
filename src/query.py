import sqlite3

def reset_table():
    con = sqlite3.connect('/database.db')
    cur = con.cursor()
    try:
        cur.execute('''DROP TABLE debris''')
    except:
        print("Table not available.")

    cur.execute('''CREATE TABLE debris (name text, s text, t text)''')

    con.commit()

    con.close()

def inset_value(name, s, t):
    try:
        con = sqlite3.connect('/database.db')
        cur = con.cursor()
        cur.execute(f"INSERT INTO debris VALUES ('{name}',{s},{t})")
        con.commit()
        con.close()
    except:
        reset_table()
        try:
            con = sqlite3.connect('/database.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO debris VALUES ('{name}',{s},{t})")
            con.commit()
            con.close()
        except:
            print("ERROR INSERTING VALUE!!!!!!")