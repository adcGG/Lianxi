import web
urls = (
	'/','Index',
	'/login','Login',
	'logout','Logout',
)
render = web.template.render('templates/')
firstSet = (
	('admin','123')                             # 设置访问登录页面的初始用户名密码
)
web.config.debug = False
app = web.application(urls,locals())
session = web.session.Session(app,web.session.DiskStore('session'))
class Index:
	def GET(self):
		if session.get('logged_in',False):
			return '<h1>成功！</h1><a href="/logout">Logout</a>'.encode("utf-8")
		raise web.seeother("/login")

class Login:
	def GET(self):
		return render.login()
	def POST(self):
		i = web.input()
		username = i.get('username')
		passwd = i.get('passwd')
		if (username,passwd) in firstSet:
			session.logged_in = True
			web.setcookie('test','',3600)
			raise web.seeother('/')
		else:
			return '<h1>出错！</h1><a href="/login">Login</a>'.encode("utf-8")

class Logout:
	def GET(self):
		session.logged_in  = False
		raise web.seeother("/login")
if __name__=='__main__':
	app.run()

