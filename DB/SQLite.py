import sqlite3
# conn = sqlite3.connect(":memory:") # 建立第一个基于内存的数据库
conn = sqlite3.connect("First.db")
cur = conn.cursor()
# cur.execute('''Create table T_fish(date text,name text,nums int,price real,Explain text)''')
cur.execute("insert into T_fish VALUES ('2018-3-29','鲤鱼',17,10.3,'John')")
cur.execute("insert into T_fish VALUES ('2018-3-30','鲢鱼',9,9.3,'Tim')")
conn.commit()
cur.execute("select * from T_fish")
for row in cur.fetchall():
	print(row)
cur.execute("delete from T_fish where nums = 17")
conn.commit()
cur.execute("select * from T_fish")
for row in cur.fetchall():
	print(row)

conn.close()
