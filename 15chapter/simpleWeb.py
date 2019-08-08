from http.server import *

class RequestHandler(BaseHTTPRequestHandler):
	Page = '''\
	<html>
	<body>
	<p>Hello Web!</p>
	</body>
	</html>
	'''
	def do_GET(self):                                       # 重写该父类的do_GET方法
		self.send_response(200)                             # 返回响应码，200代表成功
		self.protocol_version="HTTP/1.1"                    # 指定HTTP协议版本
		self.send_header("Content-Type","text/html")        # 告诉浏览器返回内容的格式
		self.send_header("Content-Length",str(len(self.Page)))
		self.end_headers()
		self.wfile.write(self.Page.encode('utf-8'))

if __name__=='__main__':
	serverAddress = ('127.0.0.1',8099)
	server =  HTTPServer(serverAddress,RequestHandler)      # 创建web服务器实例
	server.serve_forever()
