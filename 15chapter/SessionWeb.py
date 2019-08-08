import web
web.config.debug = False
urls = (
	"/","countUsers",
	"/reset","resetSession",
)
app = web.application(urls,locals())
if web.config.get('_session') is None:
	session = web.session.Session(app,web.session.DiskStore('sessions'),{'count':0})    # 把session信息存储到内存上，初始计数为0
else:
	session = web.config._session

class countUsers:
	def GET(self):
		session.count+=1            # 访问用户数累计
		return str(session.count)

class resetSession:
	def GET(self):
		session.kill()
		return "已执行"
if __name__=='__main__':
	app.run()


