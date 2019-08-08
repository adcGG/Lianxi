import web
import sqlite3
from datetime import datetime,date
render = web.template.render('templates/')
urls = (
	'/','index',
	'/add','add',
)
dd = datetime.now()
showDay = str(dd.year)+'-'+str(dd.month)+'-'+str(dd.day)

def GetDayHello():
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

def InsertHello(name):
	conn = sqlite3.connect("ShowDB")
	cur = conn.cursor()
	cur.execute("insert into T_Show VALUES('"+showDay+"','"+name+"')")
	conn.commit()
	conn.close()



class index:
	def GET(self):
		name =GetDayHello()
		return render.Show_temp1(name)
class add:
	def POST(self):
		input1 = web.input(name = [])
		InsertHello(input1.title)

if __name__=='__main__':
	app = web.application(urls,globals())
	app.run()