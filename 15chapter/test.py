import sqlite3
conn = sqlite3.connect('SessionDB')
cur = conn.cursor()
cur.execute("create table sessions(session_id char(128) UNIQUE NOT NULL ,atime timestamp NOT NULL DEFAULT current_timestamp ,"
            "data text)")
conn.commit()
conn.close()