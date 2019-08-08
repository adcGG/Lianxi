import web
web.config.debug = False
urls = (
	"/","countUsers",
	"/reset","resetSession",
)
db = web.database(dbn='sqlite',db='SessionDB')          # 连接sqlite的SessionDB数据库
app = web.application(urls,locals())                    # 根据URL通知web服务器调用对应的类
store = web.session.DBStore(db,'session')               # 建立session的内容存储到数据库表对象
# DBstore类封装了把指定session数据库存储到指定数据库表的过程，这里看不到相应的SQL语句

session = web.session.Session(app,store,{'count':0})    # 用户访问信息存储到sessions表中
web.config.session_parameters['cookie_name'] = 'webpy_session_id'       # cookie_name ——保存session id 的Cookie的名称
web.config.session_parameters['cookie_domain'] = None                   # cookie_domain——保存session id的Cookie的domain信息
web.config.session_parameters['timeout'] = 86400                        # timeout——session的有效时间，以秒为单位
web.config.session_parameters['ignore_expiry'] = True                   # ignore_expiry如果为True session就永不过期
web.config.session_parameters['ignore_change_ip'] = True                # ignore_change_ip——如果为False 就表名只有在访问
																		# 该session的IP与创建该session的IP完全一致时，session才被允许访问
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'    # 密码种子，为session加密提供一个字符串种子
web.config.session_parameters['expired_message'] ='Session expired'     # session过期时显示的提示信息


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


