import web
import sqlite3
from datetime import datetime,date
render = web.template.render('templates/')
urls = (
	'/','index'
)

def GetDayHello():
	dd = datetime.now()
	showDay = str(dd.year)+'-'+str(dd.month)+'-'+str(dd.day)
	name = ''
	conn = sqlite3.connect('ShowDB')
	cur = conn.cursor()
	cur.execute("select * from T_Show")
	for row in cur.fetchall():
		if row[0]==showDay:
			name = row[1]
			break
	if name == '':
		name = "World"
	conn.close()
	return name


class index:
	def GET(self):
		name =GetDayHello()
		return render.Show_temp(name)

if __name__=='__main__':
	# conn = sqlite3.connect('ShowDB')
	# cur = conn.cursor()
	# cur.execute("create table T_Show(date text,ShowInf text)")
	# cur.execute('insert into T_Show VALUES ("2019-7-6","Dog")')
	# cur.execute('insert into T_Show VALUES ("2019-7-7","Cat")')
	# cur.execute('insert into T_Show VALUES ("2019-7-8","三酷猫")')
	# cur.execute('insert into T_Show VALUES ("2019-7-9","大佬狗")')
	# conn.commit()
	# conn.close()
	app = web.application(urls,globals())
	app.run()